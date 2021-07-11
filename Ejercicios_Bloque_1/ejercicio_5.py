inicio=int(input("Ingrese el Primer numero: "))
fin=int(input("Ingrese el Segundo numero: "))

salida=""
for numero in range(inicio,fin):
    salida+=str(numero)+"-"
else:
    print(salida+str(fin))