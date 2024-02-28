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
        request = self._prepare_request(data)
        self.socket.send(request.encode("utf-8"))

    def _prepare_request(self, data: str):
        req = ""
        chunk_size = len(data)
        req += f"Chunk-Size = {chunk_size}".ljust(49)
        req += "\n"
        req += data
        return req

    def get_response(self):
        data = self.socket.recv(255)
        print(data)