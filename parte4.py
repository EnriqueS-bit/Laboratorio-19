estudiantes = {
    "Juan": 5.0,
    "Ana": 4.2,
    "Luis": 4.5,
    "Pablo":3.5
}
nombre=input("Ingresa el nombre del estudiante: ")
calificaciones=float(input("Ingrese la calificacion: "))
if nombre in estudiantes:
    estudiantes[nombre]=calificaciones
else:
    estudiantes[nombre]=calificaciones
print("Informacion de estudiantes")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre} tiene una calificacion de {calificaciones}")
print(estudiantes)