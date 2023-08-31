"""Week 2 workshop Assigment, baking taks
by Tami Gaertner
last edited on 8/30/23"""

def atm_menu(name):
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

name =""
pin =""
balance = 0
name = input("Enter a name to register\n")
pin=input("Enter PIN:\n")
balance= input(f"{name} has been registered with a starting balance of ${str(balance)}\n")

#task 3 while loop that request the users name and pin 
while True:
    name_to_validate = name 
    pin_to_validate = pin
     

atm_menu(name)
