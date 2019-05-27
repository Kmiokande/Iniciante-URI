valores = [0, 0, 0, 0, 0, 0]
cont = 0

for a in range(6):
    valores[a] = float(input())
    if valores[a] > 0:
        cont += 1

print("%d valores positivos" % cont)
