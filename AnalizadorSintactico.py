import numpy as np

listLexico = list()
pila = list()

tabla3 = [2, 0, 0, 1],\
        [0, 0, -1, 0],\
        [0, 3, -3, 0],\
        [2, 0, 0, 4],\
        [0, 0, -2, 0]
tbl2 = np.array(tabla3)



tabla2 = [2, 0, 0, 1],\
        [0, 0, -1, 0],\
        [0, 3, 0, 0],\
        [4, 0, 0, 0],\
        [0, 0, -2, 0]
tbl = np.array(tabla2)

lr = [2, 0, 1],\
     [0, -1, 0],\
     [0, -2, 0]

lrt = np.array(lr)

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
    
    def analizador(self):
        while self.continua:
            c = self.input[self.i]

            if self.estado == 0:
                if c >= "0" and c <= "9":
                    self.estado = 1
                    self.tmp += c
                
                elif c == "E":
                    self.tmp += c
                    self.tipo.append(3)
                    objlex = noTerminal("E",self.tipo[-1],0)
                    listLexico.append(objlex)
                    self.continua = False
                elif c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_":
                    self.estado = 4
                    self.tmp += c
                elif c == " ":
                    self.estado = 0
                elif c == "'" or c=='"':
                    self.estado = 9
                    self.tmp += c
                elif (c == "*") or (c == "/"):
                    self.estado = 0
                    self.tmp += c
                    self.tipo.append(6)
                    objlex = terminal(self.tmp, self.tipo[-1],0)
                    listLexico.append(objlex)
                    self.clean()
                elif (c == "=") or (c == "!"): #Para los simbolos
                    self.clean()
                    self.estado = 5
                    self.tmp += c
                elif (c == "<") or (c == ">"):
                    self.clean()
                    self.estado = 6
                    self.tmp += c
                elif (c == "|"):
                    self.clean()
                    self.estado = 7
                    self.tmp += c
                elif (c == "&"):
                    self.clean()
                    self.estado = 8
                    self.tmp += c
                elif (c == "+") or (c == "-"):
                    if self.aux == 1:
                        self.tipo.append(1)
                        objlex = terminal(self.tmp, self.tipo[-1],0)
                        

    def reservada(self):
        res = self.tmp
        if "while" == res:
            self.tipo.append(20)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "if" == res:
            self.tipo.append(19)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "return" == res:
            self.tipo(19)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "else" == res:
            self.tipo(22)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "int" == res:
            self.tipo(4)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "float" == res:
            self.tipo(4)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        elif "void" == res:
            self.tipo(4)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
            print(res, " Palabra reservada de tipo", self.tipo[-1])
        else:
            self.tipo.append(0)
            objlex = terminal(self.tmp, self.tipo[-1],0)
            listLexico.append(objlex)
    
    def clean(self):
        self.estado = 0
        self.tmp = ""
        self.continua = True
    
    def find(self, str):
        for objlex in listLexico:
            if objlex == str:
                return objlex
            else:
                pass