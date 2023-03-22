import requests
import sys

# username from first command line argument, password from second
username = sys.argv[1]
password = sys.argv[2]

url = 'http://blue/register.php?user=' + username + '&pass=' + password

r = requests.post(url)