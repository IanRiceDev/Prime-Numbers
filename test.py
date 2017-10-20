numberinput = input("Cheak prime: ")

message = ""
basePrimes = [2,3,5,7]
notPrimes = [0,1]
from sys import exit
exit()

while True:

    if numberinput.isdigit() == False:
        print("That is not a number")
        break
    if True:
        numberoutput = int(numberinput)
        baseNum = numberoutput
        m2 = baseNum
    if m2 in basePrimes:
        message = numberinput+" is a prime number number."
        break
    if m2 in notPrimes:
        message = numberinput+" is not a prime number."
        break
    else:
        break
for prime in basePrimes :
    if m2 % prime == 0:
        message = numberinput + " is not a prime number."
        break
    else:
        message = numberinput + " is a prime number."
        break
print(message)
input("Press anything to exit!")