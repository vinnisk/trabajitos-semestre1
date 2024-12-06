# programa 5: Patrones  
## Fecha de elaboración: 2024/11/5  
### Elaborado por: Edgar Alejandro Reyes  

---

### **Patrón para contar**  
- **Línea 6**: Se declara una lista llamada `letras` que contiene una serie de cinco elementos, cada uno representando una letra (`"a"`, `"b"`, `"c"`, `"d"`, `"e"`).  
  ```python
  letras = ["a", "b", "c", "d", "e"]
  ```

- **Línea 7**: Se inicializa una variable `cont` con valor `0`. Esta variable servirá como contador para contar los elementos de la lista.  
``` python
cont = 0
```

- **Línea 8 y 9**: Se utiliza un ciclo `for` que recorre cada elemento de la lista `letras`. Por cada iteración, se incrementa la variable `cont` en `1`. Esto permite contar la cantidad total de elementos en la lista.  
``` python
for letra in letras:
    cont += 1
```

- **Línea 9**: Al final del ciclo, se imprime el mensaje indicando la cantidad total de letras en la lista:  
  ```
  La lista "letras" tiene 5 letras
  ```

---

### **Patrón para suma**  
- **Línea 13**: Se declara una lista llamada `nums` que contiene una serie de cuatro números enteros (`100`, `200`, `300`, `400`).  
  ```python
  nums = [100, 200, 300, 400]
  ```

- **Línea 14**: Se inicializa una variable `sum` con valor `0`. Esta variable se usará para acumular la suma de los números en la lista.  
``` python
sum = 0

```

- **Línea 15 y 16**: Se utiliza un ciclo `for` que recorre cada elemento de la lista `nums`. Por cada iteración, se suma el valor del número actual a la variable `sum`.  
``` python
for num in nums:
    sum += num
```
- **Línea 17**: Al final del ciclo, se imprime el resultado de la suma total:  
  ```
  la sumatoria es  1000
  ```

---

### **Concatenando**  
- **Línea 20**: Se declara una lista llamada `pals` que contiene una serie de elementos que forman una frase: `"hoy"`, `" "`, `"hace"`, `" "`, `"frio"`.  
  ```python
  pals = ["hoy", " ", "hace", " ", "frio"]
  ```

- **Línea 21**: Se inicializa una variable `con` con una cadena vacía (`""`). Esta variable se usará para concatenar (unir) los elementos de la lista.  
```python
con = ""
```

- **Línea 22-23**: Se utiliza un ciclo `for` que recorre cada elemento de la lista `pals`. Por cada iteración, el elemento actual se añade al final de la cadena `con` utilizando el operador `+`.  
``` python
for pal in pals:
    con = con + pal
```

- **Línea 24**: Al final del ciclo, se imprime la cadena concatenada, que forma la frase completa:  
  ```
  hoy hace frio
  ```
