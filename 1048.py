salario = float(input())
reajuste = 0
percentual = 0

if salario >= 0 and salario <= 400:
    percentual = 15
    reajuste = ((salario * percentual) / 100) + salario
elif salario > 400 and salario <= 800:
    percentual = 12
    reajuste = ((salario * percentual) / 100) + salario
elif salario > 800 and salario <= 1200:
    percentual = 10
    reajuste = ((salario * percentual) / 100) + salario
elif salario > 1200 and salario <= 2000:
    percentual = 7
    reajuste = ((salario * percentual) / 100) + salario
elif salario > 2000:
    percentual = 4
    reajuste = ((salario * percentual) / 100) + salario

print("Novo salario: %.2f" % reajuste)
print("Reajuste ganho: %.2f" % (reajuste - salario))
print("Em percentual: %d %%" % percentual)
