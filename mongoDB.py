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
clusterName = "inf142-ma"

# Connect to your cluster
client = MongoClient("mongodb+srv://"+ username + ":" + password + "@"+ clusterName + ".3w00x.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

# Create a new database in your cluster
database = client.INF142
# database = client.sample_airbnb
# databaseChamps = client.Champions
# Create a new collection in you database
person = database.person
# champions = databaseChamps.champsList

personDocument = {
  "firstname": "Tobias",
  "lastname": "Thorsen",
  "course": "INF142"
}
print(personDocument)
person.insert_one(personDocument)
print(person.inserted_id)
