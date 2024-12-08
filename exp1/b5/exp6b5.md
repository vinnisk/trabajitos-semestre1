# Programa 6: Operaciones  
## Fecha de elaboración: 2024/11/14  
### Elaborado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa realiza una serie de operaciones matemáticas básicas (*suma, resta, multiplicación, división* y *módulo*) entre dos números ingresados por el usuario. También incluye la funcionalidad de mostrar el resultado de la división con una cantidad personalizada de decimales.

---

### **Explicación del código**  

1. **Definición de la función `ope`**  
   - **Líneas 5-15**:  
     La función `ope` recibe tres argumentos:  
     - `num1`: Primer número.  
     - `num2`: Segundo número.  
     - `dec`: Cantidad de decimales a mostrar en el resultado de la división.  
     Dentro de la función:  
     - Se realizan las operaciones básicas (*suma, resta, multiplicación, división* y *módulo*).  
     - Los resultados se almacenan en variables (`suma`, `resta`, `mult`, `div`, `mod`).  
     - Finalmente, se imprimen los resultados utilizando *f-strings*, formateando la división con la cantidad de decimales indicada por el usuario.  

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
         print(f'la suma de {num1} % {num2} es: {mod}\n')    
     ```

2. **Solicitud de datos al usuario**  
   - **Líneas 17-19**:  
     El programa solicita tres entradas al usuario:  
     - `num1`: El primer número, convertido a entero usando `int()`.  
     - `num2`: El segundo número, también convertido a entero.  
     - `dec`: La cantidad de decimales que el usuario desea mostrar en el resultado de la división.  

     Ejemplo de solicitud:  
     ```python
     num1 = int(input("Digite el primer numero: \n"))
     num2 = int(input("Digite el segundo numero: \n"))
     dec = int(input("Ingrese la cantidad de decimalles a mostrar en el modulo: \n"))
     ```

3. **Llamada a la función `ope`**  
   - **Línea 20**:  
     Se llama a la función `ope`, pasando los valores ingresados por el usuario como argumentos:  
     ```python
     ope(num1, num2, dec)
     ```
