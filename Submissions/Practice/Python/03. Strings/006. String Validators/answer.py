# https://www.hackerrank.com/challenges/string-validators/problem
# Difficulty = Easy
# Score = 10

def c_aphlanum(string):
    for char in string:
        if char.isalnum():
            return True
    return False


def c_alpha(string):
    for char in string:
        if char.isalpha():
            return True
    return False


def c_digit(string):
    for char in string:
        if char.isdigit():
            return True
    return False


def c_lower(string):
    for char in string:
        if char.islower():
            return True
    return False


def c_upper(string):
    for char in string:
        if char.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(c_aphlanum(s))
    print(c_alpha(s))
    print(c_digit(s))
    print(c_lower(s))
    print(c_upper(s))
