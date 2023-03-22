import requests
import sys

# username from first command line argument, password from second
username = sys.argv[1]
password = sys.argv[2]

url = 'https://USC-Bank2/register.php?user=' + username + '&pass=' + password

r = requests.post(url)