entrada = input().split()

cod = int(entrada[0])
quant = int(entrada[1])

if cod is 1:
    cQuente = quant * 4.00
    print("Total: R$ %.2f" % cQuente)
elif cod is 2:
    xSalada = quant * 4.50
    print("Total: R$ %.2f" % xSalada)
elif cod is 3:
    xBacon = quant * 5.00
    print("Total: R$ %.2f" % xBacon)
elif cod is 4:
    torrada = quant * 2.00
    print("Total: R$ %.2f" % torrada)
elif cod is 5:
    refrigerante = quant * 1.50
    print("Total: R$ %.2f" % refrigerante)
