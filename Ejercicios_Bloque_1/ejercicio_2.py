salida = ""
for numero in range(1,121):
    if numero % 2 == 0:
        salida += str(numero)+","
else:
    print(salida)