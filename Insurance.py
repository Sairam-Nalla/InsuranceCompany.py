# This is a program to practice OOP using insurance as an example
from random import randint
import sys

class Insurance:
    def __init__(self, fName, lName, insPlan):
        self.firstName = fName
        self.lastName = lName
        self.insurancePlan = insPlan
        self.id = str(randint(10000,99999))
        if (self.insurancePlan == "Platinum"):
            self.coverage = 0.15
        elif (self.insurancePlan == "Gold"):
            self.coverage = 0.10
        elif (self.insurancePlan == "Silver"):
            self.coverage = 0.7
        else:
            self.coverage = 0.5
            
    def __str__(self):
        return f"Name: {self.lastName}, {self.firstName} \nID: {self.id} \nInsurance Plan: {self.insurancePlan} ({100 * self.coverage}%)"
    
def registerAccount():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    print("Insurance Plan:")
    print("\tPlatinum   - 15% -    $750")
    print("\tGold       - 10% -    $600")
    print("\tSilver     - 07% -    $450")
    print("\tBronze     - 05% -    $300")
    print("\nWhat insurance plan would you like?")
    insPlan = input(">> ")
  
    newAcc = Insurance(firstName, lastName, insPlan)
    
    print("Account Created:")
    print(newAcc)
    return newAcc
    
def findAccount(accountStorage):
    print("**Entering Insurance Database**")
    print("What is the account ID?")
    accID = input(">> ")
    
    print(len(accountStorage))
    
    for acc in range(len(accountStorage)):
        if (accountStorage[acc].id == accID):
            print("ACCOUNT FOUND\n")
            return accountStorage[acc]
        
    print("ACCOUNT NOT FOUND\n")       
    return
def coPay(accountStorage):
    acc = findAccount(accountStorage)
    print("How much did your hospital visit cost?")
    bill = int(input("$"))
    covered = bill * acc.coverage
    rest = bill - covered
    print(" -------------------------------------------------------------------- ")
    print(f"|We will cover ${covered}. The ${rest} will need to be paid out of pocket|")
    print(" -------------------------------------------------------------------- ")
    
def menu():
    print("Welcome to the Insurance Database")
    print("1) Register Account")
    print("2) Lookup Account")
    print("3) Co-Pay")
    print("4) Exit")
    print()
    userInput = int(input("What would you like to do? "))
    
    accountStorage = []
    while(userInput != 4):
        if (userInput == 1):
            newUser = registerAccount()
            accountStorage.append(newUser)      
            print()
        elif (userInput == 2):
            print(findAccount(accountStorage))
            print()
        elif (userInput == 3):
            coPay(accountStorage)
            print()
            
        print("Welcome to the Insurance Database")
        print("1) Register Account")
        print("2) Lookup Account")
        print("3) CO-Pay")
        print("4) Exit")
        print()
        userInput = int(input("What would you like to do? "))
            
    print("GoodBye...")
    sys.exit()
    
    

menu()

      