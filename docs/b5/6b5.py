# programa 6: Operaciones
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
    print(f'la suma de {num1} % {num2} es: {mod}\n')    
num1 = int(input("Digite el primer numero: \n"))
num2 = int(input("Digite el segundo numero: \n"))
dec = int(input("Ingrese la cantidad de decimalles a mostrar en el modulo: \n"))
ope(num1, num2, dec)