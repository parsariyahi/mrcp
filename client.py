import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print(f"Connected to {server_address}")


data = "0110.01.010.111.01/010.00.1011.01.1111.11".encode("utf-8")

try:
    # Receive the welcome message from the server
    welcome_message = client_socket.send(data)

finally:
    # Clean up the connection
    client_socket.close()