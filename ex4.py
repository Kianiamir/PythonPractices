# develop a program that calculates the factorial of a desired number.

from unittest import result


def factorial():
    n=int(input("please enter a number: "))
    while n < 0:
        n=input("please enter a non-negative number: ")
    if n == 0:
        result=1
    elif n==1:
        result=1
    else:
        result=n
        while n>1:
            n-=1
            result*=n
    print(result)

factorial()