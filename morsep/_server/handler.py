import asyncio
import socket


class RequestHandler:
    def __init__(self, request: socket.socket) -> None:
        self.request = request 

    async def get_data(self):
        loop = asyncio.get_event_loop()
        data = (await loop.sock_recv(self.request, 255)).decode("utf-8")
        self.request.close()
        print(data)
        return data