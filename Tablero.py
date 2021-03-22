import random
from Ficha import Ficha
from Jugador import Jugador

class Tablero:
    ArrayFichasCabeza=[]
    ArrayFichasCola=[] 
    cola=0
    cabeza=0

    def inicia(self,ficha):
        cola=ficha.valorA
        cabeza=ficha.valorB
        ficha.spin=0
        self.ArrayFichasCabeza.append(ficha)
        #comienza el juego    

    def Coloca(self,Ficha, lugar):
        #se añade la ficha colocada y se actualizan las listas de la cola / cabeza (valores del tablero) 
        
        if lugar=="Cola":
           self.ArrayFichasCola.insert(0,Ficha) 
           if self.cola==Ficha.valorA:
                self.cola=Ficha.valorB
                return
           else:
                self.cola=Ficha.valorA
                return
        if lugar=="Cabeza":
           self.ArrayFichasCabeza.append(Ficha) 
           if self.cabeza==Ficha.valorA:
                self.cabeza=Ficha.valorB
                return
           else:
                self.cabeza=Ficha.valorA
                return

    def ver(self):
        #se muestra el tablero
        girovalorSpin=0
        posinicial=6
        contador=0

        print("--------- CABEZA DE LA SERPIENTE ---------------")
        for f in self.ArrayFichasCabeza:
            if posinicial==f.valorA:
                print(f.valorA,":",f.valorB," - ", end=' ')
                posinicial=f.valorB
            else:
                print(f.valorB,":",f.valorA," - ", end=' ')
                posinicial=f.valorA

        print()

        print("--------- COLA DE LA SERPIENTE ---------------")
        for f in self.ArrayFichasCola :
            contador -=1
            if self.ArrayFichasCola[contador].spin==False:
                print(self.ArrayFichasCola[contador].valorA,":",self.ArrayFichasCola[contador].valorB," - ", end=' ')
            else:
                print(self.ArrayFichasCola[contador].valorB,":",self.ArrayFichasCola[contador].valorA," - ", end=' ')

        girovalorSpin=-1
        posinicial=6
        print()

#------------------------------------------------------------
# Zona de funciones
#------------------------------------------------------------

def CuantosHay(lista):
    contador=0
    for a in lista:
        contador= contador+1
    return contador

def tipojugador(texto):

    try:
        respuesta=int(input("Elige " + texto + ": CPU (1) o Humano (2):"))
    except:
        print("Producido un error al introducir numero")
        return
        pass

    if respuesta==1:
        jugadorElegido=Jugador()
        jugadorElegido.tipo="CPU"
        jugadorElegido.inteligencia=int((input("Elige la dificultad: Fácil (1), Media (2), Díficil (3):")))

    else:
        jugadorElegido=Jugador()
        jugadorElegido.tipo="Humano"
    return jugadorElegido


def elegirJugadores():
    print("-------------------------------------------------")
    print("Inicio del juego....eligiendo tipo de jugador")
    print("-------------------------------------------------")
    jugadorA=tipojugador("Jugador A")
    jugadorB=tipojugador("Jugador B")
    jugadorC=tipojugador("Jugador C")
    jugadorD=tipojugador("jugador D")
    return jugadorA,jugadorB,jugadorC,jugadorD

def AveriguaJugadorConFicha(FichaBuscada,jugA,jugB,jugC,jugD):
    #esta funcion sirve para saber que jugador tiene una determinada ficha (6:6 por ejemplo)
    f=Ficha()

    for f in jugA.ArrayFichas:
        if (f.valorA == FichaBuscada.valorA) and (f.valorB == FichaBuscada.valorB):
            return jugA, 0
    for f in jugB.ArrayFichas:
        if (f.valorA == FichaBuscada.valorA) and (f.valorB == FichaBuscada.valorB):
            return jugB, 1
    for f in jugC.ArrayFichas:
        if (f.valorA == FichaBuscada.valorA) and (f.valorB == FichaBuscada.valorB):
            return jugC, 2
    return jugD, 3

