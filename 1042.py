entrada = input().split()

valores = [int(i) for i in entrada]
valores.sort()

for a in valores:
	print(a)

print()

for b in entrada:
	print(b)
