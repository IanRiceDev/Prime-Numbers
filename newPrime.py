import sys

notPrime = [0, 1]
basePrimes = [2, 3, 5, 7]
userInput = int(input())

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

checkNotPrimes(userInput)
checkBasePrimes(userInput)

checkNumbers(userInput, 2)
checkNumbers(userInput, 3)
checkNumbers(userInput, 5)
checkNumbers(userInput, 7)
userInput = str(userInput)

print(userInput + " is a prime number")
