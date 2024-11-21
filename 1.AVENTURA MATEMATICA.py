print("----- Aventura Matemática: ¡A por el tesoro, Jack!🏝️🏴‍☠️ -----")
nivel = 1
archivo = open("puntos.txt", "w")
while nivel > 0 and nivel < 11:
    try:
        match nivel:
            case 1:
                print("\n🗺️ NIVEL 1: La Isla del Tesoro")
                print("\nJack, el pirata, ha llegado a la Isla del Tesoro, pero la entrada al escondite está bloqueada por una puerta con un candado. \nPara abrirlo, necesita resolver un problema matemático.")
                print("¿Cuánto es 15 + 3 x 4 - 8?")
                resultado1 = int(input("🚩 Ingrese el resultado: "))

                if (resultado1 != 0 and resultado1 != 19):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado1 = int(input("🚩 Ingrese el resultado: "))
                if (resultado1 == 19):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 1: 10 PUNTOS\n")
                elif (resultado1 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 2:
                print("\n🗺️ NIVEL 2: El Bosque Enigmático")
                print("\nJack se adentra en un bosque lleno de acertijos. Un mapa le indica que el cofre está escondido detrás de un árbol con un número específico de hojas.")
                print("Hay 24 hojas en el árbol. Si se caen 1/4 de las hojas, ¿cuántas hojas quedan en el árbol?")
                resultado2 = int(input("🚩 Ingrese el resultado: "))

                if (resultado2 != 0 and resultado2 != 18):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado2 = int(input("🚩 Ingrese el resultado: "))
                if (resultado2 == 18):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 2: 10 PUNTOS\n")
                elif (resultado2 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 3:
                print("\n🗺️ NIVEL 3: El Río de las Multiplicaciones")
                print("\nJack llega a un río donde tiene que cruzar en un pequeño bote. Para que el bote no se hunda, necesita calcular el peso máximo que puede soportar.")
                print("El bote puede soportar 50 kg. Jack pesa 35 kg y lleva un cofre que pesa 10 kg. ¿Cuántos kilos más puede cargar el bote?")
                resultado3 = int(input("🚩 Ingrese el resultado: "))

                if (resultado3 != 0 and resultado3 != 5):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado3 = int(input("🚩 Ingrese el resultado: "))
                if (resultado3 == 5):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 3: 10 PUNTOS\n")
                elif (resultado3 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 4:
                print("\n🗺️ NIVEL 4: La Cueva de las Restas")
                print("\nJack llega a una cueva oscura donde debe resolver un enigma para encontrar el cofre.")
                print("El cofre se encuentra a 12 pasos de la entrada. Jack ya ha dado 5 pasos. ¿Cuántos pasos más tiene que dar?")
                resultado4 = int(input("🚩 Ingrese el resultado: "))

                if (resultado4 != 0 and resultado4 != 7):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado4 = int(input("🚩 Ingrese el resultado: "))
                if (resultado4 == 7):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 4: 10 PUNTOS\n")
                elif (resultado4 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 5:
                print("\n🗺️ NIVEL 5: La Montaña de las Sumas")
                print("\nJack debe escalar una montaña para llegar al cofre. Cada escalón representa una suma.")
                print("Jack sube 3 escalones, luego baja 1, sube otros 2 y finalmente baja 1. ¿Cuántos escalones ha subido en total?")
                resultado5 = int(input("🚩 Ingrese el resultado: "))

                if (resultado5 != 0 and resultado5 != 3):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado5 = int(input("🚩 Ingrese el resultado: "))
                if (resultado5 == 3):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 5: 10 PUNTOS\n")
                elif (resultado5 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 6:
                print("\n🗺️ NIVEL 6: La Playa de las Divisiones")
                print("\nJack llega a una playa donde el cofre está enterrado. Para saber dónde cavar, necesita dividir un número.")
                print("El mapa indica que el cofre se encuentra a 18 pasos de una roca gigante. Si se divide la distancia en 3 partes iguales, ¿cuántos pasos hay que dar en cada una de las 3 partes?")
                resultado6 = int(input("🚩 Ingrese el resultado: "))

                if (resultado6 != 0 and resultado6 != 6):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado6 = int(input("🚩 Ingrese el resultado: "))
                if (resultado6 == 6):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 6: 10 PUNTOS\n")
                elif (resultado6 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 7:
                print("\n🗺️ NIVEL 7: El Laberinto de las Fracciones")
                print("\nJack se encuentra en un laberinto con caminos que representan distancias. Debe elegir el camino correcto para llegar al cofre.")
                print("Jack tiene que elegir entre dos caminos: uno de 150 centímetros de distancia y otro de 1 metro de distancia. ¿Qué camino es más corto?")
                resultado7 = int(input("🚩 Ingrese el resultado: "))

                if (resultado7 != 0 and resultado7 != 1):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado7 = int(input("🚩 Ingrese el resultado: "))
                if (resultado7 == 1):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 7: 10 PUNTOS\n")
                elif (resultado7 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 8:
                print("\n🗺️ NIVEL 8: La Ciudadela de las Ecuaciones")
                print("\n Jack llega a una ciudadela con una puerta que solo se abre resolviendo una ecuación.")
                print("x + 5 = 12. ¿Cuál es el valor de x?")
                resultado8 = int(input("🚩 Ingrese el resultado: "))

                if (resultado8 != 0 and resultado8 != 7):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado8 = int(input("🚩 Ingrese el resultado: "))
                if (resultado8 == 7):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 8: 10 PUNTOS\n")
                elif (resultado8 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 9:
                print("\n🗺️ NIVEL 9: El Volcán de los Porcentajes")
                print("\nJack debe atravesar un volcán activo. Para evitar la lava, necesita calcular la distancia segura.")
                print("La distancia total hasta el cofre es de 100 metros. La lava cubre el 20% de la distancia. ¿Cuántos metros debe avanzar Jack para evitar la lava?")
                resultado9 = int(input("🚩 Ingrese el resultado: "))

                if (resultado9 != 0 and resultado9 != 80):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado9 = int(input("🚩 Ingrese el resultado: "))
                if (resultado9 == 80):
                    print("Resultado correcto ✔. PASASTE AL SIGUIENTE NIVEL ✨🤗")
                    print("Sumaste 10 puntos 🎇")
                    nivel = nivel + 1
                    archivo.write("NIVEL 9: 10 PUNTOS\n")
                elif (resultado9 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
            case 10:
                print("\n🗺️ NIVEL 10: Encontrar el tesoro final")
                print("\nJack ha superado todos los obstáculos y ha llegado al tesoro final. Pero para abrirlo, necesita resolver un problema matemático final.")
                print("El tesoro está protegido por una llave que se abre con un código de 3 dígitos. El código es la suma de los números de todos los cofres encontrados en los niveles anteriores.")
                print("19 + 18 + 5 + 7 + 3 + 6 + 1 + 7 + 80 = ?")
                resultado10 = int(input("🚩 Ingrese el resultado: "))

                if (resultado10 != 0 and resultado10 != 146):
                    print("Resultado incorrecto ❌. Intento de nuevo... ")
                    resultado10 = int(input("🚩 Ingrese el resultado: "))
                if (resultado10 == 146):
                    print("Resultado correcto ✔. AYUDASTE A JACK A LLEGAR AL FINAL ✨🤗")
                    archivo.write("NIVEL 10: 10 PUNTOS\n")
                    archivo.close()
                    print(f"¡FELICITACIONES! SUMASTE 100 PUNTOS🎇")
                    break
                elif (resultado10 == 0):
                    print("JACK TE ESPERA PRONTO...🏝️🏴‍")
                    break
    except ValueError:
        print("Error. Ingrese un valor numérico ❌")
