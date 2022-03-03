import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os
from socket import socket
from threading import Thread

sock = socket()
sock.bind(('localhost', 5550))
sock.listen()

print(pymongo.version)

# Get you password from .env file
password = os.environ.get("PASSWORD")
username = "admin"
clusterName = "inf142-cluster"

# Connect to your cluster
client = MongoClient("mongodb+srv://"+ username + ":" + password + "@"+ clusterName + ".mi4zj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create a new database in your cluster
database = client.Champions

# Create a new collection in you database
champStats = database.Champions
stats = {}
  
# databaseChamps = client.Champions
def makeDict(filename, collectionName):
  newDict = {}
  with open(f"{filename}") as f:
    for line in f:
      line = line.split(",")
      newDict[line[0]] = [line[1], line[2], line[3][:-1]]
  database.collectionName.insert_one(newDict)


# while True:
#   connectionSock, _ = sock.accept()
#   inputServer = connectionSock.recv(2048).decode()

#   connectionSock.sendall(inputServer.encode())
#   connectionSock.close()



