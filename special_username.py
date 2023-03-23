import requests
import sys
import random

username = 0
password = 0

# read username from the popular-usernames.csv file
usernames = open('special-usernames.csv', 'r')

for username in usernames:
    # username from first command line argument, password from second
    # set password as random number between 0 and 1000
    password = random.randint(0, 100)
    url = 'https://blue/register.php?user=' + username + '&pass=' + password
    # see if weird passwrod breaks the system

    r = requests.post(url)
