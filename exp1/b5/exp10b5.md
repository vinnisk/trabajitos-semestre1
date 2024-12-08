## Fecha de elaboracion: 2024/11/15
### Elaborado por: Edgar Alejandro 

### **Explicación del código: Programa 10 - Definir si un número es primo usando una función**  
Este programa encapsula la lógica para verificar si un número es primo en una función llamada `primo`. Además, verifica que el número esté en el rango de 10 a 99 antes de realizar la validación de primalidad.  

---

#### **1. Definir la función `primo`**  
```python
def primo(num):
    if num >= 10 and num <= 99:
        for i in range(2, num + 1):
            res = num % i
            if res == 0:
                print("Tu numero no es un numero primo")
                break
            else:
                print("Tu numero es un numero primo")
                break
    else:
        print("Tu numero no esta entre 10 y 99")
```

- **Definición de la función**:  
  - `primo(num)`: Toma como argumento un número entero `num`.  
  - Evalúa si el número está en el rango de 10 a 99. Si no lo está, muestra un mensaje indicando que no está en el rango.  
  - Si el número está en el rango, verifica si es primo dividiéndolo por los números desde `2` hasta `num`.  

---

#### **2. Verificar si el número está en el rango**  
```python
if num >= 10 and num <= 99:
```
- **Condición**:  
  - Verifica si el número ingresado está entre 10 y 99 (inclusive).  
  - Si cumple esta condición, el programa procede a verificar si el número es primo.  

---

#### **3. Iterar para evaluar divisibilidad**  
```python
for i in range(2, num + 1):
    res = num % i
```
- **Bucle `for`**: Recorre los números desde 2 hasta `num` (inclusive).  
- **Residuo de la división**: Calcula el residuo de la división de `num` entre `i` para determinar si es divisible.  

---

#### **4. Evaluar si el número es divisible**  
```python
if res == 0:
    print("Tu numero no es un numero primo")
    break
```
- **Condición**:  
  - Si `res` es igual a `0`, significa que el número es divisible por `i`.  
  - Esto indica que no es un número primo, ya que tiene divisores distintos de 1 y él mismo.  
  - Muestra el mensaje correspondiente y finaliza el bucle con `break`.  

---

#### **5. Confirmar que el número es primo**  
```python
else:
    print("Tu numero es un numero primo")
    break
```
- **Condición**:  
  - Si `res` no es igual a `0`, significa que `num` no es divisible por el número actual (`i`).  
  - En este caso, se asume que el número es primo y se muestra el mensaje correspondiente.  
  - El bucle termina con `break`, ya que se concluye que el número es primo.  

---

#### **6. Manejar el caso de un número fuera del rango**  
```python
else:
    print("Tu numero no esta entre 10 y 99")
```
- Si el número ingresado por el usuario no está entre 10 y 99, muestra un mensaje indicando que no está en el rango permitido.  

---

#### **7. Llamar a la función `primo`**  
```python
num = int(input("Digite un numero entre 10 y 99: "))
primo(num)
```
- **`input()`**: Solicita al usuario que ingrese un número.  
- **`int()`**: Convierte el dato ingresado en un número entero.  
- **Llamada a la función**: Se pasa el número ingresado como argumento a la función `primo`, que ejecuta la lógica explicada.
