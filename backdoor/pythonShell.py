import socket
import sys

# Define the server address and port
PORT = int(sys.argv[1])
server_address = ('1.1.1.5', PORT)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

# Connect the socket to the server address and port
try:
    sock.connect(server_address)
except ConnectionRefusedError:
    print("Could not connect to the server")
    sock.close()
    exit()

# Loop to get user commands
while True:
    # Get user input
    command = input('Enter a command: ')

    # Check if the user wants to quit
    if command.lower() == 'quit':
        break

    # Send the command to the server
    sock.sendall(command.encode())

    # Receive the response from the server in a loop
    while True:
        try:
            response = sock.recv(1024).decode()
            if not response:
                break
            print(response.strip())
        except socket.timeout:
            break

# Close the socket
sock.close()