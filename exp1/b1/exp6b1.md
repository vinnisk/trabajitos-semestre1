# programa 6: Calcular el area de un triangulo
## Fecha de elaboracion: 2024/10/15
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 4 y 5 son un par de `input` que guardaran informacion en las variables `num1` y `num2`, convirtiendolos en tipos de datos `float`
``` python
num1 = float(input("Digite la base del triangulo: "))
num2 = float(input("Digite la altura del triangulo: "))
```
- La linea 6 es la formmula para conseguir el area de un triangulo, la variable `num1` reemplaza la base y la variable `num2` reemplaza la altura, y el resultado de esa operacion sera guardado en la variable `res`
``` python
res = num1 * num2 / 2
```
- La variable 8 es un `print` que muestra el resultado de la variable `res` convirtiendo esa variable en una de tipo `string`
``` python
print("El area del triangulo es: "+ str(res))
```
