# echo-client.py

import socket

ADDR = '127.0.0.1'
PORT = 65000

message = (b'A' * 4096) + b'X'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ADDR, PORT))
    s.sendall(message)