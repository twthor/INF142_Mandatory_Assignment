from threading import Thread
import socket
from champlistloader import load_some_champs
import json

class ProcessData:
    # class variables
    process_id = 0 
    project_id = 1

    def __init__(self):
        # instance variables
        self.task_id = 2
        self.start_time = 3

DatabaseSideSocket = socket.socket()
host = '127.0.0.1'
port = 5555
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

# aswell as store match history to a .txt file

while True:
    serverSock, address = DatabaseSideSocket.accept()
    championDict = load_some_champs()
    serialized_results = json.dumps(championDict)
    serverSock.send(serialized_results.encode())
    
