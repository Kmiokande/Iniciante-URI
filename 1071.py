x = int(input())
y = int(input())
soma = 0

if x < y:
	for a in range((x + 1), y):
		cond = a % 2 != 0
		if cond:
			soma += a
else:
	for a in range((y + 1), x):
		cond = a % 2 != 0
		if cond:
			soma += a

print(soma)