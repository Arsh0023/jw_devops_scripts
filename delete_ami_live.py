import boto3, datetime 
from datetime import date 
from datetime import datetime 
 
 
instance_node = { 
        'prefix': "mrdelivery-live", 
        'InstanceID': "i-04f2476478482b57e", 
        'Region': "ap-south-1", 
        'delBefore': 3 
        } 
 
strOfObjs = [instance_node] 
 
for i in strOfObjs: 
        prefix = i['prefix'] 
        InstanceID = i['InstanceID'] 
        Region = i['Region'] 
        delBefore = i['delBefore'] 
 
        today = date.today() 
        date_format = "%Y/%m/%d" 
        today=today.strftime('%Y/%m/%d') 
        a = datetime.strptime(today, date_format) 
 
        time = datetime.now() 
        name = prefix + time.strftime("-%H.%M-%B%d%-Y") 
        ec2 = boto3.client('ec2', region_name = Region) 
        ec2.create_image(InstanceId=InstanceID, Name=name,NoReboot=True) 
 
        images=ec2.describe_images(Owners=['self']) 
        for currImage in images['Images']: 
                if currImage['Name'].startswith(prefix): 
                        amiId=currImage['ImageId'] 
                        creationDate=currImage['CreationDate'] 
                        creationDate=creationDate[:10] 
                        creationDate=creationDate.replace("-", "/") 
                        b = datetime.strptime(creationDate, date_format) 
                        diff = a-b 
                        if diff.days > delBefore: 
                                ec2.deregister_image(ImageId=amiId) 
 
                                blockDevices = currImage['BlockDeviceMappings'] 
 
                                for currBlock in blockDevices: 
                                        if 'SnapshotId' in currBlock['Ebs']: 
                                                snapId = currBlock['Ebs']['SnapshotId'] 
                                                ec2.delete_snapshot(SnapshotId=snapId)