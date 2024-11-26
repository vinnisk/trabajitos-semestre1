# programa 9: programa que calcule el costo total de un articulo si: + son 3 articulos o menos el precio unitario sera de 35, si es maypr sera 30
## Fecha de elaboracion: 2024/10/25
### Elaborado por: Edgar Alejandro
- En la linea 5 se solicito un numero de articulos al usuario y fue guardado en la variable `art`
``` python
art = int(input("digite el numero de articulos:  "))
```
- En la linea 7, usando una condicional `if` preguntamos si `art` es menor o igual a 3, en caso de que lo sea, en la linea 8 se le dara el precio fijo de 45 y el resultado de la multiplicacion sera cuardado en la variable `costo`
``` python
if art <= 3:
    costo = art * 45
```
- En caso de que la condicional anterior no se cummpliera, la linea 9 asume que la cantidad de articulos es mayor a tres, por lo que con un `else` se le dara un precio fijo de 35 a cada articulo y el resultado sera guardado en la variable `costo`
``` python
else:
    costo = art * 35
```
- En la  linea 11 se le mostrara el total al usuario concatenando la variable `costo` y en la linea 12 se mostrara un mensaje de despedida
``` python
print("El costo total es de:", costo)
print("gracias por usar el programa")
```
