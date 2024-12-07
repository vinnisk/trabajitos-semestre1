# programa 12: Uso de `print(f"")`  
## Fecha de elaboración: 2024/12/8  
### Elaborado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa muestra cómo utilizar la funcionalidad de cadenas formateadas (*f-strings*) en Python para incluir variables en un mensaje de salida.  

---

### **Explicación del código**  

1. **Línea 4-6**: Se definen tres variables:  
   - **`nombre`**: Almacena un nombre como una cadena.  
     ```python
     nombre = "Edinguer"
     ```  
   - **`edad`**: Almacena un número entero que representa una edad.  
     ```python
     edad = 27
     ```  
   - **`cal`**: Almacena un número decimal que representa una calificación.  
     ```python
     cal = 93.8
     ```  

2. **Línea 7**:  
   - Se utiliza una *f-string* en la función `print()` para generar un mensaje que incluye las variables definidas anteriormente.  
   - La *f-string* permite insertar valores directamente dentro de la cadena utilizando `{}` como delimitadores, proporcionando una manera sencilla de formatear texto y variables en una sola línea.  
   ```python
   print(f"Nombre: {nombre}. edad: {edad}, Calificacion: {cal}")
   ```  
