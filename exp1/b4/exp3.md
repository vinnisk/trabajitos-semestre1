# programa 3: Función `range`  
## Fecha de elaboración: 2024/11/4  
### Elaborado por: Edgar Alejandro Esparza Reyes  

- **Línea 4**: Se declara una variable `x` utilizando la función `range()`. Esta genera una secuencia de números que, por defecto, comienza desde `0`, incrementa de uno en uno, y finaliza antes del número proporcionado como argumento. En este caso, la secuencia va del `0` al `9` (excluyendo el `10`).  
  ```python
  x = range(10)
  ```

- **Línea 5**: Al imprimir `x`, no se muestran los valores de la secuencia directamente, sino una representación de tipo `range`:
  ```python
  range(0, 10)
  ```

- **Línea 7-9**: El programa utiliza un ciclo `for` para recorrer la variable `x` e imprimir cada número de la secuencia generada por `range(10)`. Esto imprimirá los números del `0` al `9`.  
  ``` python
  print("Imprime los valores del 0 al 15")
  for num in x:
    print(num)
  ```
---

- **Línea 11**: Se imprime un mensaje indicando que se generará una nueva secuencia de números, ahora del `5` al `15` inclusive.
  ``` python
  print("imprime los valores del 5 al 15")
  ```

- **Línea 12**: Se declara una nueva variable `x1` con `range(5, 16)`. Aquí, el rango empieza desde `5` (inclusive) y termina en `16` (excluyendo el `16`), generando números del `5` al `15`.  
  ```python
  x1 = range(5, 16)
  ```

- **Línea 14 y 15**: Se utiliza un ciclo `for` para recorrer la secuencia de `x1` y mostrar los números del `5` al `15`.
  ```python
  for num in x1:
    print(num)
  ```

---

- **Línea 17**: Se imprime un mensaje indicando que se generará una secuencia de números pares desde el `10` al `20` inclusive.

- **Línea 18**: Se declara una nueva variable `x2` con `range(10, 21, 2)`. Aquí, se define un rango con un incremento personalizado (`step`) de `2`. Esto genera números desde `10` hasta `20` (incluido), avanzando de dos en dos.  
  ```python
  x2 = range(10, 21, 2)
  ```

- **Línea 19-20**: Se utiliza un ciclo `for` para recorrer e imprimir los números de la secuencia generada en `x2`.
  ```python
  for num in x2:
    print(num)
  ```
