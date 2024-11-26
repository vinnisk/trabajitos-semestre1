# Programa 1.12 P/Probar las compuertas lógicas AND, OR
## Elaborado por: Edgar Alejandro Esparza Reyes
### Fecha: 2024/10/18
- Las lineas 6 y 9 las cuatro combinaciones posibles para la compuerta `or`, claro, solo teniendo dos variables booleanas, esta compuerta dara un resultado `True` siempre que uno de los elementos comparados sea `True`, en caso de que todos los elementos sean `False` entonces todos los resultados lo seran.
``` python
print("Compuerta OR")
print(False or False)
print(False or True)
print(True or False)
print(True or True)
```
- De la linea 11 a la 15 son ejemplos de la compuerta `and`, donde siempre que una de las variables comparadas sea `False` el resultado tambien sera de este tipo, unicamente sienndo diferente cuando todos los elementos comparados son `True`
``` python
print("\n compuerta AND")
print(False and False)
print(False and True)
print(True and False)
print(True and True)
```
