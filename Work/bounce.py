# bounce.py
#
# Exercise 1.5

count = 0
ball_height = 100

while count < 10:
    ball_height *= 0.6
    count += 1
    print(count, round(ball_height, 4))    
