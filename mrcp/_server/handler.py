import asyncio
import socket

from .._translator.decoder import Decoder
from ..settings import Settings

class RequestHandler:
    def __init__(self, request: socket.socket) -> None:
        self.request = request 

    async def handle_request(self):
        loop = asyncio.get_event_loop()
        chunk_size = await self.get_chunk_size()
        data = (await loop.sock_recv(self.request, chunk_size)).decode("utf-8")
        self.request.close()
        print(data)
        d = Decoder()
        decoded_data = d.decode(data)
        print("raw data: ", data, "\ndecoded data: ", decoded_data)
        return 

    async def get_chunk_size(self):
        loop = asyncio.get_event_loop()
        chunk_size_header = (await loop.sock_recv(
                self.request,
                Settings.CHUNK_SIZE_BIT_SIZE)
                ).decode("utf-8")
        # Replace the spaces with nothing
        chunk_size_header = chunk_size_header.replace(" ", "")
        # Split the key, value
        chunk_header = chunk_size_header.split("=")
        return int(chunk_header[1])

    async def old_get_data(self):
        loop = asyncio.get_event_loop()
        data = (await loop.sock_recv(self.request, 50)).decode("utf-8")
        # await loop.sock_sendall(self.request, "I get that thanks".encode("utf-8")) #Just for testing the reponse part of the request.
        self.request.close()

        d = Decoder()
        # decoded_data = d.decode(data)
        # print("raw data: ", data, "\ndecoded data: ", decoded_data)
        print("raw data: ", data)
        return data