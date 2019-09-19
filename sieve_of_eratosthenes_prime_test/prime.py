import sys

number = input("Enter number: ")

if int(number) == 0:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()

elif int(number) == 1:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()
elif int(number) == 2:

    print(number, "is a prime number")
    input("Ending program")
    sys.exit()

elif int(number) == 3:

    print(number, "is a prime number")
    input("Ending program")
    sys.exit()

elif int(number) == 5:

    print(number, "is a prime number")
    input("Ending program")
    sys.exit()

elif int(number) == 7:

    print(number, "is a prime number")
    input("Ending program")
    sys.exit()

elif int(number) % 2 == 0:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()

elif int(number) % 3 == 0:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()

elif int(number) % 5 == 0:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()

elif int(number) % 7 == 0:

    print(number, "is not a prime number")
    input("Ending program")
    sys.exit()

else:

    print(number, "is a prime number")
    input("Ending program")
    sys.exit()

