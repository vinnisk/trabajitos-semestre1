# programa 9: Numeros primos entre 10 y 99
# Fecha de elaboracion: 2024/11/15
# Elaborado por: Edgar Alejandro Esparza Reyes
num = int(input("Digite un numero entre 10 y 99: "))

if num >= 10 and num <= 99:
    for i in  range(2, num +1):
        res= num % i
        if res == 0:
            print("Tu numero no es un numero primo")
            break
        else:
            print("Tu numero es un numero primo")
            break
    
else:
    print("Tu numero no esta entre 10 y 99")
