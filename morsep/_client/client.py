from typing import Optional
import socket

from .._translator.encoder import Encoder

class Client:
    def __init__(self, host: str, port: Optional[int] = 8555) -> None:
        self.host = host
        self.port = port

        self._prepare_socket()

    def _prepare_socket(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def request(self, data: str):
        e = Encoder()
        data = e.encode(data)
        self.socket.send(data.encode("utf-8"))

    def get_response(self):
        data = self.socket.recv(255)
        print(data)