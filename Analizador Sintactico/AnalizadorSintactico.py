import numpy as np

listalexico = list()
pila = list()
lisreglas = list()
auxregl = list()
matrizreglas = list()

class Regla:
    def __init__(self, aux, num, elementos, regla):
        self.aux = aux
        self.num = num
        self.elementos = elementos
        self.regla = regla

def reglas():
    file = open('compilador.lr', 'r')
    line = file.readlines()
    for l in line:
        l = l.rstrip()
        matrizreglas.append(l.split('\t'))
    # for i in range (len(matrizreglas)):
    #     for j in range(len(matrizreglas[i]):
    #         matrizreglas[i][j] = int(matrizreglas[i][j])
    # file.close()

    for i in range (len(matrizreglas)):
        for j in range(len(matrizreglas[i])):
            matrizreglas[i][j] = int(matrizreglas[i][j])
    file.close()

def auxreglas():
    n = 1
    file = open('rgl.txt', 'r')
    line = file.readlines()
    for l in line:
        l = l.rstrip()
        auxreglas.append(l.split('\t'))
    for o in auxreglas:
        o = Regla(n, int(o[0]), int(o[1]), str(o[2]))
        n += 1
        lisreglas.append(o)
    file.close()

def buscar(str):
    for objetoLeixco in listalexico:
        if objetoLeixco == str:
            return objetoLeixco
        else:
            pass

class elementoPila:
    def __init__(self, cadena, tipo, pos):
        self.cad = cadena
        self.tipo = tipo
        self.pos = pos
    def __repr__(self):
        return str(self.__dict__)
class terminal(elementoPila):
    def __init__(self, cadena, tipo, pos):
        elementoPila.__init__(self, cadena, tipo, pos)

class noterminal(elementoPila):
    def __init__(self, cadena, tipo, pos):
        elementoPila.__init__(self, cadena, tipo, pos)

class estado(elementoPila):
    def __init__(self, cadena, tipo, pos, estado):
        elementoPila.__init__(self, cadena, tipo, pos)
        self.estado = estado