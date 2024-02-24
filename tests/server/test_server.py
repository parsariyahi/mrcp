import socket

from morsep import Server

def test_server_listening():
    server = Server()
    server.start()

    
    host = socket.gethostname()  # as both code is running on same pc
    port = 8555
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send("test")  # send message
    client_socket.close()  # close the connection