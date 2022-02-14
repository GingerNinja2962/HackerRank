# https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty = Easy
# Score = 10

if __name__ == '__main__':
    the_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        the_list.append([name, score])
    the_list.sort(key= lambda x: x[1])
    i = 1
    first, second = the_list[0][1], the_list[1][1]
    while first == second:
        first, second = the_list[0][1], the_list[i][1]
        i += 1
    new_list = sorted( [ name for name, score in the_list if score == second ] )
    for item in new_list:
        print(item)
