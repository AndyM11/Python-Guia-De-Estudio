from pymongo import MongoClient
from pymongo.database import Database

# Base de datos local
# db_client: MongoClient = MongoClient().local

# Base de datos remota
db_client: Database = MongoClient(
    ""
).test
