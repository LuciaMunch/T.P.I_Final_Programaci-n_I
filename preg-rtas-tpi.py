def juego_preguntas_qatar2022():
    
    print("¡¡BIENVENIDOS A PREGUNTAS Y RESPUESTAS QATAR 2022!!")
    
    #Lista de preguntas
    preguntas=["¿QUÉ EQUIPO GANÓ EL MUNDIAL DE QATAR 2022?","QUÉ JUGADOR HIZO EL PRIMER GOL DE ARGENTINA EN LA FINAL?",
             "¿QUÉ JUGADOR FUÉ EL GOLEADOR DEL MUNDIAL DE QATAR 2022?",
             "¿QUIÉN FUE EL ÁRBITRO PRINCIPAL DE LA FINAL DEL MUNDIAL DE QATAR 2022?", 
             "¿CUÁNTOS PENALES ATAJÓ EMILIANO MARTINEZ DURANTE EL MUNDIAL DE QATAR 2022?" ]

    #Lista de respuestas correctas, usando números que corresponden a las opciones
    respuestas_correctas=[3,2,2,4,2]

    #Lista de opciones, cada sublista contiene las opciones para la pregunta correspondiente
    opciones=[["1)BRASIL","2)FRANCIA","3)ARGENTINA","4)ALEMANIA"], ["1)ÁNGEL DI MARÍA","2)LIONEL MESSI","3)JULIÁN ÁLVAREZ","4)LAUTARO MARTINEZ"],
          ["1)LIONEL MESSI","2)KYLIAN MBAPPÉ","3)OLIVIER GIROUD","4)JULIÁN ÁLVAREZ"],
          ["1)DANIELE ORSATO (ITALIA)","2)CÉSAR RAMOS (MÉXICO)","3)DANNY MAKKELIE (HOLANDA)","4)SZYMON MARCINIAK (POLONIA)"],
          ["1) 2 PENALES","2) 3 PENALES","3) 4 PENALES","4) 5 PENALES"]
          ]
    
    #Inicializa la puntuación y las vidas del jugador
    puntos=0
    vidas=3
    
    #Pregunta el nombre del jugador
    nombre_jugador=input("Ingrese su nombre: ")
    
    #Itera sobre las preguntas, usando el índice
    for i in range(len(preguntas)):
        print("\n" + "*"*90)
        print(f"PREGUNTA {i+1}:{preguntas[i]}")
        print("*"*90)
       
        for opcion in opciones[i]:     #Muestra las opciones para la pregunta actual
            print(opcion)
        respuesta_jugador=int(input("INGRESE SU RESPUESTA, CON NÚMEROS DEL 1 AL 4:  "))   #Se obtiene la respuesta del jugador
        while respuesta_jugador<1 and respuesta_jugador>4:    #Validación de la entrada
            print("EL CARACTER INGRESADO ES INCORRECTO")
            respuesta_jugador=int(input("INGRESE SU RESPUESTA, CON NÚMEROS DEL 1 AL 4:  "))
        if respuesta_jugador==respuestas_correctas[i]:  #Verifica si la respuesta es correcta
                puntos+=20
                print(f">>>>>>>>RESPUESTA CORRECTA<<<<<<<<\nTIENES {vidas} VIDAS\nTIENES {puntos} PUNTOS")
                
        else:                                           #Si la repuesta es incorrecta
                vidas-=1
                print(f">>>>>>>>RESPUESTA INCORRECTA<<<<<<<<\nTIENES {vidas} VIDAS")
            
        if vidas==0:                                    #Si el jugador se queda sin vidas, termina el juego
                print("\nPERDISTE TODAS TUS VIDAS")
                print("*"*40)
                break
    print("\n"+"*"*40)        
    print(f"JUEGO TERMINADO\nTU PUNTUACIÓN ES: {puntos} PUNTOS")  #Muestra la puntuación final
    print("*"*40)
    with open("puntajes.txt", "a") as archivo:              #Guarda el nombre del jugador y el puntaje en un archivo de texto
        archivo.write(f"{nombre_jugador}: {puntos} pts.\n")
        
        print("Puntaje guardado")

while True:                                     #Bucle principal del juego
    juego_preguntas_qatar2022()                 #Ejecuta el juego
    reiniciar=input("¿QUIERES VOLVER A JUGAR? SI (S) NO (N)").lower() #Pregunta al jugador si quiere volver a jugar
    if reiniciar!="s":
        print("Gracias por jugar\nGAME OVER")
        break
                


    
        
    
    
        
        
            