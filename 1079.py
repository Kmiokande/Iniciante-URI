n = int(input())

medias = []
for a in range(n):
    notas = input().split()
    n1 = float(notas[0])
    n2 = float(notas[1])
    n3 = float(notas[2])
    result = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    medias.append(result)

for a in medias:
    print('%.1f' % a)
