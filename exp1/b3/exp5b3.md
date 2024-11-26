# programa 5: que calcule el nivel de desempeño de un estudiante respecto con su calificacion dada por el usuario
## Fecha de elaboracion: 2024/10/29
### Elaborado por: Edgar Alejandro 
- La linea 5 consiste en un input que solicita una calificacion y la guarda en la variable `ing`
``` python
ing = float(input("Digite su calificacion: "))

```
- La linea 7 es una condicional if que compara la variable `ing` con el numero 70, si la variable es menor o igual a este numero aparecera un mensaje de motivacion
``` python
if ing <= 70:
    print("patetico, date de baja")
```
- La linea 9 es una condicional `elif` que compara la variable `ing` con el numero 79, si la variable es menor o igual a este numero aparecera un mensaje de motivacion
``` python
elif ing <= 79:
    print("Rendimiento deplorable, pero podras redimirte en el futuro")
```
- La linea 11 es una condicional `elif` que compara la variable `ing` con el numero 89, si la variable es menor o igual a este numero aparecera un mensaje de aprovacion
``` python
elif ing <= 89:
    print("Tus resultados son pateticos, pero sientete feliz de saber que pudo haber sido peor")
```
- La linea 13 es una condicional `elif` que compara la variable `ing` con el numero 95, si la variable es menor o igual a este numero aparecera un mensaje de felicitacion
``` python
elif ing <= 95:
    print("No dire nada excepto en que tu deberias ser el estandar, buen trabajo")
```
- La linea 15 es una condicional `elif` que compara la variable `ing` con el numero 100, si la variable es menor o igual a este numero aparecera un mensaje de felicitacion
``` python
elif ing <= 100:
    impue = ing * 0.15
    print("Lo lograste, una calificacion practicamente perfecta, unicamente por detras de mi.")
print("gracias por usar")
```
