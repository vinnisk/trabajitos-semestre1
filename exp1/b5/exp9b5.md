# programa 9: Numeros primos entre 10 y 99
## Fecha de elaboracion: 2024/11/15
### Elaborado por: Edgar Alejandro

### **Explicación del código: Programa 9 - Números primos entre 10 y 99**  
El programa verifica si un número ingresado por el usuario está en el rango de 10 a 99 y si es un número primo.  

---

#### **1. Solicitar el número al usuario**  
```python
num = int(input("Digite un numero entre 10 y 99: "))
```
- **`input()`**: Solicita al usuario que ingrese un número.  
- **`int()`**: Convierte el dato ingresado de texto a entero para que se pueda trabajar con él matemáticamente.  
- El número se almacena en la variable `num`.  

---

#### **2. Validar si el número está en el rango permitido**  
```python
if num >= 10 and num <= 99:
```
- Verifica si el número ingresado está entre 10 y 99 (inclusive).  
- **Condición**:  
  - Si el número cumple esta condición, ejecutará el bloque de código que sigue.  
  - Si no la cumple, se ejecutará el bloque del `else`.  

---

#### **3. Iterar para verificar divisibilidad (solo si está en rango)**  
```python
for i in range(2, num + 1):
```
- **`range(2, num + 1)`**: Genera una secuencia de números desde 2 hasta `num` (inclusive).  
- La variable `i` toma el valor de cada número en esta secuencia.  
- Este bucle se utiliza para verificar si `num` es divisible por algún número desde 2 hasta él mismo.  

---

#### **4. Calcular el residuo de la división entre `num` y `i`**  
```python
res = num % i
```
- Calcula el residuo de la división de `num` entre `i`.  
- **Propósito**: Determinar si `num` es divisible por `i`. Si el residuo es `0`, significa que `num` no es primo.  

---

#### **5. Evaluar si el número es divisible**  
```python
if res == 0:
    print("Tu numero no es un numero primo")
    break
```
- **Condición**:  
  - Si `res` es igual a `0`, el número no es primo, ya que es divisible por algún número distinto de 1 y él mismo.  
  - El programa muestra el mensaje correspondiente y termina el bucle con `break`, ya que no es necesario seguir evaluando.  

---

#### **6. Confirmar que el número es primo (bloque `else`)**  
```python
else:
    print("Tu numero es un numero primo")
    break
```
- **Condición**:  
  - Si `res` no es igual a `0`, significa que `num` no ha sido divisible por el número actual (`i`).  
  - En este caso, se asume que el número es primo y se muestra el mensaje correspondiente.  
  - El bucle termina con `break`, ya que se concluye que el número es primo.  

---

#### **7. Manejar el caso en que el número no esté en el rango**  
```python
else:
    print("Tu numero no esta entre 10 y 99")
```
- Este bloque se ejecuta si el número ingresado por el usuario no está en el rango de 10 a 99.  
- Se muestra un mensaje indicando que el número no está dentro del rango permitido.  
