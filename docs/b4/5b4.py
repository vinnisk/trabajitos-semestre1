# programa 5: Patrones
# Fecha de elaboracion: 2024/11/5
# Elaborado por: Edgar Alejandro Reyes

# patron para contar
letras = ["a", "b", "c", "d", "e"] 
cont = 0
for letra in letras:
    cont += 1
print("La lista \"letras\" tiene", cont, "letras")

# Patron para suma
nums = [100, 200, 300, 400]
sum = 0
for num in nums:
    sum += num
print("la sumatoria es ", sum)

# Concatenando
pals = ["hoy", " ", "hace", " ", "frio"]
con = ""
for pal in pals:
    con = con + pal
print(con)
