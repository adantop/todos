#!/bin/bash

cd $(dirname "$0"); pwd

nohup python3 ./backend/app.py   > ./backend/app.log   2>&1 &
echo "Backend $(ps -f | grep 'backend/app.py' | grep -v grep | awk '{print $2}')" > ./process.pid

nohup python3 ./webserver/app.py > ./webserver/app.log 2>&1 &
echo "Frontend $(ps -f | grep 'webserver/app.py' | grep -v grep | awk '{print $2}')" >> ./process.pid

cat ./process.pid