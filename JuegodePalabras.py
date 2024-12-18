import random 

palabras = ["programacion", "desarrollo", "ingenieria", "universidad", "tecnologia", "computadora", "estudiante", "matematicas", "algoritmo"]

def desordenar_palabra(palabra):
    palabra_lista = list(palabra)
    random.shuffle(palabra_lista)
    return ''.join(palabra_lista)

def juegodepalabras():
    print("¡Bienvenido al juego de palabras!")
    print("Se te mostrará una palabra con las letras desordenadas, debes escribirla correctamente.")
    
    seguir_jugando = True

    while seguir_jugando:
        
        palabra_correcta = random.choice(palabras)
        palabra_desordenada = desordenar_palabra(palabra_correcta)

        print(f"\nLa palabra desordenada es: {palabra_desordenada}")
        
        intentos = 0
        adivinanza = None
        
        while adivinanza != palabra_correcta:
            adivinanza = input("Escribe la palabra correcta: ").lower()
            intentos += 1
            
            if adivinanza == palabra_correcta:
                print(f"¡Correcto! La palabra es '{palabra_correcta}'. Lo lograste en {intentos} intento(s).")
            else:
                print("Incorrecto. Inténtalo de nuevo.")
        
        respuesta = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if respuesta != "sí" and respuesta != "si":
            seguir_jugando = False
            print("¡Gracias por jugar! Hasta la próxima.")
            
juegodepalabras()
