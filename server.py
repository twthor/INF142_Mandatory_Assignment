# Server side of TNT
from importlib.resources import path
from socket import create_server
import champlistloader
import core
import teamLocalTactics
from threading import Thread


sock = create_server(('localhost', 5550)) #reuse_port=True
sock.listen()
path_obj = "C:/Users/tthor/OneDrive - University of Bergen/INF142/INF142_Mandatory_Assignment/server.py"

while True:
    #while user := input("Server>> "):
    connectionSock, _ = sock.accept()
    info = "hei"
    file = open(path_obj, 'rb')
    chunk = file.read(1024)
    connectionSock.sendall(info.encode())
    connectionSock.sendall(chunk)
    connectionSock.close()



