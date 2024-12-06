# programa 1: Ciclo for
## Fecha de elaboracion: 2024/11/4
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 4 presenta una variable tipo `List`, llamada `lista` donde guardaremos unsa serie de 6 numeros enteros
``` python
lista = [10, 30, 40, 20, 35, 80]
```

- Las lines 6-10 presentan una serie de prints donde mostraran de forma individual los elementos de la variable `lista` (debido a la indexacion que empieza en 0, nuestro programa iniciara mostrando un 30 ya que iniciamos con un 1)
``` python
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
```

- para terminar, usamos un ciclo `for` con una variable de control que crecera en 1 con cada iteracion (el valor inicia desde 0) y se detenndra cuando no exista un elemento que contar en la variable `list`. el mismo ciclo muestra un `print(i)`, el cual mostrara cada elemento de forma individual de la variable `lista`
``` python
for i in lista:
    print(i)
```
