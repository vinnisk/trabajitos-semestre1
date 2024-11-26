# programa 8: Calcular los minutos, horas y meses.
# Fecha de elaboracion: 2024/10/16
# Elaborado por: Edgar Alejandro Esparza Reyes
dias = int(input("digite el numero de dias:"))

horas = dias * 24
minutos = horas * 60
meses = dias / 30

print("la cantidad de horas que hay en " + str(dias) + " es: " + str(horas))
print("la cantidad de minutos que hay en " + str(dias) + " es: " + str(minutos))
print("la cantidad de meses que son " + str(dias) + " son: " + str(meses))
