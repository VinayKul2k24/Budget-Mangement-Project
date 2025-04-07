#importing required liberaries
import os, time, sys
from tabulate import tabulate

def printMessage(msg):
    for char in msg:
        time.sleep(1/10)
        print(char, end="", flush=True)

# ----------------------------------- USER ----------------------------------- #

# function to check if provided user credentional exist in data or not
def validCredential(username, password):
    
    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()
    
    isValid = False
    i=0
    
    for data in userData:
    
        if f"{username}___{password}___" in data:
            isValid = True
            break
        i+=1
        
    return isValid, i

# function to update either username or/and password of the user
def update_credentials():

    print("\nTo Confirm It's You, Please")
    
    print("\nRe-enter Username : ", end="")
    username = input()
    
    print("Re-enter Password : ", end="")
    password = input()
    
    isValid, line = validCredential(username, password)
    
    if not isValid:
        print()
        printMessage("Incorrect Username Or Password\n")
        printMessage("Terminating Credential Update\n")
        time.sleep(2)
        return
    
    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()
        
    individualData = userData[line].split("___")
    
    print("\n\t+---------------------+")
    print("\t|  Select Operation   |")
    print("\t+---------------------+")
    print("\t| 1 | Update Username |")
    print("\t| 2 | Update Password |")
    print("\t| 3 | Update Both     |")
    print("\t+---------------------+")

    updateChoice = int(input("\n\tUpdate Choice : "))
    
    if updateChoice == 1: 
        individualData[0] = input("\n\tEnter New Username : ")
    elif updateChoice == 2: 
        individualData[1] = input("\n\tEnter New Password : ")
    elif updateChoice == 3: 
        individualData[0] = input("\n\tEnter New Username : ")
        individualData[1] = input("\tEnter New Password : ")
    else:
        return
    
    userData[line] = "___".join(individualData)

    with open("userData.txt", 'w') as userDataFile:
        userDataFile.writelines(userData)
    
# function to view all details or himself/herself (users)
def view_all_details(line):

    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()

    currentUserData = userData[line].split("___")

    allData = [["Username", currentUserData[0]],  
    ["Password", currentUserData[1]],  
    ["Alloted Amt", currentUserData[2]],  
    ["Expended Amt", currentUserData[3]],  
    ["Remaining Amt", currentUserData[4]],  
    ["Expenses", currentUserData[5].replace('_', ' ')]]  
    
    print()
    print(tabulate(allData, tablefmt="grid"))
    

# function to view all expenses along with their price (as a list)
def view_all_expense(line):
    
    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()

    expenses = userData[line].split("___")[5].replace('_', '\n').replace('|', ' : ')
    print()
    print(f"Expenses List : \n\n{expenses}")


# function to see the remaining budget
def view_remaining_budget(line):
    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()

    remaining_budget = userData[line].split("___")[4]
    print()
    print(f"Remaining Amount : {remaining_budget}")
    
# function to add a new expense(s) along with their price
def add_expense(line):

    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()

    numberOfExpenses = int(input("\nEnter Number Of Expenses : "))
    
    itemAndPrice = {}
    totalPrice = 0
    
    for i in range(numberOfExpenses):
        item = input(f"\nItem {i+1} : ")
        price = input(f"Price {i+1} : ")
        itemAndPrice[item] = price
        totalPrice += int(price)


    currentData = userData[line].split("___")

    # if total price goes beyond the alloted price, cancel the purchase
    if int(currentData[4]) < totalPrice:
        printMessage("\nPrice Is Going Over Budget\n")
        printMessage("Re-consider the purchase again!\n")
        return

   
    if userData[line].split("___")[-1] == '\n':
        expensesToAdd = "" 
    else:
        expensesToAdd = "_"

    for item, price in itemAndPrice.items():
        expensesToAdd += f"{item}|{price}_"
    
    currentData[-1] = currentData[-1].replace('\n', f"{expensesToAdd[:-1]}\n")

    currentData[3] = str(int(currentData[3]) + totalPrice )
    currentData[4] = str(int(currentData[4]) - totalPrice )

    userData[line] = "___".join(currentData)

    with open("userData.txt", 'w') as userDataFile:
        userDataFile.writelines(userData)
    

# handling function for the user and related operations
def user_main():

    username = input("Enter Username : ")
    password = input("Enter Password : ")
    
    isValid, line = validCredential(username, password)
    
    if not isValid:
        print()
        printMessage("Incorrect Login Username Or Password\n")
        printMessage("Terminating Current Login Session\n")
        time.sleep(2)
        sys.exit(0)
        
    printMessage(f"\nWelcome Back {username}!\n")
    printMessage("Press Enter To Continue ...")
    input()
    os.system("cls")
    
    while True:
        
        os.system("cls")
        
        print("+---------------------------+")
        print("|     Select Operation      |")
        print("+---------------------------+")
        print("| 1 | Update Credentials    |")
        print("| 2 | View All Details      |")
        print("| 3 | View All Expense      |")
        print("| 4 | View Remaining Budget |")
        print("| 5 | Add Expense           |")
        print("| 6 | Exit                  |")
        print("+---------------------------+")

        try: operationChoice = int(input("\nOperation Choice : "))
        except: continue
        
        if   operationChoice == 1 : 
            update_credentials()
        elif operationChoice == 2 : 
            view_all_details(line)
        elif operationChoice == 3 : 
            view_all_expense(line)
        elif operationChoice == 4 : 
            view_remaining_budget(line)
        elif operationChoice == 5 : 
            add_expense(line)
        elif operationChoice == 6 : 
            sys.exit(0)
        elif operationChoice == 0 : 
            print()
            with open("userData.txt", 'r') as userDataFile:
                print(userDataFile.read())
        else : 
            continue
    
        input()

