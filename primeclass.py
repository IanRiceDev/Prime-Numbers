# defines this file as a class
def check_if_prime(numberinput):

    # defines vars
    numbertest = str(numberinput)
    message = ""
    basePrimes = [2,3,5,7]
    notPrimes = [0,1]

    # loop where the work of the class takes place
    while True:
        # checks if the in put is a number before math of the class
        if numbertest.isdigit() == False:
            print("That is not a number")
            break
        # defines vars in the scope of the loop
        if True:
            numberoutput = int(numberinput)
            baseNum = numberoutput
            basePrime = baseNum
        # checks if number is a part of base primes
        if basePrime in basePrimes:
            message = numbertest+" is a prime number number."
            break
        # checks if number is a part of numbers that can not be prime
        if basePrime in notPrimes:
            message = numbertest+" is not a prime number."
            break
        # uses modelo oprater to test remander of devishon for primes
        if basePrime % 2 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 3 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 5 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 7 == 0:
            message = numbertest+" is not a prime number."
            break
        # else must be prime
        else:
            message = numbertest+" is a prime number."
            break
    # returns var message
    return message
