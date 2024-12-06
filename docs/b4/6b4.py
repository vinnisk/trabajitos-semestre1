# programa 6: Lista de todos los numeros menores a 50
# Fecha de elaboracion: 2024/11/6
# Elaborado por: Edgar Alejandro Reyes

numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 29]
menores = []
for numero in numeros:
    if numero < 50:
        menores.append(numero)
print("La lista original es: ", numeros)
print("La lista nueva es: ", menores)
