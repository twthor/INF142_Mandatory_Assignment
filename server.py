# Server side of TNT
import socket
from _thread import *
import pickle
from time import sleep
from threading import Lock
import teamLocalTactics
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
    welcome = teamLocalTactics.welcomeMessage()
    return welcome

def load_champions():
    champs = get_champs()
    return champs

"""

def chose_champs(userInput, connection):
    if clients[0] == connection:
        # fiks valid champ
        # teamLocalTactics.valid_champion(userInput, load_some_champs(), player1, player2)
        player1.append(userInput)
    elif clients[1] == connection:
        # teamLocalTactics.valid_champion(userInput, load_some_champs(), player2, player1)
        player2.append(userInput)

def valid_champion(userInput: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected. Returns userinput if champion is valid.
    while True:
        if userInput not in champions:
             (f'The champion {userInput} is not available. Try again.')
        if userInput in player1:
            return (f'{userInput} is already in your team. Try again.')
        if userInput in player2:
            return(f'{userInput} is in the enemy team. Try again.')
        else:
            return userInput

def run_match(player1, player2, connection):
    match_results = teamLocalTactics.match(player1, player2)
    # match_results = pickle.dumps(match_results)
    for result in match_results:
        result = pickle.dumps(result)
        # connection.send(result)
    # lastTable = pickle.dumps(match_results[:-1])
    # connection.send(lastTable)
    # return match_results

def select_champion(champions):
    while True:
        player = "[red] Player 1"
        message = pickle.dumps(player)
        clients[0].sendall(message)

        '''userInput = clients[0].recv(4096)
        if userInput not in champions:
            return (f'The champion {userInput} is not available. Try again.')
        if userInput in player1:
            return (f'{userInput} is already in your team. Try again.')
        if userInput in player2:
            return(f'{userInput} is in the enemy team. Try again.')
        else:
            return userInput'''"""

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
            '''
            print("player1 ", player1)
            print("player2 ", player2)
            run_match(player1, player2)'''

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

    # global variables 
    global threadCount
    global clients
    threadCount = 0
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