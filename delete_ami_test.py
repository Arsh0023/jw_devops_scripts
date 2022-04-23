import boto3, datetime
from datetime import date
from datetime import datetime
import sys
import os
import time

print(os.getcwd())
start_time = time.time()
project_name=str(sys.argv[1])
instance_node = {
        'prefix': str(sys.argv[1])+"-Ami-",
        'Region': str(sys.argv[2]),
        'delBefore': 10800
        }

strOfObjs = [instance_node]

for i in strOfObjs:
        prefix = i['prefix']
        Region = i['Region']
        delBefore = i['delBefore']


        now = datetime.now()
        now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        new_time = datetime.strptime(now_str,date_format)
        print(new_time)


        ec2 = boto3.client('ec2', region_name = Region)

        images=ec2.describe_images(Owners=['self'])
        amis_delted = 0
        try:
            for currImage in images['Images']:
                    if currImage['Name'].startswith(prefix):
                            amiId=currImage['ImageId']
                            print("ami_id :"+amiId)
                            creationDate=currImage['CreationDate']
                        # creationDate=creationDate[:10]
                        # creationDate=creationDate.replace("-", "/")
                            b = datetime.strptime(creationDate, date_format)
                            diff = new_time-b
                            print(diff.seconds)
                            if diff.seconds > delBefore:
                                    ec2.deregister_image(ImageId=amiId)

                                    blockDevices = currImage['BlockDeviceMappings']

                                    for currBlock in blockDevices:
                                            if 'SnapshotId' in currBlock['Ebs']:
                                                    snapId = currBlock['Ebs']['SnapshotId']
                                                    ec2.delete_snapshot(SnapshotId=snapId)
                                    amis_delted+=1
        except Exception as e:
            print(e)
        print(f"AMIs deleted - {amis_delted}")
end_time = time.time()

def get_execution_time():
    time_sec = int(end_time-start_time)
    time_rs = (time_sec)%60
    time_min = time_sec/60
    time_min = int(time_min)
    return f'{time_min} Min {time_rs} Seconds'

with open('/root/scripts/delete_ami.log','a') as file:
    file.write(f'Project - {project_name}\n')
    file.write(f'pwd - {os.getcwd()}\n')
    file.write(f'AMIs deleted - {amis_delted} at {datetime.utcnow()} Time Taken = {get_execution_time()}\n\n')