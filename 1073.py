n = int(input())

for a in range(1, n+1):
    if a % 2 == 0:
        val = pow(a, 2)
        print("%d^2 = %d" % (a, val))
