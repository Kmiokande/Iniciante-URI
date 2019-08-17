maior = 0
posicao = 0

for a in range(1, 101):
    entrada = int(input())

    if entrada >= maior:
        maior = entrada
        posicao = a

print(maior)
print(posicao)
