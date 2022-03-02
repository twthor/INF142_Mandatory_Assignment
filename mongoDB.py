import pymongo
import client 

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

print(pymongo.version)

# Get you password from .env file
password = os.environ.get("PASSWORD")
username = "admin"
clusterName = "inf142-ma"
db_name = "TNT-db"

# Connect to you cluster
# client = MongoClient('mongodb+srv://' + username + ':' + password + '@' + clusterName + '.3w00x.mongodb.net/TNT-db?retryWrites=true&w=majority')
client = MongoClient("mongodb+srv://"+ username + ":" + password+ "@"+ clusterName + ".3w00x.mongodb.net/" + db_name + "?retryWrites=true&w=majority")
# Create a new database in your cluster
database = client.INF142

# Create a new collection in you database
person = database.person

personDocument = {
  "firstname": "Tobias",
  "lastname": "Thorsen",
  "course": "INF142"
}

person.insert_one(personDocument)