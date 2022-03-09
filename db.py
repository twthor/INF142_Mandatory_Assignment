from inspect import getcallargs
import pickle
from threading import Thread
import socket
from champlistloader import load_some_champs
from teamLocalTactics import *
import json
from _thread import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table


DatabaseSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5555
ThreadCount = 0
try:
    DatabaseSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print(">> Database is listening.. <<")
DatabaseSideSocket.listen(5)

def addChamps(newChampion: str):
    with open("some_champs.txt", 'a') as f:
        f.write('\n')
        f.write(newChampion)
    return "Champion added!"

def load_champs():
    # data_encoded = connection.recv(4096)
    dictChamps = load_some_champs()
    champs = print_available_champs(dictChamps)
    # return connection.sendall(str.encode(welcome))
    return champs

def multi_threaded_client(connection):
    #connection.send(str.encode('Server is working..'))
    while True:
        # res = connection.recv(4096)
        get_champs = load_champs()
        encode_champs = pickle.dumps(get_champs)
        print("> Sending champs to server.. ")
        connection.sendall(encode_champs)
        connection.close()
        print("> Sent!")
        break
# aswell as store match history to a .txt file

while True:
    # serverSock, address = DatabaseSideSocket.accept()
    # championDict = load_some_champs()
    # serialized_results = json.dumps(championDict)
    # serverSock.send(serialized_results.encode())
    Client, address = DatabaseSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
