# programa 4: valoracion de ingresos
# Fecha de elaboracion: 2024/10/29
# Elaborado por: Edgar Alejandro Esparza Reyes

ing = int(float("Digite sus ingresos: "))

if ing <= 1000:
    impue = ing * 0.05
    print("Los impuestos a pagar son un total de: ", impue)
elif ing <=2500:
    impue = ing * 0.08
    print("Los impuestos a pagar son un total de: ", impue)
elif ing <=6000:
    impue = ing * 0.12
    print("Los impuestos a pagar son un total de: ", impue)
elif ing > 6000:
    impue = ing * 0.15
    print("Los impuestos a pagar son un total de: ", impue)
total = ing - impue
print("el total de tus ingresos sin los impuestos es: ", total)

print("gracias por usar")
