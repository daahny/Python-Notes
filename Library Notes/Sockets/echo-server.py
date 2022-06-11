# echo-server.py

import socket

ADDR = '127.0.0.1'
PORT = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ADDR, PORT))
    s.listen()
    
    conn, addr = s.accept()
    with conn:
        message = b''
        data = b'non-empty'
        while data:
            data = conn.recv(4096)
            message += data
    print(message)



### Socket Families
# Address format that is required by a socket object is selected based on the address family specified when the socket
# was created.
# AF_INET -- Address family represented as a socket pair (host, port)

### Socket Types
# Define the communication properties visible to a user.
# socket.SOCK_STREAM -- A socket type allowing processes to communicate over TCP. Data is written to the socket as a bytes stream.
# socket.SOCK_DGRAM  -- A socket type allowing processes to communicate over UDP.

### Functions
# socket.socket(family=AF_INET, type=SOCK_STREAM) -- Returns a socket object
# socket.close(file_descriptor)

### Socket Objects
# socket.accept()       -- Accept a connection. The socket must be bound to an address and already listening for connections.
#                           Returns value is a pair (conn, addr) where conn is a new socket object usable to send/receive
#                           and addr is the address bound to the socket on the other end of the connection
# socket.bind(addr)     -- Bind the socket to addr. 
# socket.connect(addr)  -- Connect to a remote socket at addr
# socket.dup()          -- Duplicate the socket
# socket.fileno()       -- Return the socket's file descriptor
# socket.getpeername()  -- Return the remote address to which the socket is connected
# socket.listen()       -- Enable a server to accept connections
# socket.recv(bufsize)  -- Receive data from the socket. The return value is a bytes object representing the data received
#                          Max amount of data to be received at once is specified by bufsize (should be relatively small power of 2 -- like 4096)
# socket.send(bytes)    -- Send data to the socket. The socket must already be connected to a remote socket. 
#                          Apps are responsible for making sure all data is sent.
# socket.sendall(bytes) -- Unlike send(), all data is sent until all data is sent or an error occurs. None is returned on success.

### Bytes Objects
# immutable sequences of single bytes
# b'I am a bytes object as a string'