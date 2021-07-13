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

"""-------------Menu-------------"""
#creo lista de 120 elementos
lista_numero_random=generador_lista_aleatoria(120)
#
mostrar_lista(lista_numero_random)