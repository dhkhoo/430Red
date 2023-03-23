import requests
import sys

session = requests.Session()

username = 0
password = 0
curRequest = 0
ipIndex = 0

ip_addresses = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all')
cur_ip = ip_addresses[ipIndex]

# username from first command line argument, password from second
while(1):
    username = username + 1
    
    # https://www.thepythoncode.com/article/using-proxies-using-requests-in-python
    # https://reqbin.com/code/python/9ooszjzg/python-requests-session-example#:~:text=The%20Requests%20Session%20object%20allows,as%20cookies%20and%20HTTP%20headers.
    # rotate ip address every 1000 requests
    if curRequest == 1000:
        curRequest = 0
        # set requests ip to the next ip in the list
        ipIndex = ipIndex + 1
        if ipIndex == len(ip_addresses):
            ipIndex = 0
        
        cur_ip = ip_addresses[ipIndex]
        session.proxies = {'http': cur_ip, 'https': cur_ip}
        
        
    
    url = 'https://blue/register.php?user=' + username + '&pass=' + password
    
    session.post(url)

    # r = requests.post(url)
    curRequest = curRequest + 1