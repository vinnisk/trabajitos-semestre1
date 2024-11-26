# programa 8: promedio de calificaciones y determinar si el alumno aprobo o no
# Fecha de elaboracion: 2024/10/25
# Elaborado por: Edgar Alejandro Esparza Reyes

cal1 = int(input("digite su primer calificacion: "))
cal2 = int(input("digite su segunda calificacion: "))
cal3 = int(input("digite su tercer calificacion: "))
cal4 = int(input("digite su cuarta calificacion: "))
cal5 = int(input("digite su quinta calificacion: "))

prom = (cal1 + cal2 + cal3 + cal4 + cal5)/5

if(prom >=70):
    print("El alumno aprobo con un promedio de", prom)
else:
    print("El alumno reprobo con un promedio de", prom)
