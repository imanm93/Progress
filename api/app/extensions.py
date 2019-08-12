import os
from . import config as Config

# Get Config
application_mode = os.getenv('APPLICATION_MODE', 'DEV')
config = Config.get_config(application_mode)

# Extension to MongoDB
from pymongo import MongoClient
client = MongoClient(config.DB_URI)
db = client['progress_db']

# Extension to Neo4j
from py2neo import Graph
graph = Graph(config.GRAPHDB_URI)
