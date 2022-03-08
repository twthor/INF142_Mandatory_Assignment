# Client side of TNT
from json import load
from socket import socket
import teamLocalTactics
from champlistloader import load_some_champs
from threading import Thread
from rich import print

sock = socket()
sock.connect(('localhost', 5550))

champions = load_some_champs()
print(teamLocalTactics.print_available_champs(champions))

# client side fills in the lists
player1 = []
player2 = []
for _ in range(2):
        teamLocalTactics.input_champion('Player 1', 'red', champions, player1, player2)
        teamLocalTactics.input_champion('Player 2', 'blue', champions, player2, player1)

# Sends champs to server
for champ in player1:
    sock.sendall(champ.encode())
for champ in player2:
    sock.sendall(champ.encode())

while True:
    #message = sock.recv(2048).decode()
    #print(message)
    #sock.sendall(message.encode())
    for _ in range(4):
        response = sock.recv(2048).decode()
        print('From server:', response)
    sock.close()

# pic = open(, 'rb')
# chunk = pic.read(1024)

# Mottar første bits
# l = sc.recv(1024)
# while (l):
#   f.write(l) 
#   l = sc.recv(1024) tar i mot neste bits.
# 