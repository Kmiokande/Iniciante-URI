import math


entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

try:
	r1 = ((-b) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a);
	r2 = ((-b) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a);

	print("R1 = %.5f" % r1)
	print("R2 = %.5f" % r2)

except ValueError:
	print("Impossivel calcular");
except ZeroDivisionError:
	print("Impossivel calcular");
