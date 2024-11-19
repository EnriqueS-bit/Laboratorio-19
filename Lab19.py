#Parte 1-1
numero=int(input("Ingrese un numero: "))
if numero%2==0:
    print("El numero es par")
else:
    print("El numeroes impar")

#Parte 1-2
numero=int(input("Ingrese un numero: "))
if numero>=0 and numero<10:
    print("El numero tiene 1 digitos")
elif numero>=10 and numero<100:
    print("El numeroes tiene 2 digitos")
elif numero>=100:
    print("El numeroes tiene 3 digitos")

#Parte 2-1
n=int(input("Cuantos empleados tiene la empresa:"))
x=1
sueldobajo=0
sueldoalto=0
gastos=0
while x <=n:
    print(f"Para el empleado {x} de {n}:")
    sueldo=float(input("Ingrese el sueldo:"))
    if sueldo<=3000000:
        sueldobajo=sueldobajo+1
    else:
        sueldoalto=sueldoalto+1 
    gastos=gastos+sueldo
    x=x+1 
print("La cantidad de empleados que gana menos de 3 millones es: ",sueldobajo)
print("La cantidad de empleados que ganan mas de 3 millones es: ",sueldoalto)
print("El gasto total es: ",gastos)

#Parte 2-2
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))
    if x>0 and y>0:
        cuadrante1=cuadrante1+1 
    elif x<0 and y>0:
        cuadrante2=cuadrante2+1 
    elif x<0 and y < 0:
        cuadrante3=cuadrante3+1 
    elif x>0 and y < 0:
        cuadrante4=cuadrante4+1 
print(f"Hay {cuadrante1} puntos en el primer cuadrante")
print(f"Hay {cuadrante2} puntos en el segundo cuadrante")
print(f"Hay {cuadrante3} puntos en el tercer cuadrante")
print(f"Hay {cuadrante4} puntos en el cuarto cadrante")

#Parte 3
calificaciones={"Jose":5.0,"Juan":4.5,"Ana":4.2,"Luis":4.3}
n = int(input("Ingrese la cantidad de estudiantes: "))
calificaciones = {}
for _ in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    calificaciones[nombre] = nota

nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")

nombre_min = min(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más baja es {nombre_min} con una calificación de {calificaciones[nombre_min]}.")