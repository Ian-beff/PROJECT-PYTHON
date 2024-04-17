import random

def mostrarMenu(): # Esta función muestra el menú del juego y pide al usuario que escoja una opción
	msg = "Benvingut al Joc de l'Oca!\nEscull una opció:\n1.Inicialitzar Joc\n"
	msg +="2.Visualitzar taulell \n3.Jugar\n0.Sortir" 
	print(msg)
	opcion = input("Introdueix una opció: ")
	while not opcion.isnumeric() or int(opcion) > 3 or int(opcion) < 0: # Esto comprueba que la opción introducida sea un número entre 0 y 3 si no lo es volvemos a pedir una opción
		opcion = input('\033[41m'+"Opció incorrecte!"+'\033[40m' + msg)
	return int(opcion) # Devolvemos la opción que ha elegido el usuario


def generarTaulell(): # Esta función genera el tablero del juego
	t = []
	oques = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
	for i in range(1, 64): # Recorremos todas las casillas del tablero
		if i in oques:
			t.append("| OCA     ")
		elif i == 26 or i == 53:
			t.append("|DAUS     ")
		elif i == 42:
			t.append("|LAB.     ")
		elif i == 58:
			t.append("|MORT     ")
		else:
			aux = " " if (i<10) else ""
			t.append(f"|{aux}{i}       ")
	return t


def inicialitzarJoc(): # Esta función inicializa el juego, generando el tablero y pidiendo el número de jugadores
	inicialitzarFitxes() # Inicializamos las fichas de los jugadores
	n = int(input("Indica quants jugadors sereu (2-6):"))
	global jugadors # Declaramos la variable jugadors como global para poder modificarla
	jugadors.clear()
	for i in range(n):
		jugadors.append(1)
	global taulell  # Declaramos la variable taulell como global para poder modificarla
	taulell.clear()
	taulell = generarTaulell()
	for i in range(n):
		print(fitxes[i], end="   ") # Imprimimos la ficha del jugador
	print()
	return


def mostrarTaulell(): # Esta función muestra el tablero del juego, que indica la posición de cada jugador
    for i in range(len(taulell)):  # Recorremos todas las casillas del tablero
        if i+1 in jugadors:  # Si hay algún jugador en la casilla actual
            fitxs = ""  # Inicializamos la cadena de fichas
            k = 0  # Inicializamos el contador de fichas
            for j in range(len(jugadors)):
                if jugadors[j] == i+1:
                    fitxs += fitxes[j]   # Añadimos la ficha del jugador a la cadena de fichas
                    k+=1
            espais = (5 - k) * " "
            print(taulell[i][:5] + fitxs + espais, end="")  # Imprimimos la casilla con las fichas de los jugadores
        else:
            print(taulell[i], end="")
        if i%12==0:
            print("|")
    print("|")
    return

def ferTirada(taulell, torn):  # Esta función tira el dado por cada jugador en su turno y mueve su ficha
    dau = random.randint(1, 6)  # Tirar el dado
    print(f"És el torn del jugador {torn + 1}. Ha tret un {dau}.")
    jugadors[torn] += dau  # Mover la ficha del jugador
    canvi_torn = ComprovarAccionsTirada(taulell, torn) # Comprobamos si la casilla en la que ha caído el jugador tiene alguna acción especial
    return canvi_torn

def ComprovarAccionsTirada(taulell, torn):  # Esta función comprueba si la casilla en la que ha caído el jugador tiene alguna acción especial
    casella = taulell[jugadors[torn]-1]
    if casella == '| OCA     ':
        # Encuentra la siguiente OCA en el tablero
        siguiente_oca = min([i for i in range(jugadors[torn], len(taulell)) if taulell[i] == '| OCA     '], default=63)
        jugadors[torn] = siguiente_oca + 1
        print(f"El jugador {torn + 1} ha caigut en la casella de la OCA. Es mou a la següent casella de la OCA i torna a tirar.")
        return False  # El jugador tiene que volver a tirar, así que no cambiamos de turno
    elif casella == '|DAUS     ':
        desplaçament = random.choice([-1, 1])  # Hacemos un desplazamiento aleatorio de -1 o 1
        jugadors[torn] += desplaçament  # Movemos al jugador
        if desplaçament == 1:
            print(f"El jugador {torn + 1} ha caigut en la casella DAUS. Es desplaça una casella cap endavant i torna a tirar.")
        else:
            print(f"El jugador {torn + 1} ha caigut en la casella DAUS. Es desplaça una casella cap endarrere i torna a tirar.")
        return False
    elif casella == '|LAB.     ':
        jugadors[torn] = 30 # Movemos al jugador a la casilla 30
        print(f"El jugador {torn + 1} ha caigut en la casella LAB. Es desplaça automàticament a la casella 30.")
        return True
    elif casella == '|MORT     ':
        jugadors[torn] = 1 # Movemos al jugador a la casilla 1
        print(f"El jugador {torn + 1} ha caigut en la casella de la MORT. Torna a començar des del principi.")
        return True
    else:
        return True

def inicialitzarFitxes():  # Esta función inicializa las fichas de los jugadores con diferentes colores
    global fitxes
    negre = '\033[40m'
    vermell = '\033[41m'
    verd = '\033[42m'
    groc = '\033[43m'
    blau = '\033[44m'
    lila = '\033[45m'
    cyan = '\033[46m'
    gris = '\033[47m'

    fitxes = []
    fitxes.append(verd + " " + negre)
    fitxes.append(blau + " " + negre)
    fitxes.append(vermell + " " + negre)
    fitxes.append(groc + " " + negre)
    fitxes.append(lila + " " + negre)
    fitxes.append(cyan + " " + negre)
    fitxes.append(gris + " " + negre)	
    
def Jugar(tau):  # Esta función controla el juego, cambiando los turnos de los jugadores y comprueba si alguno ha ganado
    partidaActiva = True  # Inicializamos la variable a True para indicar que la partida está en curso
    torn = -1  # Inicializamos la variable torn a -1 para indicar que aún no ha empezado ningún turno
    tir = 0  # Inicializamos la variable tir a 0 para saber la cuenta de las tiradas
    while partidaActiva:
        # 1- Assignem torn 
        torn = (torn+1) % len(jugadors)  # Calculamos a quién le toca el turno
        canviarTorn = False  # Inicializamos la variable canviarTorn a False para indicar que no hay que cambiar de turno

        # 2- Bucle de tirades fins que canviem de torn o algun jugador arribi a 63
        while not canviarTorn:
            tir+=1
            canviarTorn = ferTirada(tau, torn)  # Hacemos una tirada y comprobamos si hay que cambiar de turno
            mostrarTaulell()
            input("Prem return per continuar...")
            
            # 3- Si un jugador arriba al final, s'acaba la partida
            if jugadors[torn] >= 63:  # Si el jugador ha llegado a la casilla 63 o más
                partidaActiva = False   # La partida se acaba
                print(f"Enhorabona jugador {torn+1}!! Has guanyat la partida!")
                break


# Aquí comienza el main
# Declaración de variables
taulell = []
jugadors = []
fitxes = []
opcio = -1
# Bucle principal (que acaba cuando el usuario escoge 0 para salir)
while opcio != 0:
	# LLama a la función menú
	opcio = mostrarMenu()
	if opcio == 1:
		inicialitzarJoc()
		# print(taulell)
		mostrarTaulell()
	elif opcio == 2:
		mostrarMenu()
	elif opcio == 3:
		Jugar(taulell)