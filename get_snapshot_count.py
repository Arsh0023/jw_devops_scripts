import os
import boto3

if __name__ == '__main__':
    
    ec2 = boto3.resource('ec2')
    snapshots = ec2.snapshots.all()
    snapshot_ids = []

    for snap in snapshots:
        snapshot_ids.append(snap.id)

    print(len(snapshot_ids))