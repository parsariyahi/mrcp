import socket

class Settings:
    # The chunk size with "\n" is 50,
    # So when we want to send the cunk,
    # We need to send 49 bit,
    # One bit is reserved for "\n".
    CHUNK_SIZE_BIT_SIZE = 50
    
    DEFAULT_PORT = 8555
    DEFAULT_HOST = socket.gethostname()
