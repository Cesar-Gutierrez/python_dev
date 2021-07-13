import random
"""-------------Funciones-------------"""
def generador_lista_aleatoria(tamanio = 1):
    lista = []
    i=0
    while i < tamanio:
        lista.append(random.randint(1,30))
        i+=1
    return lista

def mostrar_lista(lista):
    i=1
    for elemento in lista:
        print(f"{i}){elemento}")
        i+=1

def buscador_elemento(lista):
    elemento_buscado = int(input("\nIngrese el numero que desee encontrar: "))
    if elemento_buscado in lista:
        print(f"El elmento {elemento_buscado} existe en la posicion {lista.index(elemento_buscado)}.")
    else:
        print(f"El elemento {elemento_buscado} no existe.")

"""-------------Menu-------------"""
lista_numero_random=generador_lista_aleatoria(8)
print("Lista de numeros:")
mostrar_lista(lista_numero_random)
lista_numero_random.sort()
print("\nLista ordenada: ")
mostrar_lista(lista_numero_random)
print(f"\nLa longitud de la lista es: {len(lista_numero_random)}")
buscador_elemento(lista_numero_random)