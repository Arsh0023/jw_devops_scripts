from email import message
import requests


## Getting the Value ##
# import subprocess
# #value = subprocess.check_output('`tail -n 100000 /var/log/nginx/access.log | grep "$now" | grep -v "socket.io" | awk "{print $1}" | sort | uniq -c | sort -nr | head -n 10`', shell=True)
# value = subprocess.check_output('tail -n 100000 /home/arsh/Downloads/access.log | grep "30/Mar/2022:10:58:57" | grep -v "socket.io" | awk "{print $1}" | sort | uniq -c | sort -nr | head -n 10', shell=True)


# print(value)

def send_fugu(message_data):
    
    url = 'https://chat-api.fuguchat.com/api/webhook?token=f62770e89eb334535fd9c221f737689c6fbc76f7bc2a2cb2a30f55d5e05c8279'

    #data = {"message":"Hello","message_type":1}
    headers = {'app_secret_key':'e228a57c0f3226d88a67eb93e2eee103', 
        'app_version': '111',
        'content-type': 'application/json', 
        'device_type': '1'
    }
# message_data='30/Mar/2022:10:14 \\n204 15.207.17.109 \\n183 119.73.104.90 \\n106 119.157.71.112 \\n105 157.37.170.94'

    data = '{ "en_user_id":"de9533e5edb13e4030e23eafc861b6ac","channel_id": 2344630,"data":{"message":'
    #data = '{ "en_user_id":"de9533e5edb13e4030e23eafc861b6ac","channel_id": 2344630,"data":{"message":"Hello","message_type":1}}'


    #"message_type":1}}
    data+=f'"{message_data}"'
    data+=',"message_type":1}}'

    #print(data)

    response = requests.post(url=url,data=data,headers=headers)
    #print(response.status_code)
    return response.status_code

file_path='/home/arsh/Downloads/apihits.txt'
file_nginx = open(file_path,'r')
file_lines = file_nginx.readlines()

final=''

try:
    for line in file_lines[-60:]:
        #print(line)
        final+=f'{line.strip()} \\n'
except Exception as e:
    print(e)

#print(final)
send_fugu(final)