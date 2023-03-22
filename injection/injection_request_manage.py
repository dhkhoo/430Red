import requests
import sys

# username from first command line argument, password from second
username = sys.argv[1]
password = sys.argv[2]
action = sys.argv[3]
amount = sys.argv[4]

# log in with existing legitimate account
url = 'https://uscbank5/login.php?user=' + username + '&pass=' + password

r = requests.post(url) #contains cookie

# make request to manage.php
url_manage = 'https://uscbank5/manage.php?action=' + action + '&amount=' + amount

r2 = requests.post(url_manage, cookies=r.cookies)