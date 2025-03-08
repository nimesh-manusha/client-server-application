import socket

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port number

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Enter 'time' to get current time or type your index number to exit: ")
    client.send(message.encode())

    # Receive response
    response = client.recv(1024).decode()
    print("Server:", response)

    # Exit loop if server closed connection
    if response == "Connection closed.":
        break

client.close()
