from typing import Optional
import socket

class Client:
    def __init__(self, host: str, port: Optional[int] = 8555) -> None:
        self.host = host
        self.port = port

        self._prepare_socket()

    def _prepare_socket(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def request(self, data):
        self.socket.send(data)