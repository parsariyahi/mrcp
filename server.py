import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {server_address}")

# Wait for a connection
connection, client_address = server_socket.accept()
print(f"Connection established from {client_address}")

try:
    # Receive data from the client
    data = connection.recv(1024)
    print(f"Received data: {data.decode()}")

finally:
    # Clean up the connection
    connection.close()
    server_socket.close()