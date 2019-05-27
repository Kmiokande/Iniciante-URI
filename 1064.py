valores = [0, 0, 0, 0, 0, 0]
positivos = []
cont = 0
result = 0
med = 0

for a in range(6):
    valores[a] = float(input())
    if valores[a] > 0:
        cont += 1
        positivos.append(valores[a])

for a in positivos:
    result += a
med = result / len(positivos)

print("%d valores positivos" % cont)
print("%.1f" % med)
