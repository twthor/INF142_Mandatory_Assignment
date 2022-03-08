# Client side of TNT
import json
from socket import socket
import teamLocalTactics
from champlistloader import load_some_champs
from threading import Thread
from rich import print

sock = socket()
sock.connect(('localhost', 5550))

champions = load_some_champs()
print(teamLocalTactics.print_available_champs(champions))

# client side fills in the lists
player1 = []
player2 = []
for _ in range(2):
        teamLocalTactics.input_champion('Player 1', 'red', champions, player1, player2)
        teamLocalTactics.input_champion('Player 2', 'blue', champions, player2, player1)

# Sends champs to server
for champ in player1:
    sock.sendall(champ.encode("utf-8"))
for champ in player2:
    sock.sendall(champ.encode("utf-8"))

# for _ in range(4):
#     while userInput := input("Client>> Choose your champion "):
#         sock.send(userInput.encode())
#         teamLocalTactics.input_champion('Player 1', 'red', champions, player1, player2)

while True:
    # receive response from server confiriming locked in champions:
    response = sock.recv(2048).decode()
    print('From server: ', response)

    #JSON serializing
    receive_results = sock.recv(2048).decode()
    match_results = json.loads(receive_results)
    print(match_results)

    sock.close()

# needs to print the summary of the match in nice format using teamLocalTactics.py
