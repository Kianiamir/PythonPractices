# Develop a program that recieves a sorted (lower to higher) list of numbers with some missing in between
# also ask user for the number of the input variables
# and gives back the missing numbers


def findMissed ():
    myList=input("enter your list of numbers: (just numbers seperated with a space) ")
    myList=myList.split(" ")
    for i in range(len(myList)):
        myList[i]=int(myList[i])
    count=int(input("How many numbers did you enter? "))
    while count != len(myList):
        count=int(input("Wrong Count! How many numbers did you enter? "))
    firstNum=myList[0]
    if (firstNum+count-1) != myList[-1]:
        trueList=list(range(firstNum,firstNum+count+1))
        missedList=[]
        for n in trueList:
            if n not in myList:
                missedList.append(n)
        print(f"the original list is: {myList}")
        print(f"True list is: {trueList}")
        print(f"this is the list of missing digits: {missedList}")
    else:
        print("You can't fool me! Your list does not have any missing digits in between")
findMissed()