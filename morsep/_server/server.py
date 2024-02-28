import asyncio
import socket
from typing import Optional

from .handler import RequestHandler

class Server:
    def __init__(self, host: Optional[str] = None, port: Optional[int] = 8555) -> None:
        self.host = host if host else socket.gethostname()
        self.port = port

    def start(self):
        loop = asyncio.get_event_loop()
        self._prepare_socket()
        loop.create_task(self.listen())
        loop.run_forever()
        
    async def _main(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self._prepare_server())

    def _prepare_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        self.socket.setblocking(False)

    async def listen(self):
        print("running listen server \n")
        loop = asyncio.get_event_loop()

        while True:
            request, _ = await loop.sock_accept(self.socket)
            handler = RequestHandler(request)
            loop.create_task(handler.get_data())

    async def get_all_tasks(self):
        print("get all task running \n")
        for task in asyncio.all_tasks():
            print(task.print_stack())