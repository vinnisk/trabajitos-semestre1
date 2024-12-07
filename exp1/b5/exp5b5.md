# Programa 5: Parámetro y argumento  
## Fecha: 2024/11/13  
### Realizado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa demuestra cómo trabajar con funciones en Python que aceptan múltiples parámetros, mostrando cómo se utilizan argumentos para personalizar la ejecución y generar resultados específicos.

---

### **Explicación del código**  

1. **Definición de la función**  
   - **Línea 5**:  
     Se define la función `saludar` que acepta dos parámetros:  
     - `nombre`: Representa el nombre de la persona a quien se está saludando.  
     - `edad`: Representa la edad de la persona.  
     Dentro del cuerpo de la función, se utilizan *f-strings* para incluir los valores de los parámetros en mensajes personalizados.  
     ```python
     def saludar(nombre, edad):
         print(f"¡Hola, {nombre}!")
         print(f"Tienes {edad} años")
         print('¡Espero que te encuentres bien!')
     ```  

2. **Llamadas a la función**  
   - **Líneas 11-13**:  
     La función `saludar` se invoca tres veces con diferentes argumentos. Cada llamada pasa valores específicos para `nombre` y `edad`:  
     - `"Edgar", 26`  
     - `"PEPE", 18`  
     - `"Choto", 23`  
     Al ejecutarse, la función genera un mensaje personalizado basado en los argumentos proporcionados.  
     ```python
     saludar("Edgar", 26)
     saludar("PEPE", 18)
     saludar("Choto", 23)
     ```  
