import pickle
import socket
from champlistloader import load_some_champs
from teamNetworkTactics import *
from _thread import *
from rich import print

# Socket information
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

# Extra task for assignment, not finished.
def addChamps(newChampion: str):
    with open("some_champs.txt", 'a') as f:
        f.write('\n')
        f.write(newChampion)
    return "Champion added!"

def load_champs():
    dictChamps = load_some_champs()
    champs = print_available_champs(dictChamps)
    return champs

def multi_threaded_client(connection):
    while True:
        get_champs = load_champs()
        encode_champs = pickle.dumps(get_champs)
        print("> Sending champs to server.. ")
        connection.sendall(encode_champs)
        connection.close()
        print("> Sent!")
        break

while True:
    Client, address = DatabaseSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))