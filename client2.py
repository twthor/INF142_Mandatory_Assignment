# Client side of TNT
import json
import pickle
import socket
import teamLocalTactics
from champlistloader import load_some_champs
from threading import Thread
from rich import print
from rich.prompt import Prompt
from rich.table import Table


ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5550
print('>> Waiting for connection response..')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def choose_champ(prompt: str, color: str):
    Prompt.ask(f'[{color}]{prompt}')

# Champion selection
# def choose_champions():
#     # player 1
#     while True:
#         # player1Choice = Prompt.ask('[red]Player 1')
#         sendChoice = pickle.dumps(player1Choice)
#         ClientMultiSocket.send(sendChoice)
#         # player 2
#         while True:
#             # player2Choice = Prompt.ask('[blue]Player 1')
#             sendChoice = pickle.dumps(player2Choice)
#             ClientMultiSocket.send(sendChoice)
#             break
#         break

# When starting the game, client receives the welcome message and champion list.
for _ in range(2):
    res = ClientMultiSocket.recv(4096)
    decoded = pickle.loads(res)
    print(decoded)

# Loop for interacting with the server after received the first to packets^
while True:
    res = ClientMultiSocket.recv(4096)
    if not res:
        break
    decoded = pickle.loads(res)
    print(decoded)
    choice = input()
    choice = pickle.dumps(choice)
    ClientMultiSocket.send(choice)
    if type(decoded) == list:
        for table in decoded:
            print(table)

ClientMultiSocket.close()