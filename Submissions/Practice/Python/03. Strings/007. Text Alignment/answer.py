# https://www.hackerrank.com/challenges/text-alignment/problem
# Difficulty = Easy
# Score = 10

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

# for i in range(thickness):
#     print(f"{(1+(i*2))*c}".center(thickness+4, " "))

# for i in range(thickness+1):
#     print(f"{(thickness//2)*' '}{thickness*c}{(thickness*3)*' '}{thickness*c}")

# for i in range((thickness//2)+1):
#     print(f"{(thickness//2)*' '}{(thickness*4)*c}{thickness*c}")

# for i in range(thickness+1):
#     print(f"{(thickness//2)*' '}{thickness*c}{(thickness*3)*' '}{thickness*c}")

# for i in range(thickness):
#     print(f"{thickness//2*' '}{(thickness*4)*' '}{(1+(i*2))*c}".center(thickness+4, " "))

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1, " ")+c+(c*i).ljust(thickness-1, " "))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
