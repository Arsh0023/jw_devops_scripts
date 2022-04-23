# #IPs will be there in a text file take that ip ssh into.
# #go to sudo.
# #change the crontab with updated info and then also change the delBefore variable.

# #modules can be used parmiko or fabric.
# import os
# import time
# import paramiko
# from datetime import datetime

# pwd = os.getcwd()
# KEYFILE='/home/arsh/keys/key.pem'
# USER = 'ec-2'
# utc = lambda : datetime.utcnow().time().strftime("%H:%M:%S") #"%Y-%m-%d %H:%M:%S"
# plist = os.listdir(os.getcwd())
# cron_file_data = open(f'{pwd}/run_commands_ip/cron.txt','r').read()
# delete_ami_data = ''
# delete_temp_data = ''

# ssh = paramiko.SSHClient()
# privk = paramiko.RSAKey.from_private_key_file(KEYFILE) # OR k = paramiko.DSSKey.from_private_key_file(keyfilename)
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# #change the crontab.
# #change the scripts.
# commands_to_run = [
#     'sudo su',
#     'rm -rf /var/spool/cron/root',
#     f'echo "{cron_file_data}" >> /var/spool/cron/root'
# ]

# ips = [
#     '3.7.216.216',
# ]

# log_file = open(f'{pwd}/ssh_out.log','a')

# def connect_to_host(ip):
#     log_file.write(f'For Server IP : {ip}\n')
#     HOST=ip
#     try:
#         ssh.connect(hostname=HOST, username=USER, pkey=privk)
#         log_file.write(f'Connection Established to {ip}')
#         for command in commands_to_run:
#             run_command(command)
#     except Exception as e:
#         log_file.write(f'Failed to complete.\nError - {e}')
#         print(e)
#     ssh.close()
#     log_file.write(f'Connection to {ip} closed.\n\n')

# def run_command(command,ip):
#     ssh_stdout = ''
#     ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
#     for line in ssh_stdout:
#         print(line.strip('\n'))
#         print(ssh_stdout)
#         log_file.write(line.strip('\n'))
#         log_file.write('\n')
#         log_file.write(ssh_stdout)
#         log_file.write('\n')

# if __name__ == '__main__':
#     for ip in ips:
#         connect_to_host(ip)
#         ssh = paramiko.SSHClient()
#         privk = paramiko.RSAKey.from_private_key_file(KEYFILE) # OR k = paramiko.DSSKey.from_private_key_file(keyfilename)
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.close()
#     log_file.close()

        
import os
import time
import paramiko
from datetime import datetime

cron_file_data = open(f'/home/arsh/scripts/run_commands_ip/cron.txt','r').read()

commands_to_run = [
    #'whoami',
    #'sudo su',
    #'whoami',
    'sudo rm -rf /var/spool/cron/root',
    'sudo touch /var/spool/cron/root',
    #f'sudo echo "{cron_file_data}" > /var/spool/cron/root',
    f'sudo echo "{cron_file_data}" > /home/ec2-user/root',
    'sudo mv /home/ec2-user/root /var/spool/cron/root',
    #'sudo crontab -l',
    "sudo sed -i 's/10800/259200/g' /root/scripts/delete_ami.py",
    "sudo sed -i 's/10800/259200/g' /root/scripts/delete_temp.py",
    "sudo sed -i 's/diff.seconds/diff.total_seconds()/g' /root/scripts/delete_ami.py",
    "sudo /bin/bash /root/scripts/delete_ami.sh",
    'sudo chown -R root: /var/spool/cron/root',
    'sudo chmod -R 600 /var/spool/cron/root',
]

commands_to_run_specific = [
    # 'sudo chown -R root: /var/spool/cron/root',
    # 'sudo chmod -R 600 /var/spool/cron/root',
]

