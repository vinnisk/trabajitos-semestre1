# programa 4: Nombres de personajes  
## Fecha de elaboración: 2024/11/4  
### Elaborado por: Edgar Alejandro Esparza  

- **Línea 4**: Se declara una lista llamada `x` que contiene nombres de personajes como cadenas de texto. Sin embargo, hay un error de sintaxis: faltan comas entre algunos elementos, específicamente entre `"rak"` y `"ran"`, y entre `"ran"` y `"edhan"`. Esto hará que se interprete como una sola cadena, `"rakranedhan"`, en lugar de tres elementos separados.  
  
  ```python
  x = ["baam", "khun", "shibisu", "Zahard", "V", "arlene", "androssi", "rak", "ran", "edhan"]
  ```

- **Línea 5**: Al imprimir `x`, se mostrará la lista completa tal como está escrita en el código. Si no se corrige el error, el resultado será:  
  ```
  ['baam', 'khun', 'shibisu', 'Zahard', 'V', 'arlene', 'androssi', 'rakranedhan']
  ```
---

- **Línea 7 y 8**: Se utiliza un ciclo `for` para recorrer la lista `x`. La variable de control `i` toma cada elemento de la lista en orden y lo muestra junto con el mensaje `"el nombre es"`.  
``` python
for i in x:
    print("el nombre es", i)
```
