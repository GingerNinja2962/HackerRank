# https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty = Easy
# Score = 10

if __name__ == '__main__':
    N = int(input())
    the_commands = []

    for _ in range(N):
        the_commands.append(input())

    the_list = []

    for commands in the_commands:
        command = commands.split(" ")

        if command[0] == "insert":
            the_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(the_list)

        elif command[0] == "remove":
            the_list.remove(int(command[1]))

        elif command[0] == "append":
            the_list.append(int(command[1]))

        elif command[0] == "sort":
            the_list.sort()

        elif command[0] == "pop":
            the_list.pop()

        elif command[0] == "reverse":
            the_list.reverse()
