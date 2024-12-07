# programa 9: break and continue
# Fecha de elaboracion: 2024/11/8
# Elaborado por: Edgar Alejandro Esparza Reyes

# Ejemplo break
i = 1

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
print("final del programa")

# Ejemplo continue
i = 1

while i <= 10:
    print(i)
    if i == 5:
        i += 1
        continue
    i += 1
print("final del programa")
