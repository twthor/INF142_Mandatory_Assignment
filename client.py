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

# Gammel socket
# sock = socket()
# sock.connect(('localhost', 5550))

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
def choose_champions():
    champions = load_some_champs()
    player1 = []
    player2 = []

    # player 1
    while True:
        player1Choice = Prompt.ask('[red]Player 1')
        sendChoice = pickle.dumps(player1Choice)
        ClientMultiSocket.send(sendChoice)
        # player 2
        while True:
            player2Choice = Prompt.ask('[blue]Player 2')
            ClientMultiSocket.send(sendChoice)
            sendChoice = pickle.dumps(player2Choice)
            # player 1
            while True:
                player1Choice = Prompt.ask('[red]Player 1')
                sendChoice = pickle.dumps(player1Choice)
                ClientMultiSocket.send(sendChoice)
                # player 2
                while True:
                    player2Choice = Prompt.ask('[blue]Player 2')
                    sendChoice = pickle.dumps(player2Choice)
                    ClientMultiSocket.send(sendChoice)
                    break
                break
            break
        break

# When starting the game, client receives the welcome message and champion list.
for _ in range(2):
    res = ClientMultiSocket.recv(4096)
    decoded = pickle.loads(res)
    print(decoded)

# Loop for interacting with the server after received the first to packets^
while True:
    # Input = input('Player 1: ')
    # ClientMultiSocket.sendall(str.encode(Input))
    # choose_champ("Player 1", "red")
    res = ClientMultiSocket.recv(1024)
    # choose_champ("Player 2", "blue")
    if not res:
        break
    # print(res.decode('utf-8'))
    # if (type(res) == bytes):
    decoded = pickle.loads(res)
    print(decoded)
ClientMultiSocket.close()

#######=============== ALT UNDER HER ER DET GAMLE =========================== ###
# champions = load_some_champs()
# print(teamLocalTactics.print_available_champs(champions))

# client side fills in the lists
# player1 = []
# player2 = []
# for _ in range(2):
#         teamLocalTactics.input_champion('Player 1', 'red', champions, player1, player2)
#         teamLocalTactics.input_champion('Player 2', 'blue', champions, player2, player1)

# Sends champs to server
# for champ in player1:
#     champ +="\n"
#     sock.sendall(champ.encode("utf-8"))
# for champ in player2:
#     champ +="\n"
#     sock.sendall(champ.encode("utf-8"))

# while True:
#     # receive response from server confiriming locked in champions:
#     response = sock.recv(2048).decode()
#     print(response)

#     #JSON serializing
#     receive_results = sock.recv(2048).decode()
#     match_results = json.loads(receive_results)
#     print(match_results)

#     sock.close()


