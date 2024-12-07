# programa 7: Filtro de edades  
## Fecha de elaboración: 2024/11/7  
### Elaborado por: Edgar Alejandro Esparza Reyes  

---

### **Descripción del programa**  
Este programa clasifica una lista de edades en tres categorías:  
1. Personas menores de 18 años.  
2. Personas entre 18 y 65 años.  
3. Personas mayores de 65 años.  

---

### **Explicación del código**  

1. **Línea 5**: Se declara una lista llamada `edades`, que contiene un conjunto de edades representadas por números enteros.  
   ```python
   edades = [70, 78, 89, 90, 15, 50, 60, 22, 30, 41, 8, 12, 36]
   ```

2. **Línea 7-11**: Se declaran tres listas vacías:  
   - `menores_18`: Para almacenar las edades menores a 18 años.  
   - `adul`: Para almacenar las edades entre 18 y 65 años.  
   - `adul_65`: Para almacenar las edades mayores a 65 años.  
   ```python
   menores_18 = []
   adul = []
   adul_65 = []
   ```

3. **Línea 15-21**:  
   - Se utiliza un ciclo `for` para recorrer cada elemento de la lista `edades`.  
   - Para cada edad:  
     - Si es menor a 18, se añade a la lista `menores_18`.  
     - Si está entre 18 y 65 años (inclusivo), se añade a la lista `adul`.  
     - Si es mayor a 65, se añade a la lista `adul_65`.  

   ```python
   for edad in edades:
       if edad < 18:
           menores_18.append(edad)
       elif edad < 65:
           adul.append(edad)
       else:
           adul_65.append(edad)
   ```

4. **Línea 23-27**: Se imprimen las tres listas clasificadas con mensajes descriptivos:  
   ``` python
   print("\nLas edades menores a 18 años son: ", menores_18)
  
   print("\nLas edades entre 18 y 65 años son: ", adul)

   print("\nLas edades mayores a 65 años son: ", adul_65)
   ```
