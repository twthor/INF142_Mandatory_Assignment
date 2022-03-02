# Client side of TNT
# test push
from socket import socket

sock = socket()
sock.connect(('localhost', 5555))

message = input('Lowercase: ')
sock.sendall(message.encode())
response = sock.recv(2048).decode()
print('From server:', response)
sock.close()
# 2nd test