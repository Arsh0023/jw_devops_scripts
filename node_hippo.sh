#!bin/bash

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
npm install -g node@v8.1.3
npm version :- 6.14.5
npm install -g node@v8.1.3
nvm alias default 8.1.3

source env.sh
cd $parent/$dirName
if ["branchName" == "test"]
    then
    NODE_ENV=test pm2 start server.js --name medworks-hippo-backend && pm2 logs medworks-hippo-backend
fi

if ["branchName" == "stage"]
    then
    NODE_ENV=stage pm2 start server.js --name medworks-hippo-backend && pm2 logs medworks-hippo-backend
fi