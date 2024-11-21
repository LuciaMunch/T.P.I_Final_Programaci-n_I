import random

# Función para obtener una palabra aleatoria de una lista de palabras
def obtener_palabra():
    palabras = ["python", "programacion", "ahorcado", "juego"]
    return random.choice(palabras)

# Función para mostrar el estado actual de la palabra adivinada
def mostrar_estado(palabra_secreta, letras_adivinadas):
    estado_actual = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    print(f"Palabra: {estado_actual}")

# Función principal del juego de ahorcado
def jugar_ahorcado():
    palabra_secreta = obtener_palabra()  # Obtiene una palabra aleatoria
    letras_adivinadas = []  # Lista para almacenar las letras adivinadas correctamente
    letras_incorrectas = []  # Lista para almacenar las letras adivinadas incorrectamente
    intentos = 0  # Contador de intentos fallidos
    max_intentos = 6  # Número máximo de intentos permitidos

    # Bucle principal del juego
    while intentos < max_intentos:
        mostrar_estado(palabra_secreta, letras_adivinadas)  # Muestra el estado actual de la palabra
        # Verifica si el jugador ha adivinado toda la palabra
        if "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]) == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra.")
            return True
        letra = input("Adivina una letra: ").lower()  # Solicita al jugador que adivine una letra
        # Verifica si la letra ya ha sido adivinada
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)  # Añade la letra a la lista de letras adivinadas correctamente
        else:
            letras_incorrectas.append(letra)  # Añade la letra a la lista de letras incorrectas
            intentos += 1  # Incrementa el contador de intentos fallidos
            print(f"Letra incorrecta. Intentos fallidos: {intentos}")
            # Dibuja el ahorcado según los intentos fallidos
            if intentos == 1:
                print("""
                   -----
                   |   |
                   O   |
                       |
                       |
                       |
                    --------
                """)
            elif intentos == 2:
                print("""
                   -----
                   |   |
                   O   |
                   |   |
                       |
                       |
                    --------
                """)
            elif intentos == 3:
                print("""
                   -----
                   |   |
                   O   |
                  /|   |
                       |
                       |
                    --------
                """)
            elif intentos == 4:
                print("""
                   -----
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                    --------
                """)
            elif intentos == 5:
                print("""
                   -----
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                    --------
                """)
            elif intentos == 6:
                print("""
                   -----
                   |   |
                   O   |
                  /|\  |
                  / \  |
                       |
                    --------
                """)
                print(f"Perdiste. La palabra era: {palabra_secreta}")
                return False

    print(f"HAS PERDIDO. La palabra era: {palabra_secreta}")
    return False

# Función para cargar las puntuaciones desde un archivo
def cargar_puntuaciones():
    try:
        with open("puntuaciones.txt", "r") as archivo:
            lineas = archivo.readlines()
        puntuaciones = {linea.split(": ")[0]: int(linea.split(": ")[1]) for linea in lineas}
    except FileNotFoundError:
        puntuaciones = {}
    return puntuaciones

# Función para guardar las puntuaciones en un archivo
def guardar_puntuaciones(puntuaciones):
    with open("puntuaciones.txt", "w") as archivo:
        for nombre, puntuacion in puntuaciones.items():
            archivo.write(f"{nombre}: {puntuacion}\n")

# Función principal del programa
def main():
    nombre = input("Ingresa tu nombre: ")  # Solicita el nombre del jugador
    puntuaciones = cargar_puntuaciones()  # Carga las puntuaciones desde el archivo
    racha_maxima_guardada = puntuaciones.get(nombre, 0)  # Obtiene la racha máxima guardada para el jugador
    racha_actual = 0  # Inicializa la racha actual
    racha_maxima_sesion = 0  # Inicializa la racha máxima de la sesión
    while True:
        resultado = jugar_ahorcado()  # Juega una partida de ahorcado
        if resultado:
            racha_actual += 1  # Incrementa la racha actual si el jugador gana
            if racha_actual > racha_maxima_guardada:
                racha_maxima_guardada = racha_actual  # Actualiza la racha máxima guardada si la racha actual es mayor
                puntuaciones[nombre] = racha_maxima_guardada  # Guarda la nueva racha máxima en el diccionario de puntuaciones
                guardar_puntuaciones(puntuaciones)  # Guarda las puntuaciones en el archivo
            if racha_actual > racha_maxima_sesion:
                racha_maxima_sesion = racha_actual  # Actualiza la racha máxima de la sesión si la racha actual es mayor
        else:
            print(f"Victorias consecutivas en esta sesión: {racha_actual}")
            racha_actual = 0  # Reinicia la racha actual si el jugador pierde
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()  # Pregunta al jugador si quiere jugar de nuevo
        if jugar_de_nuevo != "s":
            break
    print(f"Gracias por jugar, {nombre}. Tu racha en esta sesión fue: {racha_maxima_sesion}")
    print(f"Tu racha más alta guardada es: {racha_maxima_guardada}")

# Ejecuta la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