# ----------------------------------- ADMIN ---------------------------------- #

def update_admin_credentials():
    
    with open("adminData.txt", 'r') as adminDataFile:
        previous_pass = adminDataFile.read()
    
    print(f"\nPrevious Password : {previous_pass}")
    
    new_pass = input("\nNew Password : ")
    
    with open("adminData.txt", "w") as adminDataFile:
        adminDataFile.write(new_pass)


# function to see all users' each detail
def view_all_user_data():

    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()


    allUserData = [["Username", "Password", "Alloted Amt", "Expended Amt", "Remaining Amt", "Expenses"]]

    for data in userData:
        currentData = list(data.split("___"))
        currentData[-1] = currentData[-1].replace('_', ' ')
        allUserData.append(currentData)
        
    print()
    print(tabulate(allUserData, headers="firstrow", tablefmt="pretty"))
    input()


# function to see one particular user's data
def view_a_user_data():

    userToCheck = input("\nEnter Username : ")

    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines();
        
    aUserData = [["Username", "Password", "Alloted Amt", "Expended Amt", "Remaining Amt", "Expenses"]]

    for data in userData:
        if (list(data.split("___"))[0] == userToCheck):
            aUserData.append(list(data.split("___")))
        
    print()
    print(tabulate(aUserData, headers="firstrow", tablefmt="pretty"))



# function to add a new user
def add_a_user():

    print("\nEnter Details Of New User : \n")
    
    username = input("\tUsername : ")
    password = input("\tPassword : ")
    alloted_amt = input("\tAlloted Amount : ")
    expended_amt = '0'
    remaining_amt = alloted_amt
    expences = ""
    
    dataToAppend = "___".join([username, password, alloted_amt, expended_amt, remaining_amt, expences])
    
    with open("userData.txt", 'a') as userDataFile:
        userDataFile.write(dataToAppend + "\n")
    

# function to remove an existing user
def remove_a_user():

    userToDelete = input("\nEnter Username : ")
    
    if userToDelete != '':
    
        with open("userData.txt", 'r') as userDataFile:
            userData = userDataFile.readlines()
            
        for line, data in enumerate(userData):
            if userToDelete in data:
                userData.pop(line)
                
        with open("userData.txt", 'w') as userDataFile:
            userDataFile.writelines(userData)
    

# function to change alloted budget of an existing user
def update_budget():

    userToDelete = input("\nEnter Username : ")
    newBudget = input("Enter New Budget : ")
    
    with open("userData.txt", 'r') as userDataFile:
        userData = userDataFile.readlines()
        
    i=0
    
    for data in userData:
    
        if userToDelete in data:
            currentData = data.split("___")
            currentData[2] = newBudget
            currentData[4] = str(int(currentData[2]) + int(currentData[3]))
            userData[i] = "___".join(currentData)
        i+=1
    
    
    with open("userData.txt", 'w') as userDataFile:
        userDataFile.writelines(userData)
    

# handling function for the administrator and related operations
def admin_main():

    original_admin_password = ""
    with open('adminData.txt', 'r') as adminDataFile:
        original_admin_password = adminDataFile.read()
    
    input_admin_password = input("Enter Admin Password : ")

    if (original_admin_password != input_admin_password):
        print()
        printMessage("Incorrect Admin Password\n")
        printMessage("Terminating Current Admin Session\n")
        time.sleep(2)
        sys.exit(0)

    printMessage("\nWelcome Back Admin!\n")
    printMessage("Press Enter To Continue ...")
 
    input()
    os.system("cls")
 
    while True:
        
        os.system("cls")
        
        print("+------------------------+")
        print("|    Select Operation    |")
        print("+------------------------+")
        print("| 1 | Update Credential  |")
        print("| 2 | View All User Data |")
        print("| 3 | View A User's Data |")
        print("| 4 | Add A User         |")
        print("| 5 | Remove A User      |")
        print("| 6 | Update Budget      |")
        print("| 7 | Exit               |")
        print("+------------------------+")

        try: 
            operationChoice = int(input("\nOperation Choice : "))
        except: 
            continue

        if   operationChoice == 1 :
            update_admin_credentials()
        elif operationChoice == 2 :
            view_all_user_data()
        elif operationChoice == 3 : 
            view_a_user_data()
        elif operationChoice == 4 : 
            add_a_user()
        elif operationChoice == 5 : 
            remove_a_user()
        elif operationChoice == 6 : 
            update_budget()
        elif operationChoice == 7 : 
            sys.exit(0)
        elif operationChoice == 0 : 
            print()
            with open("userData.txt", 'r') as userDataFile:
                print(userDataFile.read())
        else : continue
        
        input()


# budget manager program's starting point
if __name__ == '__main__':
    os.system("cls")

    print("+--------------+")
    print("| Who're You ? |")
    print("+--------------+")
    print("| 1 | Admin    |")
    print("| 2 | User     |")
    print("+--------------+")

    admin_or_user = int(input("\nChoice : "))
    os.system("cls")
    
    if admin_or_user==1:
        admin_main()
    elif admin_or_user==2:
        user_main()