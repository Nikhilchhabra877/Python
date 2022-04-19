import mysql.connector
import sys
class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost',user='root',password="rootroot",database='datascience')
            self.cursor = self.conn.cursor()
        except:

            print("Could not Connected to database")
            sys.exit(100)
        else:
            print('Database Connected')

    def register(self,Name,Email,password):
        try:
            self.cursor.execute("""insert into demo (Name,Email,password) values ('{}','{}','{}');""".format(Name,Email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def search(self,email,password):

        try:
            self.cursor.execute("""select * from demo where email like '{}' and password like '{}'""".format(email,password))
            data = self.cursor.fetchall()
            return data
        except:
            return -1


#db= DBHelper()
#print(db.search("nikhilchhabra877@gmail.com",'nikhil@12345'))