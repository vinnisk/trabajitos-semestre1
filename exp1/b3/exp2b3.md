# programa 2: else + if 2
## Fecha de elaboracion: 2024/10/28
### Elaborado por: Edgar Alejandro Esparza Reyes
- Las lineas 5 y 6 son un par de inputs que guardaran numeros enteros `int` en las variables `num1` y `num2` respectivamente
``` python
num1 = int(input("ingrese numero uno:"))
num2 = int(input("ingrese numero dos:"))
```
- con una condicional `if` donde compararemos las dos variables, si `num1` es menor a `num2` entonces la condicional se cumplira y se mostrara un mensaje donde declare esta misma afirmacion 
``` python
if num1 < num2:
    print("el numero 1 es menor que el numero dos")
```
- La linea 10 y 11 consisten un `elif` donde se preguntara si ambos nummeros son iguales, si lo son entonces se mostrara un mensaje en pantalla afirmandolo
``` python
elif num1 ==  num2:
    print("ambos numeros son iguaes")
```
- Si ninguna de las condicionales anteriores se cumplen entonces por descarte el `num1` es mayor a `num2`, por lo que el `else` al ejecutarse mostrara un mensaje diciendo eso mismo
``` python
else:
    print("el numero 1 es mayor al numero 2")
```
