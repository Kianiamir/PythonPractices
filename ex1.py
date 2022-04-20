# # a random two-digit number is given to you. (we know it always has two-digit )
# # develope a program that calculates the difference of the digits witout subtarcting them.

# #Method 1:

def game(number):
    result = 0
    lnumber = []
    for x in str(number):
        lnumber.append(x)
    maximum=int(max(lnumber))
    minimum=int(min(lnumber))
    while (minimum+result)<maximum:
        result+=1
    print(result)

#test the results with any number
#game(19)
