inicio=int(input("Ingrese el Primer numero: "))
fin=int(input("Ingrese el Segundo numero: "))

salida=""
for numero in range(inicio+1,fin):
    if numero % 2 != 0:
        salida+=str(numero)+"-"
else:
    print(f"La lista de impares entre {inicio} y {fin} son: {salida}")