import socket
import threading
from datetime import datetime

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port number

# Function to handle client requests
def handle_client(client_socket, addr):
    print(f"Connection from {addr} established.")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        # Check if the client sent the exit command (replace 'ITBIN-2211-xxxx' with your actual index number)
        if data.strip() == "ITBIN-2211-xxxx":
            print(f"Client {addr} sent exit command. Closing connection.")
            client_socket.send("Connection closed.".encode())
            client_socket.close()
            break
        else:
            # Send the current time
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            client_socket.send(current_time.encode())

# Setting up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)  # Allow 5 clients to wait in queue
print("Server is listening...")

while True:
    client_socket, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
