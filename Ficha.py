class Ficha:
#cuando se usa el metodo new, se crea la ficha con sus valores...
    valorA=0
    valorB=0
    def new(self,valorA,valorB):
        if valorA>valorB:
            self.valorA=valorA
            self.valorB=valorB
            self.spin= True
        else:
            self.valorA=valorA
            self.valorB=valorB
            self.spin= False

    def ver(self):
        print("Ficha: ",self.valorA,"-",self.valorB)
        return ""

    def contar(self):
        suma= self.valorA + self.valorB
        return suma