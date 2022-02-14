# https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty = Easy
# Score = 10

import cmath

if __name__ == "__main__":
    the_function = input()
    test_1 = False

    if "+" in the_function:
        numbers = the_function.replace("j", "").split("+")

    else:
        numbers = the_function.replace("j", "").split("-")
        if the_function[0] == "-":
            numbers[0] = (int(numbers[1]) * -1)
            numbers[1] = (int(numbers[2]) * -1)
            test_1 = True

        else:
            numbers[0] = int( numbers[0] )
            numbers[1] = (int(numbers[1]) * -1)

    if the_function[0] == "-" and int(numbers[0]) > 0:
        numbers[0] = (int(numbers[0]) * -1)
        numbers[1] = int(numbers[1])

    else:
        numbers[0] = int( numbers[0] )
        numbers[1] = int( numbers[1] )


    absolute = abs(complex(numbers[0], numbers[1]))
    print(absolute)

    complex_num = cmath.phase(complex(numbers[0], numbers[1]))
    print(complex_num)

    # print(numbers[0])
    # print(numbers[1])

        # 83.8152730712
        # 2.83870778521
