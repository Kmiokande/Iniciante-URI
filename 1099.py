n = int(input())

for a in range(n):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])

    s = 0

    if x > y:
        for b in range((y + 1), x):
            if (b % 2) != 0:
                s += b
    if x < y:
        for b in range((x + 1), y):
            if (b % 2) != 0:
                s += b
    if x == y:
        s = 0

    print(s)
