# programa 9: programa que calcule el costo total de un articulo si: + son 3 articulos o menos el precio unitario sera de 35, si es maypr sera 30
# Fecha de elaboracion: 2024/10/25
# Elaborado por: Edgar Alejandro

art = int(input("digite el numero de articulos:  "))

if art <= 3:
    costo = art * 45
else:
    costo = art * 35
print("El costo total es de:", costo)
print("gracias por usar el programa")
