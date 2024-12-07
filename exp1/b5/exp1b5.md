# Programa 4: Ejemplo de función  
## Fecha: 13/11/2024  
### Realizado por: Edgar Alejandro  

---

### **Descripción del programa**  
Este programa introduce el concepto de funciones en Python mediante un ejemplo sencillo. Se define una función llamada `saludar` que toma un argumento y lo utiliza para generar un mensaje personalizado.

---

### **Explicación del código**  

1. **Definición de la función**  
   - **Línea 6 y 7**:  
     Se define la función `saludar` con un parámetro llamado `nombre`.  
     - El parámetro `nombre` permite que la función reciba datos al ser llamada.  
     - Dentro del cuerpo de la función, se utiliza una *f-string* para generar un mensaje personalizado que saluda al nombre proporcionado.  
     ```python
     def saludar(nombre):
         print(f"¡Hola, {nombre}!")
     ```  

2. **Llamadas a la función**  
   - **Líneas 10-12**:  
     La función `saludar` se invoca tres veces con diferentes argumentos:  
     - `"Edgar"`  
     - `"PEPE"`  
     - `"Choto"`  
     Cada llamada genera un mensaje que utiliza el valor pasado como argumento.  
     ```python
     saludar("Edgar")
     saludar("PEPE")
     saludar("Choto")
     ``` 
