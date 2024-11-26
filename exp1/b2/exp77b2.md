# programa 7: bar
## Fecha de elaboracion: 2024/10/24
### Elaborado por: Edgar Alejandro Esparza Reyes
- La linea 5 es un mensaje que le indica al usuario que debe ser mayor de edad para entrar al bar, mientras la linea 7 le pregunta al usuario su edad, guardadolo en la vaiable `edad` y lo convierte en un valor `int`
``` python
print("Nesecita ser mayor a 18 años para pasar al bar")
edad = int(input("ingrese su edad:"))
```
- En la linea 7 hay una condicional `if` que comparara la edad ingresada por el usuario con el numero 18, si `edad` es mayor o igual a este numero entonces se mostrara un mensaje de bienvenida
``` python
if (edad>=18):
    print("ingrese a enbriagarse")
```
- En caso de que la primer condicional `if` no se cumpliera el programa ejecutaria el codigo `else`, que solo se ejecuta cuando el `if` no se cumple, este `else` mostrara un mensaje de negacion de entrada
``` python
else:
    print("no entras")
```
