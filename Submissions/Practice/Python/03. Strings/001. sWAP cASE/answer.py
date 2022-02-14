# https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty = Easy
# Score = 10

def swap_case(s):
    ret_s = ''
    for char in s:
        if char.isupper():
            ret_s = ret_s + char.lower()
        elif char.islower():
            ret_s = ret_s + char.upper()
        else:
            ret_s = ret_s + char
    return ret_s
