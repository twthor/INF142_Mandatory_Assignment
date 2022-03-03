import pymongo
# import client
#import champlistloader

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

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
with open("some_champs.txt") as f:
  for line in f:
    line = line.split(",")
    stats[line[0]] = [line[1], line[2], line[3][:-1]]

champStats.insert_one(stats)

