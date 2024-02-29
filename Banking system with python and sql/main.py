from bank_account import Bank_account

def main():
    db = Bank_account()

    while True:
        print('***** WELCOM BANKING SYSTEM *****')
        print()
        print('PRESS 1 TO REGISTRATION IF YOUR ACCOUNT IS NOT EXIST')
        print('PRESS 2 TO LOGIN ACCOUNT')
        print('PRESS 3 TO EXIT')
        print()
        try:
            choice = int(input())
            if(choice == 1):
                userid = int(input("Enter user Id : "))
                name=input("Enter user name : ")
                password=input("Enter user password : ")
                db.Registration(userid,name,password)
            
            elif choice == 2:
                db.login()

            elif choice == 3:
                break
            else:
                print('Invalid input Try again')

        
        except Exception as e:
            print(e)
            print("Invalid  Detalis Try again !!!")


main()
