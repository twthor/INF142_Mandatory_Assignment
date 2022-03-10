# Server side of TNT
from concurrent.futures import thread
from multiprocessing import connection
import pickle
from socket import create_server
import socket
from zoneinfo import available_timezones
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
import teamLocalTactics
from threading import Thread
from _thread import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
import sys
# You can create a protocol on the serverside that handles the inputs.

def getChamps():
    db_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5555
    try:
        db_sock.connect((host, port))
    except socket.error as e:
        print(str(e))
    print('>> Trying to fetch champions..')
    while True:
        champs_encoded = db_sock.recv(4096)
        if not champs_encoded:
            break
        db_sock.close()
        print(">> Server has received champions!")
        return champs_encoded



def multi_threaded_client():
    #connection.send(str.encode('Server is working..'))
    
    # while True:
    if ThreadCount == 2:
        for c in clients:
            game_start = pickle.dumps(load_game())
            c.sendall(game_start)
            send_champs = load_champions()
            c.sendall(send_champs)
        # Server receiving picked champions:
        # while true
        clients[0].sendall("[red] Player 1")
        choice = pickle.loads(clients[0].recv(4096))

        clients[1].sendall("[blue] Player 2")
        choice = pickle.loads(clients[1].recv(4096))

        clients[0].sendall("[red] Player 1")
        choice = pickle.loads(clients[0].recv(4096))

        clients[1].sendall("[blue] Player 2")
        choice = pickle.loads(clients[1].recv(4096))
        


        for _ in range(2):
            for i in range(2):
                list = ["red", "blue"]
                # for c in clients:
                askInput = f"{list[i]} Player {i+1}"
                clients[i].send(pickle.dumps(askInput))
                userInput = pickle.loads(clients[i].recv(4096))
                chose_champs(userInput, clients[i])
        print("player1 ", player1)
        print("player2 ", player2)
        run_match(player1, player2)
    # connection.close()

def load_game():
    welcome = teamLocalTactics.welcomeMessage()
    return welcome

def load_champions():
    champs = getChamps()
    return champs

player1 = []
player2 = []

def chose_champs(userInput, connection):
    if clients[0] == connection:
        # fiks valid champ
        # teamLocalTactics.valid_champion(userInput, load_some_champs(), player1, player2)
        player1.append(userInput)
    elif clients[1] == connection:
        # teamLocalTactics.valid_champion(userInput, load_some_champs(), player2, player1)
        player2.append(userInput)

def valid_champion(userInput: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected. Returns userinput if champion is valid.
    while True:
        if userInput not in champions:
             (f'The champion {userInput} is not available. Try again.')
        if userInput in player1:
            return (f'{userInput} is already in your team. Try again.')
        if userInput in player2:
            return(f'{userInput} is in the enemy team. Try again.')
        else:
            return userInput

def run_match(player1, player2, connection):
    match_results = teamLocalTactics.match(player1, player2)
    # match_results = pickle.dumps(match_results)
    for result in match_results:
        result = pickle.dumps(result)
        # connection.send(result)
    # lastTable = pickle.dumps(match_results[:-1])
    # connection.send(lastTable)
    # return match_results


def main():
    # Creates socket
    ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5550
    global ThreadCount
    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(">> Server is listening.. <<")
    ServerSideSocket.listen()
    global clients
    clients = []

    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        ThreadCount += 1
        start_new_thread(multi_threaded_client, (Client, ))
        clients.append(Client)
        print(clients)
        #if (ThreadCount == 2):
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__=="__main__":
    main()