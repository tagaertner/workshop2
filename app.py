"""Week 2 workshop Assigment, baking taks
by Tami Gaertner
last edited on 09/1/23"""
# import from banking pkg
from banking_pkg.account import show_balance, deposit, withdraw, logout
import locale

COMPANY_NAME = "Company"
def atm_menu(name,balance,deposit, withdraw, logout):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#taks 2 Registration of user and pin set up
#bonus 1 names 1-10 character are valid, if invalid show error message and promt to do it again
#bonus 2 pin can only be 4 characters, send error message if more or less than 4 and to try again
def create_account():
    user = ""
    pin = ""
    balance = 0
    while True:
        print("          === Automated Teller Machine ===          ")
        user = input("Enter a name to register:\n")

        if len(user) >= 1 and len(user) <= 10:
            pin = input("Enter 4-digit PIN:\n")
            if pin.isdigit() and len(pin) == 4:
                print(f"{user} has been registered with a starting balance of ${balance}\n")
                break
            else:
                print("Invalid PIN entered. PIN must be 4 digits.")
        else:
            print("Invalid name. Name must be between 1 and 10 characters.")
    return (user, pin, balance)

#task 3 while loop that request the users name and pin 
#
def login(name, pin):
    while True:
        print("          === Automated Teller Machine ===          ")
        name_to_validate = input("Enter name: ")
        pin_to_validate = input("Enter PIN: ")

        if name_to_validate == name and pin_to_validate == pin:
            print("Login successful!")
            break
        if name_to_validate != name or pin_to_validate != pin:
            print("Invalid credentials!")


#taks 5 add the 4 options from the account module
def option_select(name, balance, deposit, withdraw, logout):
    while True:
        atm_menu(name, balance, deposit, withdraw, logout)
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

if __name__ == "__main__":
    
    balance = 0
    name ="" 
    (name, pin, balance) = create_account()
    login(name, pin)
    balance = option_select(name, balance, deposit, withdraw, logout)
