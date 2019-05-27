valores = [0, 0, 0, 0, 0]
cont = 0

for a in range(5):
    valores[a] = int(input())
    cond = valores[a] % 2 is 0
    if cond:
        cont += 1

print("%d valores pares" % cont)
