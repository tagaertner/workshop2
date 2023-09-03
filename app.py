"""Week 2 Workshop Assigment, banking task
by Tami Gaertner
last edited on 09/2/23"""
# import from banking pkg and import locale is to show money in USD currency
from banking_pkg.account import show_balance, deposit, withdraw, logout
import locale

def atm_menu(name, balance):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#Task 2 :Registration of user and pin set up
#Bonus 1: names 1-10 character are valid, if invalid show error message and promt to do it again
#Bonus 2: pin can only be 4 characters, send error message if more or less than 4 and to try again
def create_account():
    user = ""
    pin = ""
    balance = 0
  
    while True:
        print("          === Automated Teller Machine ===          ")
        user = input("Enter a name to register:\n")

        if len(user) >= 1 and len(user) <= 10:
               break
        else:
            print("Invalid name. Name must be between 1 and 10 characters.")
                
    while True:            
            pin = input("Enter 4-digit PIN:\n") 
            if pin.isdigit() and len(pin) == 4:
                    print(f"{user} has been registered with a starting balance of ${balance}\n")
                    break
               
            else:
                    print("Invalid PIN entered. PIN must be 4 digits.")
          
    return (user, pin, balance)

#Task 3: Login request the users name and pin 
def login(name, pin):
    #for security max attempts of 3, then will exit code if unsuccessful 
    max_attempts = 3 
    attempts = 0
    login_successful = False
    
    while attempts < max_attempts:
        print("          === Automated Teller Machine ===          ")
        print("LOGIN")
        name_to_validate = input("Enter name: ")

        if name_to_validate == name:
            pin_to_validate = input("Enter PIN: ")
            if pin_to_validate == pin:
                print("Login successful!")
                login_successful = True
                break
            else:
                print("Invalid credentials!")
                attempts += 1
                break
        else:
            print("Invalid credentials!")
            attempts += 1
    if attempts == max_attempts:
        print("Maximum login attempts reached. Please try again later.\n")
        
    return login_successful

#taks 5 creat the 4 options link the account module to this page
def option_select(name, balance):
    while True:
        atm_menu(name, balance)
        option = input(f"{name}, choose an option: ")
        print("You chose option:", option)

        if option == "1":
            balance = show_balance(balance)
        elif option == "2":
            balance = deposit(balance)
        elif option == "3":
            balance = withdraw(balance)
        elif option == "4":
            logout(name)
            break

    return balance

#to make sure that this page runs first, per best practices
if __name__ == "__main__":
    
    balance = 0
    name ="" 
    (name, pin, balance) = create_account()
    
    #this code is executed after the login block of code runs. 
    #checks the retun vaule, if True the option_select will run
    #if returns False the else block of code will execute and exit.  
    if login(name, pin):
         balance = option_select(name, balance)
    else:
        exit(0)
