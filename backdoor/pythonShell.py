import socket
import sys

# Define the server address and port
PORT = int(sys.argv[1])
server_address = ('1.1.1.5', PORT)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server address and port
sock.connect(server_address)

# Loop to get user commands
while True:
    # Get user input
    command = input('Enter a command: ')

    # Check if the user wants to quit
    if command.lower() == 'quit':
        break

    # Send the command to the server
    sock.sendall(command.encode())

    # Receive the response from the server
    response = sock.recv(1024)
    print(response.decode())

# Close the socket
sock.close()