alcool = 0
gasolina = 0
diesel = 0

while True:
    op = int(input())

    if op == 1:
        alcool += 1
    elif op == 2:
        gasolina += 1
    elif op == 3:
        diesel += 1
    elif op == 4:
        break
    else:
        pass

print('MUITO OBRIGADO')
print('Alcool: {votos}'.format(votos=alcool))
print('Gasolina: {votos}'.format(votos=gasolina))
print('Diesel: {votos}'.format(votos=diesel))
