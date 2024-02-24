from typing import Optional
import socket

class Server:
    def __init__(self, host: Optional[str] = None, port: Optional[int] = 8555) -> None:
        self.host = host if host else socket.gethostname()
        self.port = port
        self._prepare_socket()

    def start(self):
        self.socket.listen()
        conn, addr = self.socket.accept()

        while True:
            data = conn.recv(1024).decode("utf-8")
            print(data)
            if not data:
                break
        
        conn.close()

    def _prepare_socket(self):
        self.socket = socket.socket()
        self.socket.bind((self.host, self.port))