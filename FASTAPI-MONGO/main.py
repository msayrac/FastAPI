from fastapi import FastAPI

app = FastAPI()

# usename : admin
# password : test1234*

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:<db_password>@cluster0.dsdov6g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)