cadena = "  "
cadena = cadena.strip()
if not cadena:
    #cargo la cadena con una frase en minuscula.
    cadena = "esto se va a mostrar en mayuscula"
    print(cadena.upper())
else:
    print("Tiene contenido la cadena.")