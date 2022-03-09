# Server side of TNT
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

# You can create a protocol on the serverside that handles the inputs.

# ======== GAMMEL SOCKET ========
# sock = create_server(('localhost', 5550)) #reuse_port=True
# sock.listen()

# Connects to the database:
# db_sock = socket.socket()
# db_sock.connect(('localhost', 5555))
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
        print(">> Server has received!")
        return champs_encoded

ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5550
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print(">> Server is listening.. <<")
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    #connection.send(str.encode('Server is working..'))
    game_start = pickle.dumps(load_game())
    connection.sendall(game_start)
    send_champs = load_champions()
    connection.sendall(send_champs)

    while True:
        # Funker ikke. Funksjonen spør om input i server terminalen
        # func_champs = pickle.dumps(teamLocalTactics.choose_champions())
        # connection.sendall(func_champs)
        # Pick champ:
        for _ in range(4):
            userInput = connection.recv(4096)
            chose_champs(userInput, "red", player1, player2)
            chose_champs(userInput, "red", player2, player1)
            
        data_encoded = connection.recv(4096)
        wanted_champ = data_encoded.decode(encoding="utf-8")
        chose_champs(wanted_champ)
        if not data_encoded:
            break
        if wanted_champ in load_some_champs():
            print("Checking if valid champions")
            teamLocalTactics.choose_champions(wanted_champ)

    connection.close()

def load_game():
    # Så lenge de ikke receiver en connection, så vil koden kjøre.
    # data_encoded = connection.recv(4096)
    welcome = teamLocalTactics.welcomeMessage()
    # return connection.sendall(str.encode(welcome))
    return welcome

def load_champions():
    champs = getChamps()
    return champs

player1 = []
player2 = []

def chose_champs(userInput, color, player1, player2):
    teamLocalTactics.input_champion(userInput, color, load_some_champs(), player1, player2)

# def validChamp(userInput):

# funket ikke å sende en prompt. Dukket opp på server side.
def askForInput():
    input = Prompt.ask(f"[red]Player 1")
    userInput = pickle.dumps(input)
    return userInput

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()



#######=============== ALT UNDER HER ER DET GAMLE =========================== ###
# champions = load_some_champs()
# player1Champs = []
# player2Champs = []
# def addChamps(champ):
#     separatedName = ""
#     for letter in champ:
#         if letter == "\n":
#             if (len(player1Champs)==2):
#                 separatedName.rstrip()
#                 player2Champs.append(separatedName)
#                 print("lagt til i player2 " + separatedName)
#             else:
#                 separatedName.rstrip()
#                 player1Champs.append(separatedName)
#                 print("lagt til i player1 " + separatedName)
#             # Makes it empty for new champion name
#             separatedName = ""
#         else:
#             separatedName += letter

# def startMatch(player1, player2):
#     match = Match(
#         Team([champions[name] for name in player1]),
#         Team([champions[name] for name in player2])
#     )
#     return match.play()

# while True:
#     #while user := input("Server>> "):
#     connectionSock, address = sock.accept()
#     print(">> Server: Connection established from : ", address, "<<")    
#     #available_champs = teamLocalTactics.print_available_champs()
    
#     #Funker. Sender tilbake alle champs til client.
#     for _ in range(4):
#         champ = connectionSock.recv(2048).decode()
#         if not champ:
#             break
#         addChamps(champ)
#         connectionSock.sendall("Champions locked in!".encode("utf-8"))

#     print(player1Champs)
#     print(player2Champs)
    
#     #Starts the match and stores the returned result in variable.
#     results = startMatch(player1Champs, player2Champs)

#     # JSON Serializing
#     serialized_results = json.dumps(results)
#     connectionSock.send(serialized_results.encode())

#     connectionSock.close()




