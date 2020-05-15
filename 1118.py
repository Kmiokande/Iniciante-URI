nota = 0
cont = 0
c = True

while c == True:
  x = float(input())

  if x >= 0.0 and x <= 10.0:
    nota += x
    cont += 1

    if cont == 2:

      print('media = {m:.2f}'.format(m=nota/2))
      cont = 0
      nota = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())

        if novo == 2:
          c = False
          break
        elif novo == 1:
          break

  else:
    print("nota invalida")
