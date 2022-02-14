# https://www.hackerrank.com/challenges/find-a-string/problem
# Difficulty = Easy
# Score = 10

def count_substring(string, sub_string):
    counted = 0
    for i in range((len(string)-len(sub_string))+1):
        if sub_string == string[i:i+len(sub_string)]:
            counted += 1
    return counted
