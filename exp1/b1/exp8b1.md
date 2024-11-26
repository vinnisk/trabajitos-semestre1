# programa 8: Calcular los minutos, horas y meses.
## Fecha de elaboracion: 2024/10/16
### Elaborado por: Edgar Alejandro Esparza Reyes
- En la linea 4 se soolicitara una cantidad de dias al usuario y se guardara en la variable del mismo nombre, `dias` y se convertira en una variable entera `int`
``` python
dias = int(input("digite el numero de dias:"))
```
- En la linea 6 se multiplico la cantidad de dias por 24 ya que esta es la cantidad de horas por dia, y el resultado fue guardado en la variable `horas` para saber la cantidad de horas que hay en la cantidad de dias que se digitaron
``` python
horas = dias * 24
```
- En la linea 7 se multiplico la variable `horas` por 60 ya  que esta es la cantidad de minutos que hay en cada hora y fue guardado en la variable `minutos` para asi saber la cantidad de minutos que hay en la cantidad de dias que se digitaron
``` python
minutos = horas * 60
```
- Finalmente, en la variable 8, la variable `dias` se dividio entre 30, ya que este es el promedio de dias en un mes, asi sabriamos cuantos meses se conforman en la cantidad de dias que se digitaron, esto fue guardado en la variable `meses`
``` python
meses = dias / 30
``` 
- Para finalizar el programa, de la variable 10 a la 12 son prints para mostrar en pantalla los resultados anteriores.
``` python
print("la cantidad de horas que hay en " + str(dias) + " es: " + str(horas))
print("la cantidad de minutos que hay en " + str(dias) + " es: " + str(minutos))
print("la cantidad de meses que son " + str(dias) + " son: " + str(meses))
``` 
