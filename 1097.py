i = 1
j = 7

for a in range(5):
    for b in range(3):
        print("I=%d J=%d" % (i, j))
        j += -1
    i += 2
    j = i + 6
