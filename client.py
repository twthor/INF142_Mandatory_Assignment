# Client side of TNT
from socket import socket
import teamLocalTactics
from threading import Thread
from rich import print

sock = socket()
sock.connect(('localhost', 5550))

#while True:
message = sock.recv(2048).decode()
print(message)
#message = sock.recv(2048).decode()
#print(message)
# sock.sendall(message.encode())
# response = sock.recv(2048).decode()
# print('From server:', response)
sock.close()

# pic = open(, 'rb')
# chunk = pic.read(1024)

# Mottar første bits
# l = sc.recv(1024)
# while (l):
#   f.write(l) 
#   l = sc.recv(1024) tar i mot neste bits.
# 