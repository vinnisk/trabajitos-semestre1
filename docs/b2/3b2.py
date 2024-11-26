# programa 3: analizar los operadores de comparacion
# Fecha de elaboracion: 2024/10/18
# Elaborado por: Edgar Alejandro Esparza Reyes
print("perro" == "perro")#verdadero, no son iguales
print("perro" != "gato")# no son iguales.
print ("Aguascalientes" < "Zacatecas")#Toma en cuenta el primer caracter de la palabra con el codigo asci y la A es antes que la z
print("Aire" >= "Agua")#lo mismo que la anterior, aunque  en este revisara el segundo caracter tambien.
print("\n")

# Operador "in"
# Revisa si la primer cadena está en la segunda
print("house" in "boathouse")#verdad house esta en boath"house"
print("bien" in "bienvenidos")#verdad bien esta en "bien"venidos
print("y" not in "ejes")#verdad y no esta en ninguna parte de ejes
print("je" not in "ejes")#falso, je esta en e"je"s y nosotros buscabamos que no estuviera
print("\n")

# operador "slicing" (rebanar)
#sirve para obtener un fragmento de una cadena dada si solo deseamos obtener un solo caracter, usaremos la indexacion
#indecing

print("Hola, mundo!"[0])#obtenemos la primera letra de la cadena Hola, mundo!
print("Hola, mundo!"[1:5])#obtenemos la subcadena desde la segunda hasta la quinta letra, es decir, Hola
print("Hola, mundo!"[6:])#obtenemos la subcadena desde la sexta hasta el final de la cadena, es decir, mundo!
print("Hola, mundo!"[:-2])#obtenemos la subcadena desde la primera hasta la penultima letra, es decir, Hola, mund
print("\n")
