# programa 10: Revisar si puedes ver una pelicula en netflix. la condicion para esto es que seas mayor de edad u hayas comprado la pelicula
## Fecha de elaboracion: 2024/10/25
### Elaborado por: Edgar Alejandro
- En la linea 5 se le preguntara su edad al usuario y se guardara su respuesta en la variable `edad`
``` python
edad = int(input("Digite su edad: "))
```
- con una condicional `if` compararemos su edad con 18, si la condicional se cumple entonces iremos a la siguiente, de lo contrtario ira directamente al `else`
``` python
if edad >= 18:   
```
Dentro de la primer condicional se le preguntara al usuario si compro la pelicula, indicando que digite el numero como respuesta
``` python
  pel = int(input("La pelicula fue comprada \n 1.- si \n 2.- no\n"))
```
- Con otra condicional `if` nos aseguraremos que la  variable tenga el valor de 1, si lo hace mostraremos un mensaje para que se vea la pelicula, de lo contrario se ira al else
``` python
if pel == 1:
        print("Puedes ver la pelicula:")
```
- En la linea 11 hay un `else` que se activara en cuanto alguno de los dos ifs anteriores no se cumpla, este else mostrara un mensaje de negacion al momento de rentar la pelicula
``` python
else:
    print("No puedes ver la pelicula")
```


#### solucion 2
- Usando un `and` haremos dos preguntas con un solo if, siendo las mismas comparaciones que en la solucion anterior, que si cumple ambas podra rentar la pelicula, en caso de que alguna no lo haga entonces ira directamente al else
``` python
if edad >= 18 and pel == 1:
    print("Puedes ver la pelicula")
```
- El `else` al cumplirse mostrara un mensaje donde el usuario no puede rentar la pelicula, y para finalizar solo mostramos un mensaje de despedida
``` python
else:
    print("No puedes ver la pelicula")
print("gracias por usar")
```
