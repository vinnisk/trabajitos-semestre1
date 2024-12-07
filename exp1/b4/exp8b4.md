# programa 8: Ciclo `while`  
## Fecha de elaboración: 2024/11/7  
### Elaborado por: Edgar Alejandro Esparza  

---

### **Descripción del programa**  
Este programa utiliza un ciclo `while` para imprimir los números del 1 al 10, incrementando en cada iteración el valor de una variable de control.  

---

### **Explicación del código**  

1. **Línea 4**: Se inicializa una variable `i` con el valor `1`. Esta variable actúa como un contador y controlará las iteraciones del ciclo.  
   ```python
   i = 1
   ```

2. **Línea 6-8**:  
   - Se establece un ciclo `while` que continuará ejecutándose mientras el valor de `i` sea menor o igual a `10`.  
   - Dentro del ciclo:  
     - Se imprime el valor actual de `i`.  
     - Luego, el valor de `i` se incrementa en `1` usando el operador de suma compuesta (`i += 1`).  
   ```python
   while i <= 10:
       print(i)
       i += 1
   ```

3. **Línea 9**: Cuando la condición del ciclo deja de cumplirse (es decir, cuando `i` supera el valor `10`), se ejecuta la siguiente línea de código, que imprime el mensaje final:  
   ```python
   print("final del programa")
   ```
