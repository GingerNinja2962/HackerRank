# https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty = Easy
# Score = 10

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    the_list = []
    for item_1 in range(x+1):
        for item_2 in range(y+1):
            for item_3 in range(z+1):
                if ( item_1 + item_2 + item_3 ) != n :
                    the_list.append([item_1, item_2, item_3])
    print(the_list)
