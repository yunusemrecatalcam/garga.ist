import mysql.connector

class db_handler():
    def __init__(self):
        self.db= mysql.connector.connect(
            host="localhost",
            user="api",
            passwd="pass",
            database="garga")

        mycursor = self.db.cursor()
        mycursor.execute("show tables")

        for x in mycursor:
            print(x)