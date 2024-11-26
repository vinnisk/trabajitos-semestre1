# programa 10: Revisar si puedes ver una pelicula en netflix. la condicion para esto es que seas mayor de edad u hayas comprado la pelicula
# Fecha de elaboracion: 2024/10/25
# Elaborado por: Edgar Alejandro

edad = int(input("Digite su edad: "))

if edad >= 18:
    pel = int(input("La pelicula fue comprada \n 1.- si \n 2.- no\n"))
    if pel == 1:
        print("Puedes ver la pelicula:")
else:
    print("No puedes ver la pelicula")

# solucion 2
if edad >= 18 and pel == 1:
    print("Puedes ver la pelicula")
else:
    print("No puedes ver la pelicula")
print("gracias por usar")
