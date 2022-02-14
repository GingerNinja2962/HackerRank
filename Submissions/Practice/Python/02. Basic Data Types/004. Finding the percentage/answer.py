# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Difficulty = Easy
# Score = 10

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    the_average =  sum(student_marks[query_name])/3
    print(f"{the_average:.2f}")
