#!/bin/bash

cd $(dirname "$0")

while read line; do
    name=${line%% *}
    pid=${line##* }
    echo "Stopping: ${name} pid: ${pid}"
    kill $pid
done < ./process.pid