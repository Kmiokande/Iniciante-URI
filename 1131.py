inter = 0
gremio = 0
empate = 0
grenais = 0

while True:
    home, way = map(int, input().split())

    if home > way:
        inter += 1
    elif home < way:
        gremio += 1
    else:
        empate += 1
    grenais += 1

    print('Novo grenal (1-sim 2-nao)')
    new = int(input())

    if new == 2:
        break

print("{q} grenais".format(q=grenais))
print("Inter:{i}".format(i=inter))
print("Gremio:{g}".format(g=gremio))
print("Empates:{e}".format(e=empate))

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
elif inter == gremio:
    print('Nao houve vencedor')
