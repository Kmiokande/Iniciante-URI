l1 = input().split()
l2 = input().split()

qt1 = int(l1[1])
valor1 = float(l1[2])
qt2 = int(l2[1])
valor2 = float(l2[2])

total = (qt1 * valor1) + (qt2 * valor2)

print("VALOR A PAGAR: R$ %0.2f" % total)
