# https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty = Easy
# Score = 20

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    empty_string = ''
    previous = ' '
    for char in s:
        if char.isalpha() and previous == ' ':
            the_char = char.upper()
        else:
            the_char = char
        empty_string = empty_string + the_char
        previous = char
    return empty_string
