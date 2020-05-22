n = int(input())

for i in range(1, n+1):
    print('{val} {val_quadrado} {val_cubo}'.format(
        val=i, val_quadrado=i**2, val_cubo=i**3))
    print('{val} {val_quadrado} {val_cubo}'.format(
        val=i, val_quadrado=(i**2)+1, val_cubo=(i**3)+1))
