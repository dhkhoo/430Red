import requests
import sys

username = 0
password = 0

# username from first command line argument, password from second
while(1):
    username = username + 1
    
    url = 'https://blue/register.php?user=' + username + '&pass=' + password

    r = requests.post(url)