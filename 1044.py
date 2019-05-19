entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
