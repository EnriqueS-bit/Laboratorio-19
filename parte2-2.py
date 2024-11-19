#Parte 3
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