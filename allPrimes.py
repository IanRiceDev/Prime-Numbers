import primeclass
z = 1

i = 0
while i < 100:
    x = primeclass.check_if_prime(z)
    print(x)
    i += 1
    z += 1
