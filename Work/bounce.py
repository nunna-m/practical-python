# bounce.py
#
# Exercise 1.5
height = 100
fraction = 0.6 #3/5
for i in range(1,10+1):
    height = height * fraction
    print(i, round(height,4))