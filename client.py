# Client side of TNT
import socket
import pickle
from rich import print

from champlistloader import load_some_champs
#from rich.table import Table

def main():
    # initiate client socket and connect to server
    clientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5550
    print('>> Waiting for connection response..')
    try:
        clientMultiSocket.connect((host, port))
        print(clientMultiSocket.recv(4096).decode())
    except socket.error as e:
        print(str(e))

    # at the beginning of the game the client will receive a welcome message and a list over the champions
    for _ in range(2):
        message = clientMultiSocket.recv(4096)
        print(pickle.loads(message))

    # interact with the server 
    while True:
        message_in = clientMultiSocket.recv(4096)
        if not message_in:
            break
        print(pickle.loads(message_in), end='')
        # If message received in client is a table or not.
        if type(pickle.loads(message_in)) == list:
            for table in pickle.loads(message_in)[:3]:
                print(table, end='')
            listFormat = pickle.loads(message_in)
            print(f"Red score {listFormat[3]}\nBlue score {listFormat[4]}")
            print(listFormat[5])
        champ_choice = input()
        message_out = pickle.dumps(champ_choice)
        clientMultiSocket.sendall(message_out)

    clientMultiSocket.close()

        #if type(decoded) == list:
        #    for table in decoded:
        #        print(table)

if __name__=="__main__":
    main()