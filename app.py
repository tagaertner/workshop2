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
while True:
    print("          === Automated Teller Machine ===          ")
    name = input("Enter a name to register:\n")

    if len(name) >= 1 and len(name) <= 10:
        pin = input("Enter 4-digit PIN:\n")
    
        if pin.isdigit() and len(pin) == 4:
            balance = 0
            print(f"{name} has been registered with a starting balance of ${balance}\n")
            break
        else:
            print("Invalid PIN entered. PIN must be 4 digits.")
    else:
        print("Invalid name. Name must be between 1 and 10 characters.")

#task 3 while loop that request the users name and pin 
#

while True:
    print("          === Automated Teller Machine ===          ")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        
        print("Login successful!")
        break
    if name_to_validate != name or pin_to_validate != pin:
        print("Invalid credentials!")

atm_menu(name)
option = input(f"{name} choose an option:")
print("Choose an option", option)