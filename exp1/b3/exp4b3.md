# programa 4: valoracion de ingresos
## Fecha de elaboracion: 2024/10/29
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 5 solicita los ingresos al usuario, guardandolos en la variable `ing` y lo convierte en tipo `float`
``` python
ing = float(input("Digite sus ingresos: "))
```
- La linea 7 consiste en un `if`, comparando el valor de la variable `ing` con el numero 1000, si este es menor o igual a este numero entonces el impuesto sera del 5%, haciendo una multiplicacion y mostrando el valor con un print
``` python
if ing <= 1000:
    impue = ing * 0.05
    print("Los impuestos a pagar son un total de: ", impue)
```
- La linea 10 consiste en un `elif`, comparando el valor de la variable `ing` con el numero 2500, si este es menor o igual a este numero entonces el impuesto sera del 8%, haciendo una multiplicacion y mostrando el valor con un print
``` python
elif ing <=2500:
    impue = ing * 0.08
    print("Los impuestos a pagar son un total de: ", impue)
```
- La linea 13 consiste en un `elif`, comparando el valor de la variable `ing` con el numero 6000, si este es menor o igual a este numero entonces el impuesto sera del 12%, haciendo una multiplicacion y mostrando el valor con un print
``` python
elif ing <=6000:
    impue = ing * 0.12
    print("Los impuestos a pagar son un total de: ", impue)
```
- La linea 16 consiste en un `elif`, comparando el valor de la variable `ing` con el numero 6000, si este es mayor a este numero entonces el impuesto sera del 15%, haciendo una multiplicacion y mostrando el valor con un print
``` python
elif ing > 6000:
    impue = ing * 0.15
    print("Los impuestos a pagar son un total de: ", impue)
```
- Para finalizar, restaremos el valor de los impuestos en la variable `impue` al valor de los ingresos de la variable `ing`, mostrando el total de  ingresos sin impuestos en un print, concatenando con una coma. y un ultimo print de despedida.
``` python
total = ing - impue
print("el total de tus ingresos sin los impuestos es: ", total)
print("gracias por usar")
```
