# programa 1: else + if
## Fecha de elaboracion: 2024/10/28
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 5 es una variable donde se guardo la cadena "hamster
``` python
nombre = "hamster"
```
- La linea 7 es un condicional `if` donde se pregunta si "perro" esta dentro de la variable `nombre`, si se cumple entonces se mostrara el mensaje "es un perro".
``` python
if "perro" in nombre:
    print("Es un perro")
```
- La condicional `elif` es un else que al mismo tiempo puede hacer una pregunta como un `if`, en el cual preguntamos si "gato" esta en `nombre`, si se cumple entonces se imprimira el mensaje de "es un gato"
``` python
elif "gato" in nombre:
    print("Es un gato")
```
- Si ninguna de las condiciionales se cumplen entonces se imprimira el mensaje "mascota desconocida" con un `else`, ya que no queremos agregar otra pregunta, y solo añadimos un `print` con mensaje de despedida
``` python
else:
    print("Mascota desconocida.")
print("gracias por usar el programa")
```

