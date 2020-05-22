n = int(input())
x = 1

for i in range(n):
    print('{val1} {val2} {val3} PUM'.format(val1=x, val2=x+1, val3=x+2))
    x += 4
