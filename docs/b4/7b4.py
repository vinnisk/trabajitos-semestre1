# programa 7: filtro edades
# Fecha de elaboracion: 2024/11/7
# Elaborado por: Edgar Alejandro Esparza Reyes

edades = [70, 78, 89, 90, 15, 50, 60, 22, 30, 41, 8, 12, 36]

menores_18 = [] # Personas menores a 18 años

adul = [] # Personas mayores a 18 años pero menores de 65 años

adul_65 = [] # Personas mayores a 65 años

# Filtro para edades menores a 18

for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad < 65:
        adul.append(edad)
    else:
        adul_65.append(edad)

print("\nLas edades menores a 18 años son: ", menores_18)

print("\nLas edades entre 18 y 65 años son: ", adul)

print("\n\u87Las edades mayores a 65 años son: ", adul_65)
