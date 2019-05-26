salario = float(input())
imposto = 0

if salario >= 0 and salario <= 2000:
    print("Isento")
elif salario > 2000 and salario <= 3000:
    taxa = salario - 2000
    imposto = taxa * 0.08
elif salario > 3000 and salario <= 4500:
    taxa = salario - 3000
    imposto = (taxa * 0.18) + (1000 * 0.08)
elif salario > 4500:
    taxa = salario - 4500
    imposto = (taxa * 0.28) + (1500 * 0.18) + (1000 * 0.08)

if imposto != 0:
    print("R$ %.2f" % imposto)
