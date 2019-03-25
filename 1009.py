nome = input()
salfix = float(input())
qtvendas = float(input())

bonus = (qtvendas * 15) / 100
total = salfix + bonus

print("TOTAL = R$ %0.2f" % total)
