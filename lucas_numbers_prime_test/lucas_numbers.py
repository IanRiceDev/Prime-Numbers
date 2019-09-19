
lucas_iterator_1 = 2
lucas_iterator_2 = 1


print(lucas_iterator_2)
loop_iterator = 0

lucas_number = lucas_iterator_1 + lucas_iterator_2

while loop_iterator < 100:

    print(lucas_number)
    loop_iterator = loop_iterator + 1
    lucas_iterator_1 = lucas_iterator_2
    lucas_iterator_2 = lucas_number
    lucas_number = lucas_iterator_1 + lucas_iterator_2

input()
