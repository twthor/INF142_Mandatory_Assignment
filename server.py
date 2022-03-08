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

champions = load_some_champs()

while True:
    #while user := input("Server>> "):
    connectionSock, _ = sock.accept()
    #available_champs = teamLocalTactics.print_available_champs()
    #welcomeMessage = teamLocalTactics.welcome()
    #connectionSock.sendall(welcomeMessage.encode())
    player1Champs = []
    player2Champs = []
    for _ in range(2): 
        champ = connectionSock.recv(2048).decode()
        player1Champs.append(champ)
        connectionSock.send(champ.encode())

    for _ in range(2): 
        champ = connectionSock.recv(2048).decode()
        player2Champs.append(champ)
        connectionSock.send(champ.encode())
    
    #connectionSock.send("Champs received".encode())
    print(player1Champs)

    match = Match(
        Team([champions[name] for name in player1Champs]),
        Team([champions[name] for name in player2Champs])
    )
    match.play()
    # summary of the match
    teamLocalTactics.print_match_summary(match)

    connectionSock.close()



