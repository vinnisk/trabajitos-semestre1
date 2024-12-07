# Programa 2: Funciones con números  
## Fecha de elaboración: 2024/11/13  
### Elaborado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa demuestra el uso de diversas funciones integradas de Python (*built-in functions*) que trabajan con números y realizan operaciones básicas como conversión de tipos, redondeo, sumas, y evaluaciones de valores.

---

### **Explicación del código**  

1. **Uso de `abs()`**  
   - **Línea 5**:  
     La función `abs()` calcula el valor absoluto de un número.  
     - Entrada: `-10`  
     - Salida: `10`  
     ```python
     print(abs(-10))  # Output: 10
     ```  

2. **Uso de `int()`**  
   - **Línea 7**:  
     La función `int()` convierte una cadena de texto que representa un número entero en un valor entero.  
     - Entrada: `"20"`  
     - Salida: `20`  
     ```python
     print(int("20"))  # Output: 20
     ```  

3. **Uso de `float()`**  
   - **Línea 9**:  
     La función `float()` convierte una cadena de texto que representa un número decimal en un valor de tipo flotante.  
     - Entrada: `"3.14"`  
     - Salida: `3.14`  
     ```python
     print(float("3.14"))  # Output: 3.14
     ```  

4. **Uso de `bool()`**  
   - **Línea 11**:  
     La función `bool()` evalúa un valor y devuelve `True` si el valor es *verdadero* (no cero), y `False` si el valor es *falso* (cero).  
     - Entrada: `0`  
     - Salida: `False`  
     ```python
     print(bool(0))  # Output: False
     ```  

5. **Uso de `round()`**  
   - **Línea 13**:  
     La función `round()` redondea un número flotante al entero más cercano.  
     - Entrada: `3.1416`  
     - Salida: `3`  
     ```python
     print(round(3.1416))
     ```  

6. **Uso de `sum()`**  
   - **Líneas 15-16**:  
     La función `sum()` calcula la suma de todos los elementos de una lista o un iterable.  
     - Entrada: `[1, 2, 3, 4, 5]`  
     - Salida: `15`  
     ```python
     num = [1, 2, 3, 4, 5]
     print(sum(num))  # Output: 15
     ```  
