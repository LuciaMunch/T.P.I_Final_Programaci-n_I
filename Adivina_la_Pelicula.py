import random

# Lista de películas y emojis asociados
peliculas = {
    "Titanic": "🚢💔🌊",
    "El Rey León": "🦁👑🌅",
    "Toy Story": "🤠🚀🧸",
    "Jurassic Park": "🦖🌴🚁",
    "Harry Potter": "⚡🧙‍♂️🦉",
    "Aladdin": "🧞🫖🕌",
    "Cars": "🚗⚡💨",
    "Buscando a nemo": "🐠🔍",
    "Frozen": "👸❄️⛄"
}

# Función para jugar
def jugar():
    # Selecciona una película aleatoria
    pelicula, emojis = random.choice(list(peliculas.items()))
    print("Adivina la película con estos emojis:", emojis)

    # Pide al usuario que adivine
    intento = input("Escribe el nombre de la película: ")

    # Verifica la respuesta
    if intento.lower() == pelicula.lower():
        print("¡Correcto, felicitaciones! 🎉")
    else:
        print(f"Incorrecto. La respuesta era '{pelicula}'.")

# Ciclo para jugar varias veces
def iniciar_juego():
    print("Bienvenido a 'Adivina la Película con Emojis' 🎬")
    while True:
        jugar()
        otra = input("¿Quieres jugar otra vez? (si/no): ")
        if otra.lower() != 'si':
            print("Gracias por jugar. ¡Hasta la próxima! 👋")
            break

# Inicia el juego
iniciar_juego()
