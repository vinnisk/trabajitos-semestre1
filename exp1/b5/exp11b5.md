# programa 11: Numeros primos con ciclo while
## Fecha de elaboracion: 2024/11/15
### Elaborado por: Edgar Alejandro 
### **Explicación del código: Programa 11 - Números primos con ciclo `while`**  
Este programa combina la lógica para determinar si un número es primo con un ciclo `while` que permite al usuario repetir el proceso indefinidamente hasta que decida salir. La verificación de primalidad se realiza dentro de una función llamada `primo`.  

---

### **1. Definir la función `primo`**  
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

**Explicación**:  
1. **Verificar el rango**:  
   ```python
   if num >= 10 and num <= 99:
   ```
   - Evalúa si el número ingresado está entre 10 y 99.  
   - Si no cumple esta condición, muestra un mensaje y no realiza la verificación de primalidad.  

2. **Bucle `for` para verificar primalidad**:  
   ```python
   for i in range(2, num + 1):
       res = num % i
   ```
   - Itera desde `2` hasta el número ingresado (`num + 1` para incluir `num`).  
   - Calcula el residuo de la división de `num` entre cada valor de `i`.  

3. **Determinar si es primo o no**:  
   ```python
   if res == 0:
       print("Tu numero no es un numero primo")
       break
   else:
       print("Tu numero es un numero primo")
       break
   ```
   - Si el residuo (`res`) es `0`, el número no es primo, y se detiene el bucle con `break`.  
   - Si el residuo no es `0`, el número es considerado primo y el bucle también se detiene.  
   - Nota: Este enfoque es incorrecto, ya que la evaluación se detiene después de la primera iteración, lo que puede producir resultados erróneos.  

4. **Manejar el caso fuera de rango**:  
   ```python
   else:
       print("Tu numero no esta entre 10 y 99")
   ```
   - Si el número ingresado está fuera del rango de 10 a 99, muestra un mensaje correspondiente.  

---

### **2. Iniciar un ciclo `while` para repetir el programa**  
```python
i = 0
while i == 0:
    num = int(input("Digite un numero entre 10 y 99: "))
    primo(num)
    desi = input("Desea repetir el programa (digite 'salir' si no)?\n")
    decis = desi.lower()
    if decis == "salir":
```

**Explicación**:  
1. **Control del bucle con `i`**:  
   ```python
   i = 0
   while i == 0:
   ```
   - Establece un ciclo infinito controlado por la variable `i`.  

2. **Solicitar un número al usuario**:  
   ```python
   num = int(input("Digite un numero entre 10 y 99: "))
   primo(num)
   ```
   - Pide al usuario un número y lo convierte en entero usando `int()`.  
   - Llama a la función `primo` para evaluar si el número es primo.  

3. **Solicitar al usuario si desea continuar**:  
   ```python
   desi = input("Desea repetir el programa (digite 'salir' si no)?\n")
   decis = desi.lower()
   ```
   - Pregunta al usuario si desea repetir el programa.  
   - Convierte la entrada del usuario a minúsculas usando `lower()` para facilitar la comparación.  

4. **Salir del bucle si el usuario elige "salir"**:  
   ```python
   if decis == "salir":
   ```
   - Si el usuario escribe "salir", el programa sale del bucle y finaliza.  
