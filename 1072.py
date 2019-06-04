n = int(input())

entre = 0
fora = 0

for a in range(0, n):
    x = int(input())
    if x >= 10 and x <= 20:
        entre += 1
    else:
        fora += 1

print("%d in" % entre)
print("%d out" % fora)
