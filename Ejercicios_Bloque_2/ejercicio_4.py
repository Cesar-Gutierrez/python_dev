lista = [1,2,3,4]
entero = 15
booleana = True
cadena = "hola soy una cadena"

soy_de_tipo = lambda variable : f"Es de tipo: {type(variable).__name__}"

print(soy_de_tipo(lista))
print(soy_de_tipo(entero))
print(soy_de_tipo(booleana))
print(soy_de_tipo(cadena))