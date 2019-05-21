entrada = input().split()

inicio = int(entrada[0])
final = int(entrada[1])

if inicio < final:
    total = final - inicio
elif inicio > final:
    total = 24 - inicio + final
else:
    total = 24

print("O JOGO DUROU %d HORA(S)" % total)
