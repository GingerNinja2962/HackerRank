# https://www.hackerrank.com/challenges/text-wrap/problem
# Difficulty = Easy
# Score = 10

def wrap(string, max_width):
    n_string = ''
    for index, char in enumerate(string):
        if (index) % max_width == 0 and index != 0:
            n_string = n_string + "\n"
        n_string = n_string + char
    return n_string
