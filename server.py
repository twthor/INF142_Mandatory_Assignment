# Server side of TNT
import socket
from _thread import *
import pickle
from time import sleep
from threading import Lock
from unittest import TestProgram
import teamLocalTactics
from core import Champion

# Declraing a lock
lock = Lock()
# threadCount = 0
testPlayer1 = []
testPlayer2 = []


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
    welcome = teamLocalTactics.welcomeMessage()
    return welcome

def load_champions():
    champs = get_champs()
    return champs

def run_match(player1, player2, conn):
    match_results = teamLocalTactics.match(player1, player2)
    # match_results = pickle.dumps(match_results)
    results = pickle.dumps(match_results)
    conn.sendall(results)
    
    print("test score server side", match_results[3:5])

    # red score, blue score
    score = teamLocalTactics.team_score(match_results[3], match_results[4])
    print("string server side ", score)
    score = pickle.dumps(score)
    conn.sendall(score)

def input_champion(player, color, champions, player1, player2):
    pass
        

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

            # player 1
            #if conn == clients[0]:
            player = f"[red] Player 1 > "
            message = pickle.dumps(player)
            clients[0].send(message)
            client_message = clients[0].recv(4096)
            print(pickle.loads(client_message))

                #player1 = f"[red] Player 1 chose: {pickle.loads(client_message)}"
                #clients[1].send(pickle.dumps(player1))

            # player 2
            #if conn == clients[1]:
            player = f"[blue] Player {2} > "
            message = pickle.dumps(player)
            clients[1].send(message)
            client_message = clients[1].recv(4096)
            print(pickle.loads(client_message))
                #player2 = f"[red] Player 2 chose: {pickle.loads(client_message)}"
                #clients[1].send(pickle.dumps(player2))

            #teamLocalTactics.input_champion
            #player1 = []
            #player2 = []    
            #input_champion('Player 1', 'red', champions, player1, player2)
            #input_champion('Player 2', 'blue', champions, player2, player1)

            lock.release()

            #select_champion(champs)
            
            #Lister er over funksjonen
            testPlayer1.append("Twist")
            testPlayer2.append("Siva")
            print(testPlayer1, len(testPlayer1))
            print(testPlayer2, len(testPlayer2))
            # if conn == clients[0]:
            while True:
                if len(testPlayer1) == 2 and len(testPlayer2) == 2:
                    run_match(testPlayer1, testPlayer2, conn) # conn 1 og conn 2
                    break
            break
    #conn.close()

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
    threadCount = 0
    global clients
    clients = []
    
    while True:
        conn, addr = serverSideSocket.accept()
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        clients.append(conn)
        start_new_thread(multi_threaded_client, (conn, ))
        threadCount += 1
        print('Thread Number: ' + str(threadCount))

    #ServerSideSocket.close()


if __name__=="__main__":
    main()