# Server side of TNT
from importlib.resources import path
from socket import create_server
import socket
from zoneinfo import available_timezones
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
import teamLocalTactics
from threading import Thread
import json
from _thread import *

# You can create a protocol on the serverside that handles the inputs.

# sock = create_server(('localhost', 5550)) #reuse_port=True
# sock.listen()

# Connects to the database:
# db_sock = socket.socket()
# db_sock.connect(('localhost', 5555))
def getChamps():
    db_sock = socket.socket()
    db_sock.connect(('localhost', 5555))
    recv_champions = db_sock.recv(2048).decode()
    #champions = json.loads(recv_champions)
    db_sock.close()
    return recv_champions

ServerSideSocket = socket.socket()
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
    connection.send(str.encode('Server is working..'))
    while True:
        data = connection.recv(2048)
        if not data:
            break

        welcome = teamLocalTactics.welcomeMessage()
        connection.sendall(str.encode(welcome))

        # available_champs = getChamps()
        # champions = json.loads(available_champs)
        # connection.sendall(str.encode(champions))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()

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




