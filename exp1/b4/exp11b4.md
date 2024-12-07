# programa 11: Condicionales con ciclo `while`  
## Fecha de elaboración: 2024/11/8  
### Elaborado por: Edgar Alejandro Esparza Reyes  

---

### **Descripción del programa**  
Este programa solicita al usuario que introduzca una palabra en un ciclo interactivo. El ciclo continúa ejecutándose hasta que el usuario escriba la palabra *"salir"*.  

---

### **Explicación del código**  

1. **Línea 5**: Se inicializa una variable llamada `palabra` como una cadena vacía (`""`). Esto asegura que el ciclo `while` comience.  
   ```python
   palabra = ""
   ```

2. **Línea 6**:  
   - Se inicia un ciclo `while` que se ejecuta mientras el valor de `palabra` no sea igual a `"salir"`.  
   - Este es el control principal del programa: si el usuario escribe `"salir"`, el ciclo termina.  
   ```python
   while palabra != "salir":
   ```

3. **Línea 7**: Dentro del ciclo, el programa solicita al usuario ingresar un texto mediante la función `input()`. El mensaje le indica que debe escribir la palabra exacta *"salir"* para finalizar.  
   ```python
   palabra = input("ingrese la palabra \"salir\" para terminar el programa \n")
   ```

4. **Línea 8**: Imprime el texto ingresado por el usuario como confirmación.  
   ```python
   print("ingreso: ", palabra)
   ```

5. **Línea 9**:  
   - Se usa el método `lower()` para convertir el texto ingresado a minúsculas. Esto asegura que la comparación con `"salir"` no sea sensible a mayúsculas/minúsculas.  
   ```python
   palabra = palabra.lower()
   ```

6. Cuando el usuario finalmente ingresa la palabra `"salir"`, el ciclo se interrumpe y el programa continúa con la siguiente línea después del ciclo.  
  
7. **Línea 10**: Se imprime el mensaje de finalización del programa.  
   ```python
   print("fin del programa")
   ```
