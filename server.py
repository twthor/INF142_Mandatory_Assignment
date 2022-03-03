# Server side of TNT
from socket import socket
import champlistloader
import core
import teamLocalTactics
from threading import Thread

sock = socket()
sock.bind(('localhost', 5550))
sock.listen()
while True:
    connectionSock, _ = sock.accept()
    info = connectionSock.recv(2048).decode()
    up = info.upper()
    connectionSock.sendall(up.encode())
    connectionSock.close()


