from logging import Filter
import boto3
from pprint import pprint
import time

#get the launch template with name

asg_names = [
    'TerrazasDePanama',
    'blaze-test',
    'buenbyahedev-dev',
    'buenbyahetest-test',
    'double-o-coffee-test',
    'elm-consultancy-dev',
    'elm-consultancy-test',
    'foody-dev',
    'foody-test',
    'geeb-dev',
    'geeb-test',
    'ivoryspa-dev',
    'local-beauty-dev',
    'onerail-dev',
    'pandamarket-dev',
    'pandamarket-test',
    'realestateexposure-Test-asg',
    'realestateexposure-dev-asg',
    'renant-dev',
    'renant-test',
    'saudiex-dev',
    'saudiex-test',
    'spbnb-dev',
    'spbnb-test',
    'berhan-dev',
   'berhan-test',
    'isy-healthcare',
    'lido-dev',
    'ocean-eats-dev',
    'propertyservices360-dev-asg',
    'propertyservices360-test-asg',
    'sstires-dev',
    'sstires-test',
    'sukicart-dev',
    'sukicart-test',
]

release_eips = [
    '15.206.45.227',
    '3.108.81.255',
    '13.127.175.250',
    '3.108.25.254',
    '13.126.149.106',
    '65.2.25.36',
    '3.7.14.180',
    '65.2.119.178',
    '65.2.91.95',
    '3.108.47.143',
    '3.108.26.162',
    '15.206.49.240',
    '3.108.76.129',
    '13.234.203.209',
    '13.127.14.59',
    '15.206.192.102',
    '13.234.124.99',
    '3.7.180.173',
    '3.108.48.194',
    '65.2.156.61',
    '65.2.67.180',
    '65.1.165.158',
    '15.207.219.53',
    '13.234.212.71',
    '3.108.29.16',
    '3.108.78.1',
    '3.108.32.51',
   '3.7.178.171',
    '15.207.0.137',
    '65.1.234.144',
    '3.108.38.160',
    '13.127.237.42',
    '52.66.171.98',
    '3.108.16.123',
    '3.108.15.83',
    '3.6.27.98',
]
ec2 = boto3.client('ec2',region_name='ap-south-1')
autoscaling = boto3.client('autoscaling', region_name="ap-south-1")

for asg_name in asg_names:
    #response_asgs = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])

    #Filters=[{'Name':'tag:Name', 'Values':[asg_name]}] (Filetring on name through CLI not yet supported 10/03/2022)
    #pprint(response_asgs)

    #pprint(response_asgs['AutoScalingGroups'][0]['AutoScalingGroupName'])
    #pprint(response_asgs['AutoScalingGroups'][0]['MixedInstancesPolicy']['LaunchTemplate']['LaunchTemplateSpecification']['LaunchTemplateId'])
    
    #lt = response_asgs['AutoScalingGroups'][0]['MixedInstancesPolicy']['LaunchTemplate']['LaunchTemplateSpecification']['LaunchTemplateId']
    #print(lt)
    
    # response_lt = ec2.describe_launch_templates(
    # LaunchTemplateIds=[
    #     lt,
    # ],
    # )

    #pprint(response_lt)

    # autoscaling.set_desired_capacity(
    #     DesiredCapacity=0,
    # )
    try:
        autoscaling.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            MinSize=0,
            MaxSize=0,
            DesiredCapacity=0,
        )
    except Exception as e:
        print(asg_name)
        print(e)

# for eip in release_eips:
#     ec2.release_address(
#         PublicIp=eip,
#         DryRun=True,
#     )