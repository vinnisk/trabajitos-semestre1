# programa 6: analizar los operadores de comparacion
## Fecha de elaboracion: 2024/10/24
### Elaborado por: Edgar Alejandro Esparza Reyes
Para entender el funcionammiento del programa debemos dividir cada caracter de la  palabra hamster, h=0, a=1, m=2, s=3, t=4, e=5, r=6. para los numeros negativos es lo mismo pero reversa, -1=6, -2=5, -3=4, etc
- Declaramos la variable word
``` python
word = "hamster"
```
- Como ya explique, el valor -1 es igual al  r, que es lo mismo que mostrara el print
``` python
print(word[-1])
```
- los `:` son un rango, que mostrara desde el valor 1 (a) hasta el valor -1 que es igual al 6, osea r, aunque este ultimo no se mostrara
``` python
print(word[1:-1])
```
- Igual que el anterior, mostrara cierta parte de la panntalla, pero esta vez desde el -3 o 4, y como no hay otro numero entonces mostrara el4 hasta el ultimo valor
``` python
print(word[-3:])
```
- Este es el opuesto al anterior, mostrando todo lo que este antes del valor 3
``` python
print(word[:3])
```
