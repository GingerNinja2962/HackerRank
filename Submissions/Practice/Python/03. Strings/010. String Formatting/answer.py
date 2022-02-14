# https://www.hackerrank.com/challenges/python-string-formatting/problem
# Difficulty = Easy
# Score = 10

def print_formatted(number):
    for i in range(1, number+1):
        length = len(bin(number).lstrip("0b").rstrip("L"))

        var_2 = oct(i).lstrip("0o").rstrip("L")
        var_3 = hex(i).lstrip("0x").rstrip("L").upper()
        var_4 = bin(i).lstrip("0b").rstrip("L")

        print(f"{i}".rjust(length), end='')
        print(f"{var_2}".rjust(length+1), end='')
        print(f"{var_3}".rjust(length+1), end='')
        print(f"{var_4}".rjust(length+1))
