numberinput = input("Type any number to see if it is a prime number: ")

message = ""
basePrimes = [2,3,5,7]
notPrimes = [0,1]

while True:

    if numberinput.isdigit() == False:
        print("That is not a number")
        break

    if True:
        numberoutput = int(numberinput)
        baseNum = numberoutput
        m2 = baseNum
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

if m2 in basePrimes:
    message = numberinput+" is a prime number."


if m2 in notPrimes:
    message = numberinput + " is not a prime number."
    

print("\n")
print(message)
print("\n")
input("Press the enter key to exit")