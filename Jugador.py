import random
from Ficha import Ficha

class Jugador:
    ArrayFichas=[] #lista de fichas que tiene el jugador
    marcador=0 #cuenta los puntos que se acumulan al ganar
    tipo="" #CPU o HUMAN
    inteligencia=0
    CuentaVecesQueNoPuedePoner=0
    MarcadorGeneral=0

    def escribe(self):
        print("------------Fichas que Tengo---------------")
        print("Cantidad:", len(self.ArrayFichas))
        print("Descripcion:")
        for a in self.ArrayFichas:
            a.ver()

    def cuenta(self):
        suma=0
        f=Ficha()
        for f in self.ArrayFichas:
            suma += f.valorA + f.valorB
        return suma

    def cuentaListaDada(self,lista):
        suma=0
        f=Ficha()
        for f in lista:
            suma +=1
        return suma

    def FichaMasPesada(self,lista):
        fichapesada=[]
        fichapesada.append(lista[0])
        for f in lista:
            if f.contar()>fichapesada[0].contar():
                fichapesada[0]=f
        return fichapesada

    def FichaMasPesadaDobles(self,lista):
        GrupoFichaDobles=[] #lista donde estan las dobles
        felegida=[] 
        #doy prioridad a las dobles
        for f in lista:
            if f.valorA==f.valorB:
                GrupoFichaDobles.append(f)
        if len(GrupoFichaDobles)>0:
            felegida=GrupoFichaDobles
            for f2 in GrupoFichaDobles:
                if f2.contar()>felegida[0].contar():
                    felegida[0]=f2
            return felegida,"Doble"
        else:
            #eligo la mas pesada...
            devuelve=[]
            devuelve=self.FichaMasPesada(lista)
            return  devuelve, "Pesada"

    def elimina(self,FichaBuscar):
        for fichaX in self.ArrayFichas:
            if fichaX.valorA==FichaBuscar.valorA and fichaX.valorB==FichaBuscar.valorB:
                self.ArrayFichas.remove(fichaX)

    def listafichasQuePuedenPonerse(self, Tablero, Valor,lugar):
        devuelve=[]
        for X in self.ArrayFichas:
            if X.valorA==Valor and X.valorB==Valor:
                if lugar=="Cola":
                    X.spin= False
                    devuelve.append(X)
                    X.spin= True
                    devuelve.append(X)
                    return devuelve
                else:
                    X.spin= False
                    devuelve.append(X)
                    X.spin= True
                    devuelve.append(X)
                    return devuelve
            if X.valorA==Valor:
                if lugar=="Cola":
                    X.spin= False
                else:
                    X.spin= True
                devuelve.append(X)
            elif X.valorB==Valor:
                if lugar=="Cabeza":
                    X.spin= False
                else:
                    X.spin= True
                devuelve.append(X)
        return devuelve

    def muestraFichas(self,lista):
        contador=-1
        if len(lista)>0:
          for f in lista:
            contador+=1
            print("Numero Indice: ",contador," Ficha:" ,f.valorA,":",f.valorB)

    def coloca(self,Tablero):
        FichasCabeza=[]
        FichasCola=[]
        TotalMovimientos=0
        #crear lista de fichas que puedo colocar en la cabeza de la serpiente
        FichasCabeza = self.listafichasQuePuedenPonerse(Tablero, Tablero.cabeza,"Cabeza")


        #crear lista de fichas que puedo colocar en la cola de la serpiente
        FichasCola = self.listafichasQuePuedenPonerse(Tablero, Tablero.cola,"Cola")

        TotalMovimientos = self.cuentaListaDada(FichasCabeza) + self.cuentaListaDada(FichasCola)

        #Si la suma de los elementos de las listas=1, entonces es la ultima ficha-> ganador...!!

        print("El total de movimientos es de: ",TotalMovimientos)
        if TotalMovimientos>0 and self.cuentaListaDada(self.ArrayFichas)==1:
            if len(FichasCola)==0:
                UltimaFicha=FichasCabeza[0]
                lugar="Cabeza"

            else:
                UltimaFicha=FichasCola[0]
                lugar="Cola"
            self.elimina(UltimaFicha)
            return "UltimaFicha" , UltimaFicha , lugar

        #Si las listas no contienen fichas se devuelve el valor "Pasa"

        if TotalMovimientos==0:
            return "Pasa", "", ""

        if self.tipo=="CPU":
            if self.inteligencia==1:
            #puede elegir de las dos listas, ya que tienen ambas fichas a colocar
                if len(FichasCabeza)>0 and len(FichasCola)>0:
                    if random.randint(0, 1)==1:
                        FichaMovida=random.sample(FichasCabeza, 1)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cabeza"
                    else:
                        FichaMovida=random.sample(FichasCola, 1)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cola"
                    #solo puede coger fichas de la ficha de Cabeza / Cola
                if len(FichasCabeza)>0:
                        FichaMovida=random.sample(FichasCabeza, 1)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cabeza"
                else:
                        FichaMovida=random.sample(FichasCola, 1)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cola"
            elif self.inteligencia==2:
                #----------------------------------------------------------------------
                print("Inteligencia 2")
                #----------------------------------------------------------------------
                if len(FichasCabeza)>0 and len(FichasCola)>0:
                    #Elige la ficha mas pesada de la lista...
                        FichaMovidaCabeza=self.FichaMasPesada(FichasCabeza)
                        FichaMovidaCola=self.FichaMasPesada(FichasCola)
                        if FichaMovidaCabeza[0].contar()>FichaMovidaCola[0].contar():
                            self.elimina(FichaMovidaCabeza[0])
                            return "Coloca",FichaMovidaCabeza[0],"Cabeza"
                        else:
                            self.elimina(FichaMovidaCola[0])
                            return "Coloca", FichaMovidaCola[0],"Cola"
                     #solo fichas de la Cabeza
                if len(FichasCabeza)>0:
                        FichaMovida=self.FichaMasPesada(FichasCabeza)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cabeza"
                else:
                        #solo fichas de la Cola
                        FichaMovida=self.FichaMasPesada(FichasCola)
                        self.elimina(FichaMovida[0])
                        return "Coloca", FichaMovida[0], "Cola"
            elif self.inteligencia==3:
                #comprobación de dobles 
                if len(FichasCabeza)>0 and len(FichasCola)>0:
                        FichaMovidaCabeza,tipoPesadaDobleCabeza=self.FichaMasPesadaDobles(FichasCabeza)
                        FichaMovidaCola,tipoPesadaDobleCola=self.FichaMasPesadaDobles(FichasCola)
                        if tipoPesadaDobleCabeza=="Doble" and tipoPesadaDobleCola=="Doble":
                                if FichaMovidaCabeza[0].contar()>FichaMovidaCola[0].contar():
                                    self.elimina(FichaMovidaCabeza[0])
                                    return "Coloca",FichaMovidaCabeza[0],"Cabeza"
                                else:
                                    self.elimina(FichaMovidaCola[0])
                                    return "Coloca",FichaMovidaCola[0],"Cola"
                        if tipoPesadaDobleCabeza=="Doble":
                                    self.elimina(FichaMovidaCabeza[0])
                                    return "Coloca",FichaMovidaCabeza[0],"Cabeza"
                        elif tipoPesadaDobleCola=="Doble":
                                    self.elimina(FichaMovidaCola[0])
                                    return "Coloca",FichaMovidaCola[0],"Cola"
                                    #no hay doble, coloco la que tenga m?s peso..
                        if  FichaMovidaCabeza[0].contar()>FichaMovidaCola[0].contar():
                                    self.elimina(FichaMovidaCabeza[0])
                                    return "Coloca",FichaMovidaCabeza[0],"Cabeza"
                        else:
                                    self.elimina(FichaMovidaCola[0])
                                    return "Coloca", FichaMovidaCola[0],"Cola"
                elif len(FichasCabeza)>0:
                    FichaMovidaCabeza,tipoPesadaDobleCabeza=self.FichaMasPesadaDobles(FichasCabeza)
                    self.elimina(FichaMovidaCabeza[0])
                    return "Coloca",FichaMovidaCabeza[0],"Cabeza"
                else:
                    FichaMovidaCola,tipoPesadaDobleCola=self.FichaMasPesadaDobles(FichasCola)
                    self.elimina(FichaMovidaCola[0])
                    return "Coloca",FichaMovidaCola[0],"Cola"


        else:
            print("Movimiento Humano")
            print("La serpiente es:")
            Tablero.ver()
            lugarTablero=0
            print("Las fichas que tienes son:")
            self.muestraFichas(self.ArrayFichas)
            #ver movimientos posibles para colocar en la cola / cabeza
            if len(FichasCola)!=0:
                print("Posibles movimientos para la cola(0):")
                self.muestraFichas(FichasCola)
            if len(FichasCabeza)!=0:
                print("Posibles movimiento para la cabeza(1):")
                self.muestraFichas(FichasCabeza)
            #pido eleccion de fichas...
            if len(FichasCabeza)==0:
                mydata = int(input('Solo puedes poner en la Cola(0), di el indice de ficha:'))
                self.elimina(FichasCola[mydata])
                return "Coloca",FichasCola[mydata],"Cola"
            elif len(FichasCola)==0:
                mydata =int( input('Solo puedes poner en la Cabeza(1), di el indice de ficha:'))
                self.elimina(FichasCabeza[mydata])
                return "Coloca",FichasCabeza[mydata],"Cabeza"
            else:
                lugarTablero=int(input('Elige Cola(0) o Cabeza(1):'))
                mydata = int(input('Di el indice de ficha:'))
                if lugarTablero==0:
                    self.elimina(FichasCola[mydata])
                    return "Coloca",FichasCola[mydata],"Cola"
                else:
                    self.elimina(FichasCabeza[mydata])
                    return "Coloca",FichasCabeza[mydata],"Cabeza"
        #Si las listas contienen mas de una ficha se coloca la ficha, se elimina del arreglo  
        #& se regresa el valor "Coloca"

        print(self.tipo,self.inteligencia)
        return "Error", "0", "0"

