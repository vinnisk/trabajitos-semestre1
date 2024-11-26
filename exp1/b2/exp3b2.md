# programa 3: analizar los operadores de comparacion
## Fecha de elaboracion: 2024/10/18
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 4 muestra una comparacion entre dos cadenas, donde al ser exactamente iguales mostrara verdaderoverdadero
``` python
print("perro" == "perro")
```
- El resultado de la linea 5 tambien es vardadero ya que no son iguales, el conector logico es diferennte
``` python
print("perro" != "gato") 
```
- La linea 6 toma en cuenta el primer caracter de la palabra con el codigo asci y la A es antes que la z
``` python
print ("Aguascalientes" < "Zacatecas")
```
- La linea 7 es lo mismo que la anterior, aunque  en este revisara el segundo caracter tambien ya que el primero es el mismo en ambas.
``` python
print("Aire" >= "Agua")
```
#### Operador "in"
Revisa si la primer cadena está en la segunda
- El resultado del print en la linea 12 es verdad, house esta en boath"house"
``` python
print("house" in "boathouse")
```
- El resultado de la linea 11 tambien es verdad, bien esta en "bien"venidos
``` python
print("bien" in "bienvenidos")
```
- El resultado de la linea 12 es verdad, ya que esta vez buscamos que no este en la palabra comparada. "y" no esta en ninguna parte de "ejes"
``` python
print("y" not in "ejes")
```
- El resultado de la linea 13 es falso, je esta en e"je"s y nosotros buscabamos que no estuviera
``` python
print("je" not in "ejes")
```
#### operador "slicing" (rebanar)
sirve para obtener un fragmento de una cadena dada si solo deseamos obtener un solo caracter, usaremos la indexacion
- En la linea 22 obtenemos la primera letra de la cadena Hola, mundo!
``` python
print("Hola, mundo!"[0])
```
- En la linea 23 obtenemos la subcadena desde la segunda hasta la quinta letra, es decir, Hola
``` python
print("Hola, mundo!"[1:5])
```
- En la linea 24 obtenemos la subcadena desde la sexta hasta el final de la cadena, es decir, mundo!
``` python
print("Hola, mundo!"[6:])
```
- En la linea 35 obtenemos la subcadena desde la primera hasta la penultima letra, es decir, Hola, mund
``` python
print("Hola, mundo!"[:-2])
```
