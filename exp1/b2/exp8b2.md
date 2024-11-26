# programa 8: promedio de calificaciones y determinar si el alumno aprobo o no
## Fecha de elaboracion: 2024/10/25
### Elaborado por: Edgar Alejandro Esparza Reyes
- De la linea 5 hasta la 9 se le solicito al usuario digitar 5 calificaciones con diferentes inputs, siendo guardados los valores en 5 variables diferentes como `cal1`, `cal2`, `cal3`, `cal4` y `cal5`
``` python
cal1 = int(input("digite su primer calificacion: "))
cal2 = int(input("digite su segunda calificacion: "))
cal3 = int(input("digite su tercer calificacion: "))
cal4 = int(input("digite su cuarta calificacion: "))
cal5 = int(input("digite su quinta calificacion: "))
```
- usamos un parentesis para realizar la suma de las 5 variables anteriores y ese total lo dividimos entre 5 para obtener el promedio, que fue guardado en la variable `prom`
``` python
prom = (cal1 + cal2 + cal3 + cal4 + cal5)/5
```
- Usando la condicional `if` comparamos la variable `prom` con el numero 70, si este es mayor o igual a 70 entonces se mostrara un mensaje de aprobacion y con una coma concatenamos la cadena y mostramos el promedio
``` python
if(prom >=70):
    print("El alumno aprobo con un promedio de", prom)
```
- Si la anterior condicional no se cumple se da por hecho que el alumno no consiguio 70 puntos, por lo que con un `else` mostraremos un mensaje donde indicaremos que el alumno reprobo y concatenaremos la variable `prom`
``` python
else:
    print("El alumno reprobo con un promedio de", prom)
```
