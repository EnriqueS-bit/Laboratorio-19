#Parte 1-2
numero=int(input("Ingrese un numero: "))
if numero>=0 and numero<10:
    print("El numero tiene 1 digitos")
elif numero>=10 and numero<100:
    print("El numeroes tiene 2 digitos")
elif numero>=100:
    print("El numeroes tiene 3 digitos")