import asyncio
import socket
from typing import Optional

from .handler import RequestHandler

class Server:
    def __init__(self, host: Optional[str] = None, port: Optional[int] = 8555) -> None:
        self.host = host if host else socket.gethostname()
        self.port = port

    def start(self):
        asyncio.run(self._prepare_server())

    async def _prepare_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.socket.setblocking(False)

    async def _prepare_server(self):
        await self._prepare_socket()

        loop = asyncio.get_event_loop()

        while True:
            request, _ = await loop.sock_accept(self.socket)
            handler = RequestHandler(request)
            loop.create_task(handler.get_data())