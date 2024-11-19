#Parte 2
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