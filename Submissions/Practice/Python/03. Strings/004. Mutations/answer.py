# https://www.hackerrank.com/challenges/python-mutations/problem
# Difficulty = Easy
# Score = 10

def mutate_string(string, position, character):
    s_new = ''
    for index, char in enumerate(string):
        if index == position:
            s_new = s_new + character
        else:
            s_new = s_new + char
    return s_new
