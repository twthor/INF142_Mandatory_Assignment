# Client side of TNT
# test push
from socket import socket

sock = socket()
sock.connect(('localhost', 5000))

message = ''
sock.sendall(message.encode())
response = sock.recv(2048)
print('From server:', response.decode())