#All Dev-test Servers
ips = [
    '3.109.223.76',
    '35.154.108.81',
    '65.2.94.213',
    '65.0.63.160',
    '3.110.204.242',
    '13.232.236.60',
    '15.207.21.19',
    '15.206.230.220',
    '3.109.94.0',
    '35.154.150.117',
    '65.1.24.239',
    '13.233.104.98',
    '13.232.66.174',
    '65.2.67.223',
    '13.233.55.1',
    '15.207.135.167',
    '3.109.104.72',
    '3.111.153.93',
    '13.232.11.116',
    '3.109.6.173',
    '13.234.140.30',
    '3.7.216.216',
    '3.108.232.16',
    '65.1.94.222',
    '3.109.75.255',
    '3.109.180.190',
    '15.207.221.46',
    '15.206.211.158',
    '13.126.182.131',
    '15.207.8.84',
    '13.127.208.68',
    '13.235.108.36',
    '13.233.11.119',
    '3.109.2.234',
    '13.233.116.152',
    '65.1.56.156',
    '13.232.97.39',
    '15.206.212.216',
    '3.6.31.188',
    '65.2.134.178',
    '13.232.159.211',
    '3.108.217.149',
    '3.109.136.166',
    '3.111.127.138',
    '15.207.38.207',
    '3.109.238.44',
    '35.154.46.167',
    '3.109.95.192',
    '3.111.145.52',
    '3.109.255.82',
    '3.109.124.93',
    '15.207.98.3',
    '65.1.62.32',
    '3.109.242.148',
    '65.2.95.194',
    '13.235.254.102',
    '65.1.186.174',
    '65.2.164.252',
    '13.126.98.251',
    '65.1.16.243',
    '65.1.24.233',
    '65.1.25.12',
    '35.154.246.215',
    '65.2.61.202',
    '3.6.153.41',
    '3.108.116.176',
    '3.109.233.105',
    '13.127.87.242',
    '65.1.196.188',
    '3.108.24.124',
    '13.235.218.93',
    '15.206.49.132',
    #'13.232.241.200',
    '15.206.151.251',
    '35.154.138.201',
    '3.108.81.55',
    '65.2.77.24',
    '3.108.22.147',
    '65.0.73.207',
    '13.127.195.249',
    '65.1.194.227',
    '15.206.31.224',
    '13.235.85.0',
    '13.234.133.169',
    '13.126.3.15',
    '15.207.189.191',
    '13.126.102.41',
    '3.111.28.254',
    '3.108.39.12',
    '13.235.175.239',
    '3.109.12.85',
    '13.233.143.229',
    '3.108.232.16',
    '65.2.164.187',
    '65.2.164.187',
    '3.109.98.39',
    '3.108.68.162',
    '35.154.150.117',
    '35.154.150.117',
    '65.1.24.233',
    '65.2.94.213',
    '3.7.216.216',
    '15.206.49.132',
]

specific_ips = [
    #'35.154.246.215',
    # '65.2.94.213',
    # '3.108.232.16',
    # '65.2.164.187',
    # '65.2.164.187',
    # '3.109.98.39',
    # '3.108.68.162',
    # '35.154.150.117',
    # '35.154.150.117',
    #'13.234.109.166',
    #'15.206.49.132',
    # '3.111.145.52',
    #'3.111.145.52', #medworks-test
    #'3.109.95.192', #medworks-dev
    # '65.1.24.233',
    # '65.2.94.213',
    # '3.7.216.216',
    # '15.206.49.132',
    '3.109.62.170',
    '65.2.61.202',
    '3.7.189.203',
    '15.207.82.31',
    '3.7.216.216',
    
]

if specific_ips:
    ips_run = specific_ips
else:
    ips_run = ips

if commands_to_run_specific:
    commands_to_run_actual = commands_to_run_specific
else:
    commands_to_run_actual = commands_to_run

USER='ec2-user'
sleep_time = 1
utc = lambda : datetime.utcnow().time().strftime("%H:%M:%S") #"%Y-%m-%d %H:%M:%S"
log_file = open(f'ssh_out_logs/ssh_out_{datetime.today().date()}.log','a')
error_file = open(f'error_ssh_out_{datetime.today().date()}.log','a')
def run_commands(cm):
    ssh_stdout=''
    for c in cm:
        print(c)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(c)
        for line in ssh_stdout:
            print(line.strip('\n'))
        print(ssh_stdout)
    # for line in ssh_stdout:
    #     print(line)

for ip in ips_run:
    try:
        KEYFILE='/home/arsh/keys/key.pem'
        ssh = paramiko.SSHClient()
        privk = paramiko.RSAKey.from_private_key_file(KEYFILE) # OR k = paramiko.DSSKey.from_private_key_file(keyfilename)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=USER, pkey=privk)
        #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
        ssh_stdout=''
        log_file.write(f'Connection to {ip} Established\n')
        for c in commands_to_run_actual:
            print(c)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(c)
            for line in ssh_stdout:
                a = line.strip('\n')
                print(a)
                log_file.write(f'{utc()} - {a}\n')
            #time.sleep(1)
            #print(ssh_stdout)
        log_file.write(f'DONE for {ip}\n\n')
        ssh.close()
    except Exception as e:
        error_file.write(f'Error for {ip}\nError - {e}\n\n')