def partida(jugadorA,jugadorB,jugadorC,jugadorD):
    #generar fichas....   
    GrupoFicha=[]
    contador=0
    posibles=[0,1,2,3,4,5,6,7]
    for a in posibles:
        for b in posibles[a:7]:
            contador = contador + 1
            #print a,b," - ",contador
            Ficha_Prototipo=Ficha()
            Ficha_Prototipo.new(a,b)
            #Ficha_Prototipo.ver()
            GrupoFicha.append(Ficha_Prototipo)

    ListaJugadores=[]
    ListaJugadores=[jugadorA,jugadorB,jugadorC,jugadorD]

    w=ListaJugadores[0]
    x=ListaJugadores[1]
    y=ListaJugadores[2]
    z=ListaJugadores[3]

    #repartir fichas a los jugadores
    aleatorio=0
    listaOrdenadaAleatoriamente=random.shuffle(GrupoFicha) 

    #random.shuffle: desordena de modo aleatorio una lista
    #asigno la cuarta parte de la lista de fichas a cada jugador
    #ref web: http://docs.python.org/2/library/random.html
    w.ArrayFichas=GrupoFicha[:7]
    x.ArrayFichas=GrupoFicha[7:14]
    y.ArrayFichas=GrupoFicha[14:21]
    z.ArrayFichas=GrupoFicha[21:28]

    #imprimo en pantalla como ha sido el reparto de las fichas
    print("Fichas Repartidas:")
    print("--------------------")
    print("Jugador A:")
    print(w.escribe())
    print("--------------------")
    print("Jugador B:")
    print(x.escribe())
    print("Jugador C:")
    print(y.escribe())
    print("--------------------")
    print("Jugador D:")
    print(z.escribe())

#Inicio el juego
    #averiguar quiene tiene el 6:6
    FichaBuscar=Ficha()
    FichaBuscar.valorA=6
    FichaBuscar.valorB=6

    jug=Jugador()
    jug, numero= AveriguaJugadorConFicha(FichaBuscar,w,x,y,z)

    print("El jugador que tiene la ficha buscada es..")
    #empieza a jugar con el jugador que tenga la ficha buscada...

    if numero==0:
        print("jugador A")
        numero=1
        w.elimina(FichaBuscar)
    elif numero==1:
        print("jugador B")
        numero=2
        x.elimina(FichaBuscar)
    elif numero==2:
        print("jugador C")
        numero=3
        y.elimina(FichaBuscar)
    else:
        print("jugador D")
        numero=4
        z.elimina(FichaBuscar)
#El jugador pone la ficha en la serpierte y se elimina de la lista de fichas que tiene

    Tab=Tablero()
    Tab.cola=FichaBuscar.valorA
    Tab.cabeza=FichaBuscar.valorB

#rellena el tablero  o serpiente con la primera  pieza
    Tab.inicia(FichaBuscar)

#Inicia las variables del bucle principal....
    FichaColocada=Ficha()
    Lugar=""
    respuesta=""
    print("Numero:",numero)
    valorAnterior=""
    valorPasado=""
    valorFinal=""
    bucle=True

