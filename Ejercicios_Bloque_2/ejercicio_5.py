tabla=[
    {
        "nombre":"Accion",
        "lista_de_juegos": ["GTA","COD","Pugb"]
    },
    {
        "nombre":"Aventura",
        "lista_de_juegos": ["assins","crash","prince of persia"]
    },
    {
        "nombre":"Deporte",
        "lista_de_juegos": ["Fifa","Pro21","Moto GP"]
    }
]

for elemento in tabla:
    print(f"------------La categoria: {elemento['nombre']}------------\n")
    print("Contiene los siguientes juegos: ")
    for juego in elemento['lista_de_juegos']:
        print(f" {juego}")