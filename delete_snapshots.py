import time
import boto3
import datetime as dt

def get_all_snapshots():
    ec2_resource = boto3.resource('ec2')
    snapshots = ec2_resource.snapshots.all()
    count=0
    with open('snapshots_data.txt','a') as file:
        for snapshot in snapshots:
            file.write(snapshot.id)
            file.write('\n')
            count+=1
        file.write(f'Count is {count}')
    print(count)

if __name__=='__main__':
    get_all_snapshots()
    ec2 = boto3.resource('ec2')
    
    with open('snapshots_data.txt','r') as file:
        snapshots = file.readlines()

    #snapshots = ['snap-015352b97c501b057\n','snap-05326eba031600244\n']
    
    count = 0
    flag = 0
    for s_id in snapshots:
        try:
            s_id = s_id.strip('\n')
            snapshot = ec2.Snapshot(s_id)
            snapshot.delete()
            count +=1
            time.sleep(0.25)
         
        except Exception as e:
            with open(f'delete_snapshots_logs_{dt.date.today()}','a') as file:
                file.write(f'Snapshots Successfully deleted = {count}\n')
                file.write(f'Error Occured\n{e}\n')
            flag = 1

    if not flag:
        with open(f'delete_snapshots_logs_{dt.date.today()}','a') as file:
            file.write(f'Snapshots Successfully deleted = {count}\n')