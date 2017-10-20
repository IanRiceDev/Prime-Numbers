import sys
def checkNumbers(numToCheck,num):
    int(numToCheck)
    int(num)
    if numToCheck % num == 0:
        print(numToCheck + " is not a prime numbers")
        sys.exit()


