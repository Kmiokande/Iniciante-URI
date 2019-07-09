diaInicio = input().split()
diaInicio = int(diaInicio[1])
horaInicio = input().split(':')
hInicio = int(horaInicio[0])
mInicio = int(horaInicio[1])
sInicio = int(horaInicio[2])

diaFinal = input().split()
diaFinal = int(diaFinal[1])
horaFinal = input().split(':')
hFinal = int(horaFinal[0])
mFinal = int(horaFinal[1])
sFinal = int(horaFinal[2])

dia = diaFinal - diaInicio

hora = hFinal - hInicio
if hora < 0:
    hora += 24
    dia -= 1

minuto = mFinal - mInicio
if minuto < 0:
    minuto += 60
    hora -= 1

segundos = sFinal - sInicio
if segundos < 0:
    segundos += 60
    minuto -= 1

print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minuto)
print("%d segundo(s)" % segundos)
