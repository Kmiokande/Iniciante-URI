coelhos = 0
ratos = 0
sapos = 0
total = 0

quantCobaias = int(input())

for a in range(quantCobaias):
    cobaia = input().split()
    total += int(cobaia[0])
    tipo = str(cobaia[1])
    tipo.lower()

    if tipo == 'C':
        coelhos += int(cobaia[0])
    elif tipo == 'R':
        ratos += int(cobaia[0])
    elif tipo == 'S':
        sapos += int(cobaia[0])

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % coelhos)
print("Total de ratos: %d" % ratos)
print("Total de sapos: %d" % sapos)
print("Percentual de coelhos: %.2f %%" % float((100 * coelhos) / total))
print("Percentual de ratos: %.2f %%" % float((100 * ratos) / total))
print("Percentual de sapos: %.2f %%" % float((100 * sapos) / total))
