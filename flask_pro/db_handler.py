import mysql.connector

class db_handler():

    def __init__(self):
        self.db= mysql.connector.connect(
            host="localhost",
            user="api",
            passwd="pass",
            database="garga")

        self.cursor = self.db.cursor()
        self.cursor.execute("SET NAMES 'utf8';")
        self.cursor.execute("SET CHARACTER SET utf8;")
        self.cursor.execute("show tables")

        for x in self.cursor:
            print(x)

    def insert_text(self,textname,text,mahlas):
        sql = "INSERT INTO texts (textname, text, mahlas) VALUES (%s, %s, %s)"
        val = (textname, text, mahlas)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(self.cursor.rowcount," inserted")

    def get_waitings(self):
        sql = "SELECT * FROM texts"
        self.cursor.execute(sql)
        result = []
        for waiter in self.cursor:
            result.append(waiter)
        return result