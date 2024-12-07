# programa 9: `break` y `continue`  
## Fecha de elaboración: 2024/11/8  
### Elaborado por: Edgar Alejandro Esparza Reyes  

---

### **Descripción del programa**  
Este programa demuestra el uso de las palabras clave `break` y `continue` en un ciclo `while`.  
- **`break`**: Termina el ciclo cuando se cumple una condición específica.  
- **`continue`**: Salta el resto del cuerpo del ciclo y pasa a la siguiente iteración.  

---

### **Explicación del código**  

#### **Ejemplo: `break`**  

1. **Línea 6**: Se inicializa la variable de control `i` con un valor de `1`.  
   ```python
   i = 1
   ```

2. **Línea 8-12**:  
   - Se utiliza un ciclo `while` que continúa mientras `i` sea menor o igual a `10`.  
   - En cada iteración, se imprime el valor actual de `i`.  
   - Si el valor de `i` es igual a `5`, se ejecuta el comando `break`, lo que termina inmediatamente el ciclo.  
   - Si no se cumple la condición, `i` se incrementa en `1` para continuar con la siguiente iteración.  

   ```python
   while i <= 10:
       print(i)
       if i == 5:
           break
       i += 1
   ```

3. **Línea 13**: Cuando el ciclo se interrumpe (al llegar a `i == 5`), se imprime el mensaje de finalización del programa.  
   ```python
   print("final del programa")
   ```
---

#### **Ejemplo: `continue`**  

1. **Línea 16**: Se reinicia la variable de control `i` con el valor `1`.  
   ```python
   i = 1
   ```

2. **Línea 18-23**:  
   - Se utiliza un ciclo `while` que continúa mientras `i` sea menor o igual a `10`.  
   - En cada iteración, se imprime el valor actual de `i`.  
   - Si `i` es igual a `5`, se incrementa `i` en `1` y se ejecuta el comando `continue`.  
     - Esto hace que el ciclo salte el resto del cuerpo de la iteración actual y pase directamente a la siguiente iteración.  
   - Para otros valores de `i`, simplemente se incrementa en `1` para continuar con la siguiente iteración.  

   ```python
   while i <= 10:
       print(i)
       if i == 5:
           i += 1
           continue
       i += 1
   ```

3. **Línea 24**: Cuando el ciclo termina (al llegar a `i > 10`), se imprime el mensaje de finalización del programa.  
   ```python
   print("final del programa")
   ```
