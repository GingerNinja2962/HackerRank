# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Difficulty = Easy
# Score = 10

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    sizes = input().split(" ")

    for i in range(int(sizes[0])//2):
        print(f"{i * '.|.'}.|.{i * '.|.'}".center(int(sizes[1]), '-'))

    print("WELCOME".center(int(sizes[1]), '-'))


    for i in range(int(sizes[0])//2):
        i = ((int(sizes[0])//2) - i)-1
        print(f"{i * '.|.'}.|.{i * '.|.'}".center(int(sizes[1]), '-'))
