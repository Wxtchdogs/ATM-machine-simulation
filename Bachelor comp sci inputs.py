#Cash inputs
fives = int(input("Enter the required number of $5 notes"))
fivesTotal = (fives * 5)
print("Required amount is", fivesTotal)
tens = int(input("Enter the required number of $10 notes"))
tensTotal = (tens * 10)
print("Required amount is", fivesTotal + tensTotal)
twenties = int(input("Enter the required number of $20 notes"))
twentiesTotal = (twenties * 20)
print("Required amount is", fivesTotal + tensTotal + twentiesTotal)
fifties = int(input("Enter the required number of $50 notes"))
fiftiesTotal = (fifties * 50)
print("Required amount is", fivesTotal + tensTotal + twentiesTotal + fiftiesTotal)
hundreds = int(input("Enter the required number of $100 notes"))
hundredTotal = (hundreds * 100)
remainder = fivesTotal + tensTotal + twentiesTotal + fiftiesTotal + hundredTotal
print("Remaining balance is", remainder)

def sanitize(userinput):
    validNumbers = [5,10,20,50,100]
    while True:
        if userinput not in validNumbers:
            print("invalid input! :(")
            userinput = int(input("Enter the deposited note value (5, 10, 20, 50 or 100):"))
        else: 
            return userinput

#Deposits
depositTotal = 0
userDeposit = sanitize(int(input("Enter the deposited note value (5, 10, 20, 50 or 100):")))

depositTotal = depositTotal + userDeposit
while True:
    sum = remainder - depositTotal
    print("Remaining balance is", sum)
    if sum == 0:
        print("Thanks for choosing Utopia Bank")
        print("$5", "["+str(fives)+"]", "\n$10", "["+str(tens)+"]", "\n$20", "["+str(twenties)+"]", "\n$50", "["+str(fifties)+"]", "\n$100", "["+str(hundreds)+"]")
        break
    elif sum > 0:
        userDeposit = sanitize(int(input("Enter the deposited note value (5, 10, 20, 50 or 100):")))
        depositTotal = depositTotal + userDeposit
    else: 
        print("The deposit amount", userDeposit, "exceeds the required amount", remainder, "Transaction cannot be completed")
        break
        
exit = input("Enter any key to exit")
