import mysql.connector as connector

class Bank_account:
    def __init__(self):
        self.con = connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = 'root',
            database = 'banking_system')
        query="CREATE TABLE IF NOT EXISTS Bank(userid VARCHAR(10) PRIMARY KEY, Password INT NOT NULL,Name varchar(30) NOT NULL,Deposited INT Default 0, Withdrawal INT Default 0,Current_Balance INT)"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def Registration(self, userid, name, password):
        query = "insert into bank(userid, Name, Password) values('{}','{}',{})".format(userid, name, password)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def login(self):
        print()
        print("Enter Details to Login.")
        print()
        global userid 
        userid = input("Enter your userid: ")
        password = int(input("Enter your password: "))

        query = "SELECT * FROM bank WHERE userid='{}' AND Password={}".format(userid, password)
        cur = self.con.cursor()
        cur.execute(query)
        user_data = cur.fetchall()

        while True:
            if user_data:
                print()
                print("*****Login successful!*******")
                print()
                print("PRESS 1 to Show Details.")
                print("PRESS 2 to Deposit Money.")
                print("PRESS 3 to Withdraw Money.")
                print("PRESS 4 to Log Out.")
                print()
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.show_details(userid)
                    
                elif choice == 2:
                    amount = int(input("Enter the amount to deposit: "))
                    self.deposit(userid, amount)
                elif choice == 3:
                    amount = int(input("Enter the amount to withdraw: "))
                    self.Withdraw(userid, amount)
                    
                elif choice == 4:
                    break
                else:
                    print("Invalid choice!, Try Again.")
            else:
                print("Invalid userid or password.")
                print()
                break

    def show_details(self, userid):
        query = "SELECT * FROM bank WHERE userid='{}'".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        print()
        for rows in cur:
            print("User Id: ",rows[0])
            print("Password: ",rows[1])
            print("Name: ",rows[2])
            print("Deposited: ",rows[3])
            print("Withdrawal: ",rows[4])
            print("Current balance: ",rows[5])
        print()

    def deposit(self,userid,amount):

        query = "SELECT Deposited FROM bank WHERE userid='{}'".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        Deposited = cur.fetchone()[0]
        
        Deposited = Deposited + amount
        update_query = "UPDATE bank SET Deposited={} WHERE userid='{}'".format(Deposited, userid)
        cur.execute(update_query)
        self.con.commit()
        
        update_query = "UPDATE bank SET Current_Balance={} WHERE userid='{}'".format(Deposited, userid)
        cur.execute(update_query)
        self.con.commit()

        print('****Successfully Deposited****')

    
    def Withdraw(self,userid,amount):

        query = "SELECT Withdrawal FROM bank WHERE userid='{}'".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        Withdrawal = cur.fetchone()[0]
        Withdrawal = Withdrawal + amount

        query = "SELECT Deposited FROM bank WHERE userid='{}'".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        Deposited = cur.fetchone()[0]
        
        Current_Balance=Deposited - Withdrawal

        update_query = "UPDATE bank SET Withdrawal={} WHERE userid='{}'".format(Withdrawal, userid)
        cur.execute(update_query)
        self.con.commit()

        update_query = "UPDATE bank SET Current_Balance={} WHERE userid='{}'".format(Current_Balance, userid)
        cur.execute(update_query)
        self.con.commit()
        print('**Successfully Withdrawn**')




    