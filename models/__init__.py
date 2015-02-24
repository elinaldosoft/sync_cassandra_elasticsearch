__author__ = 'elinaldo'
from config import CASSANDRA
from cqlengine import connection
connection.setup(CASSANDRA.get("IP"), CASSANDRA.get("DB"))