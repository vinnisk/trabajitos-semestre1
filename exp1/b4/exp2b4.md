# programa 2: Ciclo for con nombres  
## Fecha de elaboración: 2024/11/4  
### Elaborado por: Edgar Alejandro Esparza  

- **Línea 4**: Se declara una variable tipo `list` llamada `lista`, que contiene una serie de tres elementos de tipo `str` (cadenas de texto). En este caso, los elementos son nombres: `"Luiz"`, `"chuy"` y `"mauricio"`.  
  ```python
  lista = ["Luiz", "chuy", "mauricio"]
  ```

- **Línea 6**: Inicia un ciclo `for`, donde se utiliza una variable de control `i`. Esta variable recorrerá automáticamente cada uno de los elementos de la lista `lista` en orden.  

- **Línea 7**: Dentro del ciclo, se utiliza un `print()` que concatenará el texto `"el nombre es "` con el valor actual de `i`, mostrando un mensaje personalizado para cada elemento de la lista. Este mensaje se repetirá para cada nombre contenido en `lista`.  

  ```python
  for i in lista:
      print("el nombre es", i)
  ```
