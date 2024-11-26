# programa 7: area y perimetro de un circulo
## Fecha de elaboracion: 2024/10/16
### Elaborado por: Edgar Alejandro Esparza Reyes

- En la linea 5 se le solicitara el radio de un circulo al usuario, cualquiera que este desee, y lo que se digite sera guardado en la variable `rad` y convertido en tipo `float`
``` python
rad = float(input("digite el radio:"))
```
- En la linea 7 utilizaremos la formula para conseguuir el area de un circulo, donde `rad` reemplazara al radio en dicha formula y el resultado sera  guardado  en la variable `area` (la doble multiplicacion "**" significa potencia)
``` python
area = 3.1416 * rad ** 2
```
- En la linea 8 utilizaremos una formula distinta para conseguir el perimmetro de un circulo, pero una vez mas `rad` ocupara el lugar del radio, y el resultado sera guardado en la variable `per`
``` python
per = 2 * 3.1416 * rad
```
- Las lineas 11 y 10 solo son prints concatenando las variables con los resultados, no sin antes convertir estas ultimas en variables tipo `string`
``` python
print("El area del circulo es: " + str(area))
print("El perimetro del circulo es: " + str(per))
```
