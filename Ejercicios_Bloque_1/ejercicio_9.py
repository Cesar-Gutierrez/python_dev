corte=False
salida=""

while not corte:
    numero=int(input("Ingrese un numero: "))
    if numero == 111:
        corte = True
    else:
        salida+=str(numero)+"\n"
else:
    print(f"Estos numeros ingreso hasta el corte: \n{salida}")