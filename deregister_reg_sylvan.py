import sys
import boto3
import os
import time


def main():
	zone = sys.argv[1] #availability_zone_distinction
	asg(zone);

def asg(zone):
	client = boto3.client('autoscaling', region_name="us-east-2")
	resp = client.describe_auto_scaling_instances()
	for o in resp['AutoScalingInstances']:
	    if o['AvailabilityZone'] == zone:
	    	Instance = o['InstanceId']
	elbs(Instance);


def elbs(Instance):
	elbList = boto3.client('elbv2', region_name="us-east-2")
	bals = elbList.describe_load_balancers()
	for elb in bals['LoadBalancers']:
	    print 'ELB Name: ' +  elb['LoadBalancerName'] +  'ELB scheme type: ' + elb['Scheme']


	e_desc = elbList.describe_target_groups()
	for el in e_desc['TargetGroups']:
	    print 'Target Name: ' +  el['TargetGroupName'] + 'ARN: ' + el['TargetGroupArn']
	    if el['TargetGroupName'] == "sylvan-mysylvan": #Hard-Coded-Single-80
	    	tar_ssl_not=el['TargetGroupArn']
	    if el['TargetGroupName'] == "sylvan-mysylvan-ssl": #Hard-Coded-Single-443
	    	tar_ssl=el['TargetGroupArn']

	response = elbList.describe_target_health(
	  TargetGroupArn = tar_ssl_not
	)
	target_id_first = []
	for a in response['TargetHealthDescriptions']:
		if a['Target']['Id'] == Instance:
			target_id_first.append(a['Target'])
	    	
	print('target_id_first:' + str(target_id_first))

	response_sec = elbList.describe_target_health(
	  TargetGroupArn = tar_ssl
	)
	target_id_second = []
	for b in response_sec['TargetHealthDescriptions']:
		if b['Target']['Id'] == Instance:
			target_id_second.append(b['Target'])
	    	
	print('target_id_second:' + str(target_id_second))

	dereg(elbList,target_id_first,tar_ssl_not);
	time.sleep(5) 
	dereg_sec(elbList,target_id_second,tar_ssl);
	time.sleep(360)
	success(Instance);

def dereg(elbList,target_id_first,tar_ssl_not):
	fall = elbList.deregister_targets(
	  TargetGroupArn = tar_ssl_not,
	  Targets = target_id_first,
	)
	print (fall)
	
def dereg_sec(elbList,target_id_second,tar_ssl):
	fall_sec = elbList.deregister_targets(
	  TargetGroupArn = tar_ssl,
	  Targets = target_id_second,
	)
	print (fall_sec)

def success(Instance):
	elbList = boto3.client('elbv2', region_name="us-east-2")
	el_suc = elbList.describe_target_groups()
	for el in el_suc['TargetGroups']:
	    print 'Target Name: ' +  el['TargetGroupName'] + 'ARN: ' + el['TargetGroupArn']
	    if el['TargetGroupName'] == "sylvan-mysylvan": #Hard-Coded-Single-80
	    	tar_ssl_not_lb=el['TargetGroupArn']
	    if el['TargetGroupName'] == "sylvan-mysylvan-ssl": #Hard-Coded-Single-443
	    	tar_ssl_lb=el['TargetGroupArn']

	response_lb = elbList.describe_target_health(
	  TargetGroupArn = tar_ssl_not_lb
	)
	target_id_first_lb = []
	for c in response_lb['TargetHealthDescriptions']:
		if c['Target']['Id'] == Instance:
			target_id_first_lb.append(c['Target'])
	    	
	print('target_id_first_lb:' + str(target_id_first_lb))

	response_sec_lb = elbList.describe_target_health(
	  TargetGroupArn = tar_ssl_lb
	)
	target_id_second_lb = []
	for d in response_sec_lb['TargetHealthDescriptions']:
		if d['Target']['Id'] == Instance:
			target_id_second_lb.append(d['Target'])
	    	
	print('target_id_second_lb:' + str(target_id_second_lb))

	if not target_id_first_lb and not target_id_second_lb:
			print('\n')
			print(''' 
	    .d8888. db    db  .o88b.  .o88b. d88888b .d8888. .d8888. d88888b db    db db     
	    88'  YP 88    88 d8P  Y8 d8P  Y8 88'     88'  YP 88'  YP 88'     88    88 88     
	    `8bo.   88    88 8P      8P      88ooooo `8bo.   `8bo.   88ooo   88    88 88     
	      `Y8b. 88    88 8b      8b      88~~~~~   `Y8b.   `Y8b. 88~~~   88    88 88     
	    db   8D 88b  d88 Y8b  d8 Y8b  d8 88.     db   8D db   8D 88      88b  d88 88booo.
	    `8888Y' ~Y8888P'  `Y88P'  `Y88P' Y88888P `8888Y' `8888Y' YP      ~Y8888P' Y88888P
	      ''')   
   	else:
    		print('\n')
	    	print(''' 
	    d88888b  .d8b.  d888888b db      d88888b d8888b. 
	    88'     d8' `8b   `88'   88      88'     88  `8D 
	    88ooo   88ooo88    88    88      88ooooo 88   88 
	    88~~~   88~~~88    88    88      88~~~~~ 88   88 
	    88      88   88   .88.   88booo. 88.     88  .8D 
	    YP      YP   YP Y888888P Y88888P Y88888P Y8888D' 
	      ''')


main();