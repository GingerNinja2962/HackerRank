# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty = Easy
# Score = 10

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    i = 1
    first, second = arr[0], arr[1]
    while first == second:
        i += 1
        first, second = arr[0], arr[i]
    print(second)
