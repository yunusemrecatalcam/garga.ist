import mysql.connector
import datetime, time
VOTE_THRESHOLD = 3
FLOW_CHAR_LIM  = 500
class db_handler():

    def __init__(self):

        self.start_conn()
        self.cursor = self.db.cursor()
        self.cursor.execute("SET NAMES 'utf8';")
        self.cursor.execute("SET CHARACTER SET utf8;")
        self.stop_conn()

    def start_conn(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="api",
            passwd="pass",
            database="garga")
        self.cursor = self.db.cursor()

    def stop_conn(self):
        self.cursor.close()
        self.db.close()

    def insert_text(self,textname,text,mahlas,passkey):
        #hash = pbkdf2_sha256.encrypt(str(passkey), rounds=200000, salt_size=16)
        if mahlas == '' or textname == '' or \
            mahlas == '' or passkey == '':
            return 3
        self.start_conn()
        sql = "SELECT * FROM users WHERE mahlas='"+ str(mahlas) + "'"
        self.cursor.execute(sql)
        try:
            result = self.turn2dict(self.cursor)[0]
        except:
            result = None
        if result == None:    #new user
            sql = "INSERT INTO texts (textname, text, mahlas) VALUES (%s, %s, %s)"
            val = (textname, text, mahlas)
            self.cursor.execute(sql, val)
            print(self.cursor.rowcount, " inserted1")

            sql = "INSERT INTO users (mahlas,passwords) VALUES (%s, %s)"
            val = (mahlas, passkey)
            self.cursor.execute(sql, val)
            print(self.cursor.rowcount, " inserted2")

            self.db.commit()
            self.stop_conn()
            return 1
        elif result['mahlas']==mahlas and result['passwords']==passkey:
            sql = "INSERT INTO texts (textname, text, mahlas) VALUES (%s, %s, %s)"
            val = (textname, text, mahlas)
            self.cursor.execute(sql, val)
            self.db.commit()
            self.stop_conn()
            return 2
        else:
            return 0
    def get_waitings(self):
        self.start_conn()
        sql = "SELECT * FROM texts WHERE id NOT IN \
                (SELECT id FROM votes WHERE vote=1 GROUP BY id HAVING COUNT(id)>" + \
              str(VOTE_THRESHOLD) + ")" + "AND id NOT IN" + \
                "(SELECT id FROM votes WHERE vote=0 GROUP BY id HAVING COUNT(id)>" + \
              str(VOTE_THRESHOLD) + ")"

        self.cursor.execute(sql)
        result = []
        for waiter in self.cursor:
            result.append(waiter)
        self.stop_conn()
        return result

    def get_votes(self,text_id):
        self.start_conn()
        text_id = str(int(text_id))
        sql = "SELECT admin FROM admins"
        self.cursor.execute(sql)
        admin_dicts = self.turn2dict(self.cursor)
        admin_list  = [admin['admin'] for admin in admin_dicts]

        sql = "SELECT admin,vote FROM votes WHERE EXISTS" \
              "(SELECT admin from admins WHERE admins.admin = votes.admin AND votes.id = " + text_id + ')'# votes for text
        self.cursor.execute(sql)
        votes_dict = {vote['admin']: vote['vote'] for vote in self.turn2dict(self.cursor)}

        for admin in admin_list:
            if votes_dict.get(admin) is None:
                votes_dict[admin] = 'bekliyoruz'
            elif votes_dict.get(admin) is 1:
                votes_dict[admin] = 'iyi'
            elif votes_dict.get(admin) is 0:
                votes_dict[admin] = 'kötü'

        self.stop_conn()
        return votes_dict

    def get_text_and_attr(self, text_id):
        self.start_conn()
        sql = "SELECT textname, text, mahlas, reg_date, img_path FROM texts" \
              " WHERE id =" + str(text_id)
        self.cursor.execute(sql)
        text_dict = self.turn2dict(self.cursor)
        if len(text_dict) == 0:
            return {}        #if text not exists, its none

        self.stop_conn()
        return text_dict[0]

    def is_published(self, text_id):
        sql = "SELECT * FROM votes WHERE id=" + str(text_id)
        self.start_conn()
        self.cursor.execute(sql)
        text_dict = self.turn2dict(self.cursor)
        if len(text_dict) >= VOTE_THRESHOLD:
            return True
        else:
            return False
    def get_flow(self):

        self.start_conn()
        sql = "SELECT * FROM texts WHERE img_path!='' AND id IN \
                (SELECT id FROM votes WHERE vote=1 GROUP BY id HAVING COUNT(id)>"+\
                str(VOTE_THRESHOLD)+ ")" + "ORDER BY confirm_date DESC"
        self.cursor.execute(sql)
        result = []
        for res in self.cursor:
            trimmed = self.trim_text(res)
            result.append(trimmed)
        self.stop_conn()
        return result

    def get_waiting_for_img(self):

        self.start_conn()
        sql = "SELECT * FROM texts WHERE img_path is NULL AND id IN \
                (SELECT id FROM votes WHERE vote=1 GROUP BY id HAVING COUNT(id)>"+\
                str(VOTE_THRESHOLD)+ ")" + "ORDER BY id"
        self.cursor.execute(sql)
        result = []
        for res in self.cursor:
            trimmed = self.trim_text(res)
            result.append(trimmed)
        self.stop_conn()
        return result

    def admin_login(self, usr, passwd):
        self.start_conn()
        sql = "SELECT * FROM admins WHERE admin ='" + str(usr) + "' AND password ='" + str(passwd) + "'"
        self.cursor.execute(sql)
        text_dict = self.turn2dict(self.cursor)
        self.stop_conn()
        return False if len(text_dict)==0 else True

    def insert_vote(self, text_id, admin, vote):
        self.start_conn()
        sql = "INSERT INTO votes values(%s, %s, %s) ON DUPLICATE KEY UPDATE vote=%s"
        self.cursor.execute(sql, (text_id,admin,vote,vote))
        self.db.commit()
        sql = "SELECT * FROM votes WHERE id=" + str(text_id)
        self.cursor.execute(sql)
        text_dict = self.turn2dict(self.cursor)
        if len(text_dict) > VOTE_THRESHOLD:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            sql = "UPDATE texts SET confirm_date='" + str(timestamp)+ "'" + "WHERE id="+ str(text_id)
            self.cursor.execute(sql)
            self.db.commit()
        self.stop_conn()

    def search(self, key):
        self.start_conn()
        sql = "SELECT * FROM texts WHERE text LIKE %s AND img_path!='' "
        args = ['%' + key + '%']
        self.cursor.execute(sql, args)
        #text_dict = self.turn2dict(self.cursor)
        result = []
        for res in self.cursor:
            result.append(res)
        self.stop_conn()
        return result
    @staticmethod
    def turn2dict(cursor):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
        return data
    @staticmethod
    def trim_text(content_tuple):
        content = list(content_tuple)
        content[2] = str(content[2][:FLOW_CHAR_LIM]) + '...'
        return tuple(content)
