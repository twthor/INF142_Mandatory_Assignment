# Server side of TNT
from socket import create_server
import champlistloader
import core
import teamLocalTactics
from threading import Thread


sock = create_server(('localhost', 5550)) #reuse_port=True
sock.listen()

while True:
    #while user := input("Server>> "):
    connectionSock, _ = sock.accept()
    info = "hei"
    connectionSock.sendall(info.encode())
    connectionSock.close()



