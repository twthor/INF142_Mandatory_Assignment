# Server side of TNT
from importlib.resources import path
from socket import create_server
from zoneinfo import available_timezones
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
import teamLocalTactics
from threading import Thread
import json


sock = create_server(('localhost', 5550)) #reuse_port=True
sock.listen()
print(">> Server is listening.. <<")

champions = load_some_champs()
player1Champs = []
player2Champs = []
def addChamps(champ):
    if (len(player1Champs)==2):
        player2Champs.append(champ)
        print("lagt til i player2 " + champ)
    else:
        player1Champs.append(champ)
        print("lagt til i player1 " + champ)

def startMatch(player1, player2):
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    return match.play()

while True:
    #while user := input("Server>> "):
    connectionSock, address = sock.accept()
    print(">> Server: Connection established from : ", address, "<<")    
    #available_champs = teamLocalTactics.print_available_champs()
    
    #Funker. Sender tilbake alle champs til client.
    for _ in range(4):
        champ = connectionSock.recv(1024).decode()
        addChamps(champ)
        connectionSock.sendall(champ.encode("utf-8"))
        
    # champ = connectionSock.recv(2048).decode()
    # player2Champs.append(champ)
    # connectionSock.send(champ.encode())

    print(player1Champs)
    print(player2Champs)
    
    #Starts the match and stores the returned result in variable.
    results = startMatch(player1Champs, player2Champs)

    # JSON Serializing
    serialized_results = json.dumps(results)
    connectionSock.send(serialized_results.encode())

    connectionSock.close()




