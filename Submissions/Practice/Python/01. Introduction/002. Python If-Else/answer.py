#!/bin/python3

# https://www.hackerrank.com/challenges/py-if-else/problem
# Difficulty = Easy
# Score = 10

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif (n % 2 == 0) and ((n > 1) and (n < 6)):
        print("Not Weird")
    elif (n % 2 == 0) and ((n > 5) and (n < 21)):
        print("Weird")
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")
