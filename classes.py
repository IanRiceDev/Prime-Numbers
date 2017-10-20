import sys
from newPrime import *
def checkBasePrimes(numToCheck):
    if int(numToCheck) in basePrimes:
        print(str(numToCheck) + " is a prime number")
        sys.exit()
def checkNotPrimes(numToCheck):
    if int(numToCheck) in notPrime:
        print(str(numToCheck) + " is not a prime number")
        sys.exit()
def checkNumbers(numToCheck,num):
    if numToCheck % num == 0:
        print(str(numToCheck) + " is not a prime number")
        sys.exit()