#Bucle Principal del Juego...
    while bucle:

        if numero==1:
            print("Esta jugando....Jugador: B")
            respuesta,FichaColocada, lugar = x.coloca(Tab)
            nombrejugador="B"

        elif numero==2:
            print("Esta jugando....Jugador: C")
            respuesta,FichaColocada, lugar = y.coloca(Tab)
            nombrejugador="C"

        elif numero==3:
            print("Esta jugando....Jugador D")
            respuesta, FichaColocada, lugar = z.coloca(Tab)
            nombrejugador="D"

        else:
            print("Esta jugando....Jugdor A")
            respuesta, FichaColocada, lugar = w.coloca(Tab)
            nombrejugador="A"

        #la repuesta puede ser:
        #    "UltimaFicha"-> ya no tiene mas piezas y es el ganador...
        #    "Pasa"-> no tiene ficha para poner... y aun le quedan fichas por poner...
        #    "Coloca" -> tiene una ficha para poner... en la cola o en la cabeza de la serpiente...

        if respuesta=="UltimaFicha":
            Tab.Coloca(FichaColocada,lugar)
            if numero==1:
                x.marcador +=  w.cuenta() + y.cuenta() + z.cuenta()
            if numero==2:
                y.marcador +=  w.cuenta() + x.cuenta() + z.cuenta()
            if numero==3:
                z.marcador +=  w.cuenta() + x.cuenta() + y.cuenta()
            else:
                w.marcador +=  x.cuenta() + y.cuenta() + z.cuenta()
            print("Coloca:", FichaColocada.ver(),"Lugar:", lugar)
            print("Y es la ultima pieza!!")
            break #sale del bucle porque hay un ganador...!!

        elif respuesta=="Coloca":
            print("Coloca:", FichaColocada.ver(), "Lugar:", lugar)
            Tab.Coloca(FichaColocada,lugar)
            valorAnterior="" #no pasa porque ha colocado una ficha
            #http://www.tutorialspoint.com/python/python_if_else.htm
        
        elif respuesta=="Pasa":
            #comprobar que el anterior jugador paso.. si es asi, los dos pasan... y hay que calcular quien tiene menos puntos para saber el ganador.
            if numero==1:
                x.CuentaVecesQueNoPuedePoner = x.CuentaVecesQueNoPuedePoner + 1
            elif numero==2:
                y.CuentaVecesQueNoPuedePoner = y.CuentaVecesQueNoPuedePoner + 1
            elif numero==3:
                z.CuentaVecesQueNoPuedePoner = z.CuentaVecesQueNoPuedePoner + 1
            else:
                w.CuentaVecesQueNoPuedePoner = w.CuentaVecesQueNoPuedePoner + 1

            a = ("  A (tenia ",ListaJugadores[0].cuenta()," puntos)")
            b = ("  B (tenia ",ListaJugadores[1].cuenta()," puntos)")
            c = ("  C (tenia ",ListaJugadores[2].cuenta()," puntos)")
            d = ("  D (tenia ",ListaJugadores[3].cuenta()," puntos)")

            if valorAnterior == "Pasa":
                if valorPasado == "Pasa el otro":
                    if valorFinal == "Todos pasan":

                        if w.cuenta() < x.cuenta() and w.cuenta() < y.cuenta() and w.cuenta() < z.cuenta():
                            print("Ganador jugador A (tenia ", ListaJugadores[0].cuenta(), " puntos)")
                            print(b)
                            print(c)
                            print(d)
                            ListaJugadores[0].marcador += ListaJugadores[1].cuenta() + ListaJugadores[2].cuenta() + ListaJugadores[3].cuenta()

                        elif x.cuenta() < w.cuenta() and x.cuenta() < y.cuenta() and x.cuenta() < z.cuenta():
                            print("Ganador jugador B (tenia ", ListaJugadores[1].cuenta(), " puntos)")
                            print(a)
                            print(c)
                            print(d)
                            x.marcador += w.cuenta() + y.cuenta() + z.cuenta()

                        elif y.cuenta() < w.cuenta() and y.cuenta() < x.cuenta() and y.cuenta() < z.cuenta():
                            # gana el jugador 0
                            print("Ganador jugador C (tenia ", y.cuenta(), " puntos)")
                            print(a)
                            print(b)
                            print(d)
                            y.marcador += w.cuenta() + x.cuenta() + z.cuenta()

                        else:
                            print("Ganador jugador D (tenia ", z.cuenta(), "puntos)")
                            print(a)
                            print(b)
                            print(c)
                            z.marcador += w.cuenta() + x.cuenta() + y.cuenta()

                        break
                    else:
                        valorFinal="Todos pasan"
                else:
                    valorPasado="Pasa el otro"
            else:
                #asigno a la variable bandera el valor de "Pasa"
                valorAnterior="Pasa"
                #en la anteior jugada no paso el jugador anterior

        #cambio de turno
        if numero== 4:
            numero=1
        elif numero==1:
            numero=2
        elif numero==2:
            numero=3
        else:
            numero=4

        #muestro estado del tablero
        print("Estado de la Serpiente: ",Tab.cola,Tab.cabeza)
        bucle=True #no se ha terminado el juego


