# Server side of TNT
from socket import create_server
from zoneinfo import available_timezones
import champlistloader
import core
import teamLocalTactics
from threading import Thread


sock = create_server(('localhost', 5550)) #reuse_port=True
sock.listen()

while True:
    #while user := input("Server>> "):
    connectionSock, _ = sock.accept().decode()
    #available_champs = teamLocalTactics.print_available_champs()
    welcomeMessage = teamLocalTactics.welcomeMessage()
    connectionSock.sendall(welcomeMessage.encode())
    #champs = teamLocalTactics.return_available_champs()
    #print(champs)
    #connectionSock.send(champs)
    connectionSock.close()



