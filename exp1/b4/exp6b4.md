# programa 6: Lista de todos los números menores a 50  
## Fecha de elaboración: 2024/11/6  
### Elaborado por: Edgar Alejandro Reyes  

---

### **Descripción del programa**  
Este programa filtra una lista de números enteros y crea una nueva lista que contiene únicamente aquellos números que son menores a 50.  

---

### **Explicación del código**  

- **Línea 5**: Se declara una lista llamada `numeros` que contiene una serie de números enteros. Algunos de estos valores son menores a 50, mientras que otros no.  
  ```python
  numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 29]
  ```

- **Línea 6**: Se declara una lista vacía llamada `menores`. Esta lista se usará para almacenar los números que cumplan con la condición de ser menores a 50.  
  ```python
  menores = []
  ```

- **Línea 7-9**: Se utiliza un ciclo `for` para recorrer cada elemento de la lista `numeros`. Dentro del ciclo, hay una condición (`if`) que evalúa si el número actual (`numero`) es menor a 50:  
  - Si la condición es verdadera, el número se añade a la lista `menores` usando el método `.append()`.  
  - Los números mayores o iguales a 50 no se añaden a la nueva lista.  

  ```python
  for numero in numeros:
      if numero < 50:
          menores.append(numero)
  ```

- **Línea 10**: Se imprime la lista original, que incluye todos los números ingresados al programa.  
  ``` python
  print("La lista original es: ", numeros)
  ```

- **Línea 11**: Se imprime la nueva lista `menores`, que contiene únicamente los números menores a 50.  
  ``` python
  print("La lista nueva es: ", menores)
  ```
