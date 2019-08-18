passWd = 2002

while True:
    entrada = int(input())
    if entrada == passWd:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
