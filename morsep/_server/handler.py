import asyncio
import socket

from .._translator.decoder import Decoder

class RequestHandler:
    def __init__(self, request: socket.socket) -> None:
        self.request = request 

    async def get_data(self):
        loop = asyncio.get_event_loop()
        data = (await loop.sock_recv(self.request, 255)).decode("utf-8")
        await loop.sock_sendall(self.request, "I get that thanks".encode("utf-8")) #Just for testing the reponse part of the request.
        self.request.close()

        d = Decoder()
        decoded_data = d.decode(data)
        print("raw data: ", data, "\ndecoded data: ", decoded_data)
        return data