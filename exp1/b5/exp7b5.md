# Programa 7: Ejemplo `def` 2  
## Fecha de elaboración: 2024/11/14  
### Elaborado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa es una variación de un programa previo, pero incorpora una nueva característica: **repetir un conjunto de cálculos un número determinado de veces**.  
En cada iteración, los valores de entrada (`num1`, `num2` y `dec`) se duplican, y los resultados de las operaciones se imprimen.

---

### **Explicación del código**  

1. **Definición de la función `ope`**  
   - **Líneas 5-15**:  
     La función `ope` realiza las mismas operaciones básicas que en el programa previo:
     - Suma.  
     - Resta.  
     - Multiplicación.  
     - División (formateada según el número de decimales indicado).  
     - Módulo.  
     Cada operación se imprime utilizando *f-strings*.  

     Ejemplo:  
     ```python
     def ope(num1, num2, dec):
         suma = num1 + num2
         resta = num1 - num2
         mult = num1 * num2
         div = (num1 / num2)
         mod = num1 % num2
         print(f'la suma de {num1} + {num2} es: {suma}\n')
         print(f'la resta de {num1} - {num2} es: {resta}\n')
         print(f'la multiplicacion de {num1} * {num2} es: {mult}\n')
         print(f'la division de {num1} / {num2} es: {div:.{dec}f}\n')
         print(f'el modulo es de {num1} % {num2} es: {mod}\n')
     ```

2. **Solicitud de datos al usuario**  
   - **Línea 17**:  
     El usuario indica cuántas veces desea ejecutar los cálculos (`oas`). Este número es convertido a entero.
     ```pytnon
     oas = int(input("Digite la cantidad de veces que desea ejecutar el programa: "))
     ```
   - **Líneas 19-21**:  
     El programa solicita tres entradas adicionales:  
     ```python
     num1 = int(input("Digite el primer número: \n"))
     num2 = int(input("Digite el segundo número: \n"))
     dec = int(input("Ingrese la cantidad de decimales a mostrar en la división: \n"))
     ```
     Estos valores serán utilizados en la primera ejecución de los cálculos.  

3. **Bucle `for` para repetir el programa**  
   - **Línea 22-26**:  
     Se utiliza un bucle `for` para repetir los cálculos tantas veces como indicó el usuario (`oas`).  
     Dentro del bucle:  
     - La función `ope` es llamada con los valores actuales de `num1`, `num2` y `dec`.  
     - Después de cada iteración, los valores de `num1`, `num2` y `dec` se duplican:  
       ```python
       for _ in range(oas):
         ope(num1, num2, dec)
         num1 = num1 * 2
         num2 = num2 * 2
         dec = dec * 2
       ```  
