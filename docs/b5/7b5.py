# programa 7: ejemplo def 2
# Fecha de elaboracion: 2024/11/14
# Elaborado por: Edgar Alejandro

def ope(num1, num2, dec):
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = (num1 / num2)
    mod = num1 % num2
    print(f'la suma de {num1} + {num2} es: {suma}\n')
    print(f'la resta de {num1} - {num2} es: {resta}\n')
    print(f'la multiplicacion de {num1} * {num2} es: {mult}\n')
    print(f'la division de {num1} / {num2} es: {div:.{dec}f}\n')
    print(f'el modulo es de {num1} % {num2} es: {mod}\n')

oas = int(input("Digite la cantidad de veces que desea ejecutar el programa: "))

num1 = int(input("Digite el primer número: \n"))
num2 = int(input("Digite el segundo número: \n"))
dec = int(input("Ingrese la cantidad de decimales a mostrar en la división: \n"))
for _ in range(oas):
    ope(num1, num2, dec)
    num1 = num1 * 2
    num2 = num2 * 2
    dec = dec * 2
