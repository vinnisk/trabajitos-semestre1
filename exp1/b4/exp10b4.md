# programa 10: Métodos `lower()` y `upper()`  
## Fecha de elaboración: 2024/11/8  
### Elaborado por: Edgar Alejandro Esparza  

---

### **Descripción del programa**  
Este programa demuestra el uso de los métodos de cadenas `upper()` y `lower()` en Python:  
- **`upper()`**: Convierte todos los caracteres alfabéticos de una cadena en mayúsculas.  
- **`lower()`**: Convierte todos los caracteres alfabéticos de una cadena en minúsculas.  

---

### **Explicación del código**  

1. **Línea 5**: Se declara una cadena de texto llamada `cadena` con el valor:  
   ```python
   cadena = "Python es un lenguaje de programacion"
   ```

2. **Línea 6**: Se imprime la cadena original para mostrarla en su estado inicial.  
   ```python
   print("\n", cadena)
   ```

3. **Línea 7**:  
   - Se aplica el método `upper()` a la cadena, lo que convierte todos los caracteres alfabéticos en mayúsculas.  
   - El resultado se almacena en la variable `cadenam`.  
   ```python
   cadenam = cadena.upper()
   ```

4. **Línea 8**: Se imprime la versión en mayúsculas de la cadena.  
   ```python
   print("\n", cadenam)
   ```

5. **Línea 9**:  
   - Se aplica el método `lower()` a la cadena, lo que convierte todos los caracteres alfabéticos en minúsculas.  
   - El resultado se almacena en la variable `cadenami`.  
   ```python
   cadenami = cadena.lower()
   ```

6. **Línea 10**: Se imprime la versión en minúsculas de la cadena.  
   ```python
   print("\n", cadenami)
   ```
