# Programa 10: Operador `in` y `not in`  
## Fecha de elaboración: 2024/10/31  
### Elaborado por: Edgar Alejandro Esparza Reyes  

- **En la línea 3**, declaramos una lista llamada `nombres` que contiene tres elementos de tipo `string`:  
  ```python
  nombres = ["choto", "emilio", "Luis"]
  ```

- **En la línea 4**, usamos el operador `in` para verificar si el elemento `"Luis"` está en la lista `nombres`. El resultado será `True` porque `"Luis"` es uno de los elementos de la lista:  
  ```python
  print("Luis" in nombres)
  ```

- **En la línea 5**, usamos el operador `in` para verificar si el elemento `"emi"` está en la lista `nombres`. El resultado será `False` porque `"emi"` no coincide exactamente con ninguno de los elementos de la lista; las búsquedas con `in` son sensibles a coincidencias exactas:  
  ```python
  print("emi" in nombres)
  ```

- **En la línea 6**, usamos el operador `in` para verificar si el elemento `"javier"` está en la lista `nombres`. El resultado será `False` porque `"javier"` no está en la lista:  
  ```python
  print("javier" in nombres)
  ```

- **En la línea 7**, usamos el operador `not in` para verificar si el elemento `"jose"` no está en la lista `nombres`. El resultado será `True` porque `"jose"` efectivamente no se encuentra en la lista:  
  ```python
  print("jose" not in nombres)
  ```
