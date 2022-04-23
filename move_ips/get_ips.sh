#!/bin/bash 
 
cd /etc/nginx/conf.d/yelo_admin && ls -1 | sed 's/.conf//g' > /tmp/admin_urls_new.txt 
domainlist=`cat /tmp/admin_urls_new.txt | awk -F'/' '{print $1}'` 
for cert in `echo $domainlist` 
do 
myIP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4) 
resolveip=$(dig +short $cert | tail -n 1) 
if [[ "$resolveip" == "$myIP" || "$resolveip" == 35.154.18.171 ]] 
   then 
   echo $cert >> /tmp/pointedAdmin.txt 
else 
   echo $cert >> /tmp/unpointedAdmin.txt 
fi 
done