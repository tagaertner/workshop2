#Task 4: write 4 options that will run on app.py
# import locale is to covert to USD currency
import locale

# function 1 show_balance
# code should display the account balance of the user. 

def show_balance(balance):
    if balance ==0:
        print("Your balance is currently $0.00\n")
    else:
        locale.setlocale(locale.LC_ALL, '')
        usd_balance = locale.currency(balance, grouping = True)
        print(f"Current balance:{usd_balance}\n")
    
    return balance

#function2 deposite. User inputs amount depostied and the new balance will be printed
def deposit(balance):
    locale.setlocale(locale.LC_ALL, '')
    amount = float(input("Enter the amount to be deposit:"))
    balance += amount
    usd_balance = locale.currency(balance, grouping = True)
    print(f"Current balance: {usd_balance}\n")
    
    return balance

#function 3 withdraw user inputs amount withdraw and new balance will print out
# use cannot overdraft, will create an error message
def withdraw(balance):   
    locale.setlocale(locale.LC_ALL, '')
    amount = float(input("Enter amount to withdraw:"))
    if amount <= balance:
        balance -= amount
        usd_balance = locale.currency(balance, grouping = True)
        print(f"Current balance: {usd_balance}\n")
    else:
        print(" Insufficent funds\n")
    
    return balance 

#function 4 logout
def logout(name):
    print(f"Goodbye {name}\n")



  
