pi = 3.14159
valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

triangulo = (a * c) / 2
circulo = (c * c) * pi
trapezio = c * (a + b) / 2
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)
