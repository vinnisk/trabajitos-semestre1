# **Programa 8: Def Calculadora**  
## Fecha de elaboración: 2024/11/14  
### Elaborado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa implementa una calculadora básica dentro de un bucle `while`. Permite realizar operaciones matemáticas como suma, resta, multiplicación, división y módulo. Además, duplica los valores de entrada en cada iteración y ofrece al usuario la opción de detener el programa al escribir "salir".  

---

### **Explicación del código**  

1. **Definición de la función `ope`**  
   - **Líneas 5-15**:  
     La función `ope` realiza cálculos básicos con dos números (`num1` y `num2`) y muestra los resultados. La división es formateada según la cantidad de decimales indicada por el usuario (`dec`).  
     Ejemplo de una llamada a la función:  
     ```python
     ope(10, 5, 2)
     ```
     Producción:  
     ```
     la suma de 10 + 5 es: 15
     la resta de 10 - 5 es: 5
     la multiplicacion de 10 * 5 es: 50
     la division de 10 / 5 es: 2.00
     la suma de 10 % 5 es: 0
     ```

2. **Solicitud de entradas al usuario**  
   - **Líneas 17-19**:  
     El programa solicita al usuario:  
     - `num1`: primer número.  
     - `num2`: segundo número.  
     - `dec`: número de decimales para mostrar en la división.  

3. **Bucle infinito controlado por el usuario**  
   - **Línea 20**:  
     Se utiliza un bucle `while` con una condición `i == 0` que asegura que el programa continúa ejecutándose hasta que el usuario decida detenerlo.  
   - **Dentro del bucle**:  
     - **Línea 21**: Se llama a la función `ope` con los valores actuales de `num1`, `num2` y `dec`.  
     - **Líneas 23-25**: Después de cada iteración, los valores de `num1`, `num2` y `dec` se duplican. Esto incrementa rápidamente los cálculos realizados en cada iteración.  
     - **Líneas 26-28**:  
       El programa solicita al usuario si desea continuar. Si el usuario escribe "salir", la palabra es convertida a minúsculas (`desi.lower()`), y se evalúa la condición para detener el bucle.  

4. **Interrupción del bucle**  
   - Si el usuario ingresa "salir", el programa termina.  
   - Si se ingresa cualquier otra palabra, el bucle continúa.  
