# programa 11: analizar los operadores de comparacion
## Fecha de elaboracion: 2024/10/18
### Elaborado por: Edgar Alejandro Esparza Reyes
Los gatos al lado de cada print contienen la respuesta a cada comparacion logica
- Las lineas de la 5 a la 8 son ejemplos de conectores logicos `==` donde si alguno de los elementos no es estrictamente igual al elemento con el que se compara dara como resultado un `False`, en caso de que en verdad sean iguales entonces dara como resultado un `True`
```  python
print("operador ==")
print(5 == 7) #respuesta false
print(5 == 5) #respuesta true
print(5.0 == 5, "\n") #respuesta true
```
- Las lineas de la 10 a la 13 son los conectores logicos `!=` donde ninguno de los elemenntos comparados debe ser igual, de serlo el resultado sera `False`, cualquier otro caso es `True`
``` python
print("operador !=")
print(5 != 7) #respuesta true
print(5 != 5) #respuesta false
print(5.0 != 5, "\n") #respuesta false

```

- Las lineas de la 15 a la 18 son ejemplos de mayor que o `>`, donde el elemento comparado debe ser mayor al elemento con el que se le compara, si no lo es entonces dara como resultado un `False`, en cualquier otro caso resultara como `True`
```  python
print("operador >")
print(5 > 7) #respuesta false
print(5 > 5) #respuesta false
print(5.0 > 5, "\n") #respuesta false
```
- Las lineas de la 20 a la 23 son ejemplos del menor que o `<`, donde el elemento comparado debe ser menor al elemento con el que se le compara, de lo contrarui el resultado sera un `False`,pero si en verdad es menor entonces el resultado sra `True`
```  python
print("operador <")
print(5 < 7) #respuesta true
print(5 < 5) #respuesta false
print(5.0 < 5, "\n") #respuesta false
```
- Las lineas de la 25 a la 28 son ejemplos de mayor o igual que o `>=`, donde el elemento comparado debe ser mayor o igual al elemento con el que se le compara, si no lo es entonces dara como resultado un `False`, en cualquier otro caso resultara como `True`
```  python
print("operador >=")
print(5 >= 7) #respuesta false
print(5 >= 5) #respuesta true
print(5.0 >= 5, "\n") #respuesta true
```
- Las lineas de la 30 a la 33 son ejemplos del menor o igual que o `<=`, donde el elemento comparado debe ser menor o igual al elemento con el que se le compara, de lo contrarui el resultado sera un `False`,pero si en verdad es menor entonces el resultado sra `True`
```  python
print("operador <=")
print(5 <= 7) #respuesta true
print(5 <= 5) #respuesta true
print(5.0 <= 5) #respuesta true
```
