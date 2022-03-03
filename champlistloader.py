from core import Champion
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os


def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))

def from_championsDB():
    # Credentials
    password = os.environ.get("PASSWORD")
    username = "admin"
    clusterName = "inf142-cluster"

    # Connect to your cluster
    client = MongoClient("mongodb+srv://"+ username + ":" + password + "@"+ clusterName + ".mi4zj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    

def from_csv(filename: str) -> dict[str, Champion]:
    champions = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = _parse_champ(line)
            champions[champ.name] = champ
    return champions


def load_some_champs():
    return from_csv('some_champs.txt')
