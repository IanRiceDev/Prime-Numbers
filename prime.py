<<<<<<< HEAD
numberinput = input("Cheak prime: ")

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
    if m2 in basePrimes:
        message = numberinput+" is a prime number number."
        break
    if m2 in notPrimes:
        message = numberinput+" is not a prime number."
        break
    if m2 % 2 == 0:
        message = numberinput+" is not a prime number."
        break
    if m2 % 3 == 0:
        message = numberinput+" is not a prime number."
        break
    if m2 % 5 == 0:
        message = numberinput+" is not a prime number."
        break
    if m2 % 7 == 0:
        message = numberinput+" is not a prime number."
        break
    else:
        message = numberoutput+" is a prime number."
        break
print(message)
=======
numberinput = int(input("Cheak prime: "))
baseNum = numberinput

message = ""
basePrimes = [2,3,5,7]
notPrimes = [0,1]
m2 = baseNum
numberoutput = str(numberinput)
while True:

    if m2 in basePrimes:
        message = numberoutput+" is a prime number number."
        break
    if m2 in notPrimes:
        message = numberoutput+" is not a prime number."
        break
    if m2 % 2 == 0:
        message = numberoutput+" is not a prime number."
        break
    if m2 % 3 == 0:
        message = numberoutput+" is not a prime number."
        break
    if m2 % 5 == 0:
        message = numberoutput+" is not a prime number."
        break
    if m2 % 7 == 0:
        message = numberoutput+" is not a prime number."
        break
    else:

        message = numberoutput+" is a prime number."
        break

print(message)
>>>>>>> origin/master
