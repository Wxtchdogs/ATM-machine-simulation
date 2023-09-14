actors = {"Brad pitt":"1980", "Tom cruise": "1970", "Michael keeton": "1976"}
movies = {"Black panther":"2018", "Indiana jones":"1980"}
games = {"Fallout":"2013", "Minecraft":"2008"} 

options1 = [0, 1, 2, 3]
options2 = [1, 2, 3, 4]

#Add to dictionary function
def add(theDict):
    print(theDict)
    value1 = input("Enter the name")
    value2 = input("Enter the year")
    theDict[value1] = value2
    print("The new dictionary:", theDict)
    
#Delete from dictionary function.
def delete(theDict):
    print(theDict)
    value = input("What would you like to delete?")
    while value not in theDict:
        print("That is not in the dictionary")
        value = input("What would you like to delete?")
    del theDict[value]
    print("The new dictionary:", theDict)

#Search for item function
def search(theDict):
    value = input("What would you like to search for?")
    if value in theDict:
        print(f"{value} is in the dictionary")
    else:
        print(f"{value} is not in the dictionary")
    print(theDict)

#Sorting function
def sort(theDict):
    ascending = sorted(theDict)
    descending = sorted(theDict, reverse=True)
    print("The dictionary in ascending order:", ascending)
    print("The dictionary in descending order:", descending)

#Program starts here and will loop unless told otherwise.
while True:
    #Arbitrary numbers that aren't in the options dictionarys.
    myInput1 = 4
    choice = 5

    #Validate inputs. The try is for checking that the input is an int.
    while myInput1 not in options1:
        try:
            myInput1 = int(input("Which dictionary would you like to edit/search/sort? Actors[1] Movies[2] Games[3] Enter 0 to exit the program."))
        except:
            print("Invalid input")

    if myInput1 == 1:
        theDict = actors
    elif myInput1 == 2:
        theDict = movies
    elif myInput1 == 3:
        theDict = games
    else:
        break

    while choice not in options2:
        try:
            choice = int(input("What would you like to do? Add[1] Delete[2] Search[3] Sort[4]"))
        except:
            print("Invalid input")    

    #Use the choice input to trigger the correct function.
    if choice == 1:
        add(theDict)
    elif choice == 2:
        delete(theDict)
    elif choice == 3:
        search(theDict)
    else:
        if choice == 4:
            sort(theDict)