valores = input().split()
valores = list(map(float, valores))

a, b, c = sorted(valores, reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if pow(a, 2) == pow(b, 2) + pow(c, 2):
        print("TRIANGULO RETANGULO")
    if pow(a, 2) > pow(b, 2) + pow(c, 2):
        print("TRIANGULO OBTUSANGULO")
    if pow(a, 2) < pow(b, 2) + pow(c, 2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b or b == c) and not (a == b and b == c):
        print("TRIANGULO ISOSCELES")
