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
        d = Decoder()
        decoded_data = d.decode(data)
        print("raw data: ", data, "\ndecoded data: ", decoded_data)
        return 

    async def get_chunk_size(self):
        loop = asyncio.get_event_loop()
        chunk_size_header = (await loop.sock_recv(
                self.request,
                Settings.CHUNK_BIT_SIZE)
                ).decode("utf-8")
        # Replace the spaces with nothing
        chunk_size_header = chunk_size_header.replace(" ", "")
        # Split the key, value
        chunk_header = chunk_size_header.split("=")
        return int(chunk_header[1])