# Client side of TNT
import json
import socket
import teamLocalTactics
from champlistloader import load_some_champs
from threading import Thread
from rich import print

# sock = socket()
# sock.connect(('localhost', 5550))

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 5550
print('>> Waiting for connection response..')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def recv_welcome():
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))

if __name__== "__main__":
    recv_welcome()

res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Start game: ')
    ClientMultiSocket.sendall(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()

# champions = load_some_champs()
# print(teamLocalTactics.print_available_champs(champions))

# client side fills in the lists
player1 = []
player2 = []
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


