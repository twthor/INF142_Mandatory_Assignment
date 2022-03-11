# Server side of TNT
import socket
from _thread import *
import pickle
from time import sleep
from threading import Lock
from champlistloader import load_some_champs
import teamNetworkTactics
from core import Champion

# Declraing a lock
lock = Lock()

def get_champs():
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

def load_game():
    welcome = teamNetworkTactics.welcomeMessage()
    return welcome

def load_champions():
    champs = get_champs()
    return champs

def select_champion(user: int, userInput: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected. Appends userinput to list if champion is valid.
    clients[user].send(pickle.dumps(userInput))
    while True:
        client_message = clients[user].recv(4096)
        client_message = pickle.loads(client_message)
        # validate input
        if client_message not in champions:
            message = f'The champion {client_message} is not available. Try again.\n' + userInput
        elif client_message in player1:
            message = f'{client_message} is already in your team. Try again.\n' + userInput
        elif client_message in player2:
            message = f'{client_message} is in the enemy team. Try again.\n' + userInput
        else:
            player1.append(client_message)
            break
        clients[user].send(pickle.dumps(message))

def run_match(player1, player2, conn1, conn2):
    match_results = teamNetworkTactics.match(player1, player2)
    results = pickle.dumps(match_results)
    conn1.sendall(results)
    conn2.sendall(results)
    
    # red score, blue score
    score = teamNetworkTactics.team_score(match_results[3], match_results[4])
    score = pickle.dumps(score)
    conn1.sendall(score)
    conn2.sendall(score)

def multi_threaded_client(conn):
    conn.send(str.encode("Connected"))

    while True:
        if threadCount == 2:
            
            # load the game and send to client
            game_start = pickle.dumps(load_game())
            conn.sendall(game_start)
            champs = load_champions()
            conn.sendall(champs)

            sleep(1)

            # to make shure that thread 1 will enter first
            if conn == clients[1]:
                sleep(1)

            # acquire lock
            lock.acquire()

            champions = load_some_champs()

            # players select their champions
            select_champion(0, '[red] Player 1 > ', champions, player1, player2)
            select_champion(1, '[blue] Player 2 > ', champions, player2, player1)

            lock.release()
            
            # print(player1, len(player1))
            # print(player2, len(player2))
            while True:
                    if len(player1) == 2 and len(player2) == 2:
                        if conn == clients[1]:
                            run_match(player1, player2, clients[0], clients[1]) # conn 1 og conn 2
                    break
            break

def main():
    # create server socket
    serverSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5550
    try:
        serverSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    # only want two people to connect the server
    serverSideSocket.listen(2)
    print(">> Server is listening.. <<")
   
    # Globals
    global threadCount
    global clients
    global player1
    global player2
    threadCount = 0
    clients = []
    player1 = []
    player2 = []
    
    while True:
        conn, addr = serverSideSocket.accept()
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        clients.append(conn)
        start_new_thread(multi_threaded_client, (conn, ))
        threadCount += 1
        print('Thread Number: ' + str(threadCount))

if __name__=="__main__":
    main()