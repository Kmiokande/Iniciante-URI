valor = int(input())

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

if 0 < valor < 1000000:
    print("%d" % valor)

    cem = valor // 100
    valor = valor % 100

    cinquenta = valor // 50
    valor = valor % 50

    vinte = valor // 20
    valor = valor % 20

    dez = valor // 10
    valor = valor % 10

    cinco = valor // 5
    valor = valor % 5

    dois = valor // 2
    valor = valor % 2

    um = valor // 1

    print("%d nota(s) de R$ 100,00" % cem)
    print("%d nota(s) de R$ 50,00" % cinquenta)
    print("%d nota(s) de R$ 20,00" % vinte)
    print("%d nota(s) de R$ 10,00" % dez)
    print("%d nota(s) de R$ 5,00" % cinco)
    print("%d nota(s) de R$ 2,00" % dois)
    print("%d nota(s) de R$ 1,00" % um)
