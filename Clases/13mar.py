import random 

def tirar_dados()-> int:
    aleatorio1 = random.randrange(1, 7)
    print(f"Primer dado: {aleatorio1}")
    aleatorio2 = random.randrange(1, 7)
    print(f"Segudno dado: {aleatorio2}")
    return aleatorio1 + aleatorio2

def validar_suma()-> tuple[str, int]:  #tuple: puede regresar más de un valor
    '''''
    Simula el lanzamiento de dos dados y valida la suma de  .......
    '''
    print("Se van a tirar 2 dados...")
    suma_dados = tirar_dados()
    print(f"La suma de los dados es: {suma_dados}")

    if suma_dados == 7 or suma_dados == 11:
        resultado = "Ganaste"
    elif suma_dados == 2 or suma_dados == 3 or suma_dados == 1:
        resultado = "Perdiste"
    # aquí falta xdn't

def preguntar_repetir_juego()->bool:
    resp = input("¿Quieres volver a jugar? [si/no]:")
    return resp.upper().strip() == "SI"

def generar_reporte(total_juegos:int, total_ganados:int, total_perdidos:int):
    print("\nReporte:")
    print(f"Total de juegos jugados: {total_juegos}")
    print(f"Total de juegos ganados: {total_ganados}")
    print(f"Total de juegos pardidos: {total_perdidos}")

def jugar_dados():
    total_juegos = 0
    total_ganados = 0 
    total_perdidos = 0 
    seguir_jugando = True

    while seguir_jugando:
        total_juegos +=1
        resultado, suma_dados = validar_suma()
        print(resultado, ",", suma_dados)

        if resultado == "Seguir Jugando":
            suma_pts_usuario = suma_dados
            suma_dados = tirar_dados()
        if (suma_dados == 7 or suma_dados == 11 ): 
            #falta otro or
            print("Después de tirar de nuevo ganaste!!")
            total_ganados +=1
        else: 
            print("Después de tirar de nuevo PERDISTE!!!")
            total_perdidos +=1

        seguir_jugando = preguntar_repetir_juego()
        if not seguir_jugando:
            print("Fin del juego...")
            generar_reporte(total_juegos, total_ganados, total_perdidos)

if __name__ == "__main__":
    jugar_dados()
