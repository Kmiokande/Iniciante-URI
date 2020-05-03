a = 0
som = 0
med = 0

while a < 2:
    nota = float(input())

    if nota <= 0 or nota >= 10.1:
        print('nota invalida')
    else:
        som += nota
        a += 1

med = som / 2
print('media = {m:.2f}'.format(m=med))
