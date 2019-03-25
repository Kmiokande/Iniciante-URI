import math


valor = input().split()

a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

maior = (a + b + abs(a - b)) / 2
result = (maior + c + abs(maior - c)) / 2

print("%d eh o maior" % result)
