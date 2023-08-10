import sys

# from DataBase.class_DB import DB
from class_server import Server
from Test.test_db import DB

if __name__ == '__main__':
    db_conn = DB(test_option=True)
    server = Server(db_conn)
    server.start()