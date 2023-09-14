actors = ["Brad pitt", "Tom cruise", "Michael keeton"]
movies = ["Black panther", "Indiana jones"]
games = ["Fallout", "Minecraft"]

options1 = [0, 1, 2, 3]
options2 = [1, 2, 3, 4]

#Add to list function
def add(theList):
    print(theList)
    value = input("What would you like to add?")
    theList.append(value)
    print("The new list:", theList)

#Delete from list function.
def delete(theList):
    print(theList)
    value = input("What would you like to delete?")
    while value not in theList:
        print("That is not in the list")
        print(theList)
        value = input("What would you like to delete?")
    theList.remove(value)
    print("The new list:", theList)

#Search for item function
def search(theList):
    value = input("What would you like to search for?")
    if value in theList:
        print(f"{value} is in the list")
    else:
        print(f"{value} is not in the list")
    print(theList)
    
#Sorting function
def sort(theList):
    ascending = sorted(theList)
    descending = sorted(theList, reverse=True)
    print("The list in ascending order:", ascending)
    print("The list in descending order:", descending)

#Program starts here and will loop unless told otherwise.
while True:
    #Arbitrary numbers that aren't in the options lists.
    myInput1 = 4
    choice = 5

    #Validate inputs. The try is for checking that the input is an int.
    while myInput1 not in options1:
        try:
            myInput1 = int(input("Which list would you like to edit/search/sort? Actors[1] Movies[2] Games[3] Enter 0 to exit the program."))
        except:
            print("Invalid input")

    if myInput1 == 1:
        theList = actors
    elif myInput1 == 2:
        theList = movies
    elif myInput1 == 3:
        theList = games
    else:
        break

    while choice not in options2:
        try:
            choice = int(input("What would you like to do? Add[1] Delete[2] Search[3] Sort[4]"))
        except:
            print("Invalid input")    

    #Use the choice input to trigger the correct function.
    if choice == 1:
        add(theList)
    elif choice == 2:
        delete(theList)
    elif choice == 3:
        search(theList)
    else:
        if choice == 4:
            sort(theList)