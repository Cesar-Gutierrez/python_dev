aprobados=0
desaprobados=0

for alumno_numero in range(1,16):
    nota=int(input(f"Ingrese la nota del alumno numero {alumno_numero}: "))
    if nota >= 7:
        aprobados+=1
    else:
        desaprobados+=1
else:
    print(f"Hay {aprobados} aprobados.-")
    print(f"Hay {desaprobados} desaprobados.-")