import pymongo
import client 

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

print(pymongo.version)

# Get you password from .env file
password = os.environ.get("password")
username = "admin"
clusterName = "inf142-cluster-demo"

# Connect to you cluster
client = MongoClient('mongodb+srv://' + username + ':' + password + '@' + clusterName + '.67x6a.mongodb.net/demo-db?retryWrites=true&w=majority')

# Create a new database in your cluster
database = client.INF142

# Create a new collection in you database
person = database.person

personDocument = {
  "firstname": "Ola",
  "lastname": "Nordmann",
  "course": "INF142"
}

person.insert_one(personDocument)