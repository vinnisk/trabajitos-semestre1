# programa 5: que calcule el nivel de desempeño de un estudiante respecto con su calificacion dada por el usuario
# Fecha de elaboracion: 2024/10/29
# Elaborado por: Edgar Alejandro 

ing = int(float("Digite su calificacion: "))

if ing <= 70:
    print("patetico, date de baja")
elif ing <= 79:
    print("Rendimiento deplorable, pero podras redimirte en el futuro")
elif ing <= 89:
    print("Tus resultados son pateticos, pero sientete feliz de saber que pudo haber sido peor")
elif ing <= 95:
    print("No dire nada excepto en que tu deberias ser el estandar, buen trabajo")
elif ing > 96 and ing <= 100:
    impue = ing * 0.15
    print("Lo lograste, una calificacion practicamente perfecta, unicamente por detras de mi.")

print("gracias por usar")


