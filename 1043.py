entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

perimetro = a + b + c
area = (a + b) * c / 2

if a < (b + c) and b < (a + c) and c < (a + b):
	print("Perimetro = %.1f" % perimetro)
else:
	print("Area = %.1f" % area)