#.....................................................................................................
# he llegado al final del juego (porque alguien colocó su ultima ficha o pasaron todos los jugadores
#.....................................................................................................
    
    print("")
    print("=============================================================================")
    print("=                            Informacion de la partida                      =")
    print("=============================================================================")
    print("Resultado:")
    Tab.ver()

    print("")
    print("El jugador A, suma un total de ")
    print("   PUNTOS:",w.marcador)
    print("   Numero de veces que no ha podido poner ficha: ",w.CuentaVecesQueNoPuedePoner)
    print(w.escribe())
    print("")

    print("El jugador B, suma un total de ")
    print("   PUNTOS:",x.marcador)
    print("   Numero de veces que no ha podido poner ficha: ",x.CuentaVecesQueNoPuedePoner)
    print(x.escribe())
    print("")

    print("El jugador C, suma un total de ")
    print("   PUNTOS:",y.marcador)
    print("   Numero de veces que no ha podido poner ficha: ",y.CuentaVecesQueNoPuedePoner)
    print(y.escribe())
    print("")

    print("El jugador D, suma un total de ")
    print("   PUNTOS:",z.marcador)
    print("   Numero de veces que no ha podido poner ficha: ",z.CuentaVecesQueNoPuedePoner)
    print(z.escribe())
    print("")

    #devuelve la estadisticas de la partida

    if w.marcador > x.marcador and w.marcador > y.marcador and w.marcador > z.marcador:
        print("----------------------------------")
        print("EL GANADOR ES: Jugador A")
        print("----------------------------------")

    elif x.marcador > w.marcador and x.marcador > y.marcador and x.marcador > z.marcador:
        print("----------------------------------")
        print("EL GANADOR ES: Jugador B")
        print("----------------------------------")

    elif y.marcador > w.marcador and y.marcador > x.marcador and y.marcador > z.marcador:
        print("----------------------------------")
        print("EL GANADOR ES: Jugador C")
        print("----------------------------------")

    else:
        print("----------------------------------")
        print("EL GANADOR ES: Jugador D")
        print("----------------------------------")

    respuesta = int(input("Quieres seguir jugando:"))

    if respuesta == 1:
        pregunta = int(input("Quieres continuar con los mismos jugadores:"))
        if pregunta == 0:
            jugA, jugB, jugC, jugD = elegirJugadores()
            for f in range(1):
                jugA, jugB, jugC, jugD = partida(jugA, jugB, jugC, jugD)
                jugA.MarcadorGeneral += jugA.marcador
                jugB.MarcadorGeneral += jugB.marcador
                jugC.MarcadorGeneral += jugC.marcador
                jugD.MarcadorGeneral += jugD.marcador
            print("Final:")
            print(jugA.marcador, jugB.marcador, jugC.marcador, jugD.marcador)

        else:
            jugA, jugB, jugC, jugD = ListaJugadores[0], ListaJugadores[1], ListaJugadores[2], ListaJugadores[3]
            for f in range(1):
                jugA, jugB, jugC, jugD = partida(jugA, jugB, jugC, jugD)
                jugA.MarcadorGeneral += jugA.marcador
                jugB.MarcadorGeneral += jugB.marcador
                jugC.MarcadorGeneral += jugC.marcador
                jugD.MarcadorGeneral += jugD.marcador
            print("Final:")
            print(jugA.marcador, jugB.marcador, jugC.marcador, jugD.marcador)
            #se llama la funcióna si misma

    return print("Gracias por jugar")

    pass


def main():
    jugA= Jugador()
    jugB= Jugador()
    jugC= Jugador()
    jugD= Jugador()
    listajugadores=[jugA,jugB,jugC,jugD]
    print("")
    print("-------------------------------")
    print("-        Domino Master        -")
    print("-------------------------------")
    print("1- Comenzar partida")
    print("2- ¿Cómo jugar?")
    print("3- Salir")
    respuesta=int(input("Elige una opción:"))
    #elijo tipo de jugadores Humano o Cpu (y su dificultad)
    if respuesta==1:
        jugA, jugB, jugC, jugD = elegirJugadores()
        for f in range(1):
            jugA,jugB,jugC,jugD = partida(jugA,jugB,jugC,jugD)
            jugA.MarcadorGeneral += jugA.marcador
            jugB.MarcadorGeneral += jugB.marcador
            jugC.MarcadorGeneral += jugC.marcador
            jugD.MarcadorGeneral += jugD.marcador
        print("Final:")
        print(jugA.marcador,jugB.marcador,jugC.marcador,jugD.marcador)
   
    elif respuesta==2:
        print("""
Objetivo:        
El objetivo del juego es colocar todas tus fichas en la mesa antes que los contrarios y sumar puntos. 
El jugador que gana una ronda, suma puntos según las fichas que no han podido colocar los oponentes.        

Reglas:       
Cada jugador recibe 7 fichas al empezar la partida. Inicia la ronda el jugador que tenga la ficha 
con el doble más alto, al haber 4 jugadores empieza aquél que tenga el 6 doble.
Los jugadores van en orden inverso a las manecillas del reloj.

Desarrollo:
En su turno, cada jugador debe colocar una de sus fichas en uno de los 2 extremos abiertos 
...los puntos de uno de los lados de la ficha debe coincidir con los puntos del extremo. 
Si un jugador no puede jugar, pasará el turno al siguiente jugador.

Fin de la ronda:
Los jugadores continuan colocando sus fichas hasta que presente una de estas situaciones.-
Cuando todos los jugadores han pasado en un mismo turno
...gana el jugador con menos puntos.
Cuando un jugador coloca su última ficha en la mesa 
...gana de manera sublime.      """)
        
        main()
  
    elif respuesta==3:
        print ("Adios")
  
    elif respuesta>3:
        print ("Escoja un maldito número")
        main()
    pass

if __name__ == '__main__':
    main()