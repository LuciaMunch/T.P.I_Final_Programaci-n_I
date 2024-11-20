import random


def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    victorias = 0
    derrotas = 0
    empates = 0

    while True: # Inicia un bucle infinito que permitirá jugar múltiples rondas.
        eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        if eleccion_usuario == 'salir': # si el usuario ingresa salir se termina el bucle
            break
        if eleccion_usuario not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue

        eleccion_maquina = random.choice(opciones)

        print(f"Tú eliges: {eleccion_usuario}")
        print(f"La máquina elige: {eleccion_maquina}")

        if eleccion_usuario == eleccion_maquina:
            print("¡Es un empate!")
            empates += 1
        elif (eleccion_usuario == 'piedra' and eleccion_maquina == 'tijera') or \
                (eleccion_usuario == 'papel' and eleccion_maquina == 'piedra') or \
                (eleccion_usuario == 'tijera' and eleccion_maquina == 'papel'):
            print("¡Ganaste!")
            victorias += 1
        else:
            print("¡Perdiste!")
            derrotas += 1

    # Resumen final
    print("\nResumen final:")
    print(f"Victorias: {victorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")


if __name__ == "__main__": # Verifica si el archivo se está ejecutando directamente.
    jugar()