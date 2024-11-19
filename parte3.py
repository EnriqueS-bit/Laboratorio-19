#Parte 4

calificaciones={"Jose":5.0,"Juan":4.5,"Ana":4.2,"Luis":4.3}
print(calificaciones)
n = int(input("Ingrese la cantidad de estudiantes: "))
calificaciones = {}
for _ in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    calificaciones[nombre] = nota

#Encontrar la calificacion mas alta con "max"
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")

#Encontrar la calificacion mas baja con "min"
nombre_min = min(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más baja es {nombre_min} con una calificación de {calificaciones[nombre_min]}.")
