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

    def get_votes(self,text_id):
        sql = "SELECT admin FROM admins"
        self.cursor.execute(sql)
        admin_dicts = self.turn2dict(self.cursor)
        admin_list  = [admin['admin'] for admin in admin_dicts]

        sql = "SELECT admin,vote FROM votes WHERE EXISTS(SELECT admin from admins WHERE admins.admin = votes.admin AND votes.id = 12)" # votes for text
        self.cursor.execute(sql,text_id)
        votes_dict = {vote['admin']: vote['vote'] for vote in self.turn2dict(self.cursor)}

        for admin in admin_list:
            if votes_dict.get(admin) is None:
                votes_dict[admin] = 'waiting'
            elif votes_dict.get(admin) is 1:
                votes_dict[admin] = 'good'
            elif votes_dict.get(admin) is 0:
                votes_dict[admin] = 'bad'
        print("asdf")

    @staticmethod
    def turn2dict(cursor):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
        return data