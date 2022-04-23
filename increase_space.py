import os
import time
import requests
import boto3
import subprocess
from pprint import pprint

#GLOBALS
trigger_percentage = 90
increase_by = 10

def get_ouput(command):
    '''Runs the command in linux terminal and returns the output'''
    output = subprocess.getoutput(command)
    return output

def get_disks():
    response = get_ouput('df -h')
    response = response.split('\n')
    keys = ['Filesystem','Size','Used','Avail','Use%','Mounted on']

    response.pop(0)
    result = []

    for disk in response:
        result.append(dict(zip(keys,disk.split())))

    #pprint(result)       
    return result

def get_no(p):
    p = list(p)
    p.pop(-1)
    return int(''.join(p))

def get_volume_ids():
    res = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    instance_id = res.text
    #instance_id = 'i-022221e7b8245afaf'
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    result = []
    for device in instance.block_device_mappings:
        volume = device.get('Ebs')
        # print(volume)
        # print(volume.get('VolumeId'))
        result.append(volume.get('VolumeId'))
    return result

def vol_inc_aws(v_id,current_size):
    '''Increases the volume from aws'''
    
    ec2 = boto3.client('ec2')
    response = ec2.modify_volume(
        DryRun=True,#|False,
        VolumeId=v_id,
        Size=current_size+increase_by,
        #VolumeType='standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
        #Iops=123,
        #Throughput=123,
        #MultiAttachEnabled=True|False
    )

def increase_space(fs):
    #increase the space from aws first and then run the commands on the terminal
    aws_volumes = get_volume_ids()
    ec2 = boto3.resource('ec2')
    mount_point = fs['Mounted on']

    req_id = ''
    current_size = 0
    for v_id in aws_volumes:
        volume = ec2.Volume(v_id)
        v_data = volume.attachments

        if mount_point == '/' and v_data[0]['Device'] == '/dev/xvda':
            req_id = v_data[0]['VolumeId']
            current_size = volume.size
        if mount_point == '/apps' and v_data[0]['Device'] == 'sdb':
            req_id = v_data[0]['VolumeId']
            current_size = volume.size
    
    vol_inc_aws(req_id,current_size)
    time.sleep(100)
    
    if mount_point == '/':
        commands = []
        if fs['Filesystem'] == '/dev/xvda1':
            commands = [
                'growpart /dev/xvda 1',
                'resize2fs /dev/xvda1',                   
            ]
        elif fs['Filesystem'] == '/dev/nvme0n1':
            commands = [
                'growpart /dev/nvme0n1 1',
                'resize2fs /dev/nvme0n1p1',  
            ]
        for c in commands:
            os.system(c)
            time.sleep(1)

    if mount_point == '/apps':
        commands = [
            'pvresize /dev/nvme1n1',
            'lvextend -i1 -l+100%FREE vg_app/lv_app',
            'resize2fs /dev/mapper/vg_app-lv_app',
        ]

        for c in commands:
            os.system(c)
            time.sleep(1)


if __name__ == '__main__':
    disks = get_disks()

    for d in disks:
        if get_no(d['Use%']) >= trigger_percentage:
            increase_space(d)