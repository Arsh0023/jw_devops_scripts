import os
import subprocess
from pprint import pprint
import datetime as dt

TRIGGER = 90 #Disk Usage Percentage for which the script should take action
log_path = '/home/arsh/tookan_test_logs'
log_files = os.listdir(log_path)

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
       
    return result

if __name__ == '__main__':
    disks = get_disks()
    req = False
    for d in disks:
        pprint(d)
        if d['Filesystem'] == '/dev/mapper/vg_app-lv_app' and int(d['Use%']) >= 90 :
            req = True
            break
    
    if req:
        for f in log_files:
            date = f[-10:]
            date = dt.datetime.strptime(date,'%d-%m-%Y').date()
            today = dt.date.today()

            if date < today:
                os.system(f'echo "hi man" > {log_path}/{f}')
        