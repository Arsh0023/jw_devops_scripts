import os
import sys
import requests

acp_url = "https://chat-api.fuguchat.com/api/webhook?token=d37287ed5fbbc825769e691cb514da99a4f167b0fbea5b58f898fa840f6a7e9a"

if len(sys.argv) > 1:
    cli_msg = sys.argv[1]

if len(sys.argv) > 2:
    BASE_PATH = sys.argv[2]
else:
    BASE_PATH = os.getcwd()

SEPERATE = False #If set true sends each line in text file seperately
SEND_FROM_FILE = False #If set true will send from fugu_message.txt file present in the current directory or the path passed

def send_message(msg='Hi',channel_id=0,bot_url=acp_url):
    url = bot_url
    headers = { 
        'app_version': '111',
        'content-type': 'application/json', 
        'device_type': '1'
    }
    #msg = msg.replace('\"',"\'")
    data = '{"data":{"message":'+ f'"{msg}"' +',"message_type":1}}'
    #print(data)
    response = requests.post(url=url,headers=headers,data=data)
    return response.status_code

if __name__ == '__main__':
    if os.path.exists(os.path.join(BASE_PATH,'fugu_message.txt')) and SEND_FROM_FILE:
        lines = open(os.path.join(BASE_PATH,'fugu_message.txt'),'r').readlines()
        msg = ''
        for line in lines:
            if SEPERATE:
                status = send_message(line.strip())
            else:
                msg += line.strip()+'\\n'

        if not SEPERATE:
            status = send_message(msg)
        
    else:
        status = send_message(cli_msg)

    print(status)


