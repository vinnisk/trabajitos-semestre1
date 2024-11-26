# programa 5: solicitar dos numeros para realizar operaciones aritmeticas
## Fecha de elaboracion: 2024/10/14
### Elaborado por: Edgar Alejandro Esparza Reyes

- Las lineas 4 y 5 sin un par de `input` que guardaran todo en las variables `num1` y `num2`. y ambos se convertiran en numeros `float` para poder hacer operaciones aritmeticas
``` python
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
```
- de la linea 6 a la 9 se usaron las variables anteriores para hacer diferentes operaciones, como la suma `+`, resta `-`, multiplicacion `*` y division `/` y los resultados fueron guardados en sus respectivas variables
``` python
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
```
- Las lineas 10 a la 13 son una serie de prints donde se muestran los resultados son mostrados en una serie de prints, concatenando las variables anteriores no sin antes convertirlas en `string` para hacer posible la concatenacion
``` python
print("El valor de la suma: " + str(suma))
print("El valor de la resta: " + str(resta))
print("El valor de la multiplicación: " + str(mult))
print("El valor de la división: " + str(div))
```
