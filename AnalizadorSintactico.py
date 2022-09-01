import numpy as np

listLexico = list()
pila = list()

class elementoDePila:
    def __init__(self, cadena, tipo, pos):
        self.cad = cadena
        self.tipo = tipo
        self.pos = pos

    def __repr__(self) -> str:
        return self.__dict__

class terminal(elementoDePila):
    def __init__(self, cadena, tipo, pos):
        elementoDePila.__init__(self, cadena, tipo, pos)

class noTerminal(elementoDePila):
    def __init__(self, cadena, tipo, pos):
        elementoDePila.__init__(self, cadena, tipo, pos)

class estado(elementoDePila):
    def __init__(self, cadena, tipo, pos, estado):
        elementoDePila.__init__(self, cadena, tipo, pos)
        self.estado = estado

class analizador:
    def __init__(self, input):
        self.input = input
        self.estado = 0
        self.i = 0
        self.tmp = ""
        self.continua = True
        self.tipo = list() 
        self.aux = 0
    
    def reservada(self):
        res = self.tmp
        if "while" == res:
            self.tipo.append(20)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        

    