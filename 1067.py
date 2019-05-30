x = int(input())

for a in range(1, x+1):
    cond = a % 2 != 0
    if cond:
        print(a)
