# Programa 9: Igualdad de listas  
## Fecha de elaboración: 2024/10/31  
### Elaborado por: Edgar Alejandro Esparza Reyes  

- **En la línea 3**, declaramos una lista llamada `puntos` que contiene elementos de tipo `string`:  
  ```python
  puntos = ["10", "30", "20"]
  ```

- **En la línea 4**, declaramos otra lista llamada `puntos2` que contiene elementos de tipo `int`:  
  ```python
  puntos2 = [10, 30, 20]
  ```

- **En la línea 5**, declaramos una lista llamada `ordenados` que contiene elementos de tipo `int`, organizados en orden ascendente:  
  ```python
  ordenados = [10, 20, 30]
  ```

- **En la línea 6**, declaramos una lista llamada `puntos_texto`, que es idéntica a la lista `puntos` en contenido y tipo de datos (`string`):  
  ```python
  puntos_texto = ["10", "30", "20"]
  ```

- **En la línea 8**, usamos el operador de igualdad (`==`) para comparar las listas `puntos` y `puntos2`. El resultado será `False` porque aunque tienen los mismos valores, los tipos de los elementos son diferentes (`string` vs. `int`):  
  ```python
  print(puntos == puntos2)
  ```

- **En la línea 10**, comparamos `puntos` con `ordenados`. El resultado será `False` porque aunque los elementos son similares en valor (después de convertir a `int`), están en un orden diferente:  
  ```python
  print(puntos == ordenados)
  ```

- **En la línea 12**, comparamos `puntos` con `puntos_texto`. El resultado será `True` porque ambas listas tienen los mismos elementos, en el mismo orden y con el mismo tipo (`string`):  
  ```python
  print(puntos == puntos_texto)
  ```

- **En la línea 14**, usamos el operador de desigualdad (`!=`) para comparar `puntos` consigo misma. El resultado será `False` porque una lista siempre es igual a sí misma:  
  ```python
  print(puntos != puntos)
  ```

- **En la línea 16**, comparamos `puntos` con `ordenados` usando `!=`. El resultado será `True` porque las listas no son iguales debido al orden y tipo de los elementos:  
  ```python
  print(puntos != ordenados)
  ```

- **En la línea 18**, comparamos `puntos` con `puntos_texto` usando `!=`. El resultado será `False` porque ambas listas son iguales en contenido, orden y tipo de datos:  
  ```python
  print(puntos != puntos_texto)
  ```
