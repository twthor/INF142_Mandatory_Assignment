from audioop import add
import pymongo
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
#database = client.Champions

# Create a new collection in you database
champions = client.Champions.Champions

#_id = ObjectId("622071c2c783b03eeaa139e3")
  
# databaseChamps = client.Champions
def addChampions(championList : list):
  newChampDict = {}
  newChampDict[championList[0]] = [championList[1], championList[2], championList[3][:-1]]
  champions.update(newChampDict)
  print(newChampDict)

def main():
  while userInput := input(">> Want to submit a champion? [Y/n] "):
    if userInput == "Y":
      newChampion = input(">> Type in this format: championName,stat1,stat2,stat3): ")
      listNewChamp = newChampion.split(",")
      addChampions(listNewChamp)
      print("Champion added!")
      break
    else:
      print(">> Shutting down..")
      break


if __name__== "__main__":
  main()