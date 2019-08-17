i = 1
j = 7

for a in range(15):
    print("I=%d J=%d" % (i, j))
    if j == 5:
        i += 2
        j = 7
    else:
        j += -1
