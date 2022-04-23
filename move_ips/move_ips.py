import os

os.chdir('/home/arsh/scripts/move_ips/')
unpointed_ips = open('unpointedAdmin.txt','r')

# move_to_folder = '/etc/nginx/conf.d/yelo_admin_backup'
move_to_folder = 'yelo_backup'

log_file_path = ''

log_file = open(log_file_path)

def create_folder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)
create_folder(move_to_folder)

ips_to_move = unpointed_ips.readlines()
for ip in ips_to_move:
    ip = ip.strip()
    ip+='.conf'
    status = os.system(f'mv {ip} {move_to_folder}/') 

    if status > 0:
        log_file.write(f'failed for {ip}')

log_file.close()