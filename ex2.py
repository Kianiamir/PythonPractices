#develop a program that gives a number and tells if it's a step number or not!
#a step number is a in which every digit equals it's previous digit plus or minus one.

def isStep(number):
    while len(str(number))<2:
        number=input("Enter a number with at least two digits: ")
    res=[]
    baseDigit=int(str(number)[0])
    for digit in str(number)[1:]:
        res.append( abs(int(digit) - baseDigit) == 1)
        baseDigit=int(digit) 

    if False in res:
        print("no")
    else:
        print("yes")

isStep(767)
