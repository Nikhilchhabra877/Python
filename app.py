import sys
from dbhelper import DBHelper
class flipkart:
    def __init__(self):
        self.db=DBHelper()
        self.menu()

    def menu(self):
        user_input =input("""
        1. Enter 1 to register:
        2. Enter 2 to login:
        3. Anything else  to leave: """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
    def login_menu(self):
        input("""
        1. Enter 1 to see profile:
        2. Enter 2 to edit profile:
        3. Enter 3 to delete profile:
        4. Enter 4 to logout
        """)

    def register(self):
        name = input("Enter the name:")
        email = input("Enter the email:")
        password = input("Enter the password:")

        res = self.db.register(name,email,password)
        #print(res)
        if res == 1:
            print("Registration successful")
        else:
            print("Registration not successful")
    def login(self):
        email= input("1.Enter the email:")
        password = input("2. Enter the password:")
        res = self.db.search(email,password)
        if len(res) == 0:
             print("Not able to fetch data. Incorrect email/password.")
        else:
             print("Hello",res[0][1])
             self.login_menu()



fl = flipkart()
