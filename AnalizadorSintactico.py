import numpy as np
from tablas import *

listLexico = list()

tbl2 = np.array(tabla3)

tbl = np.array(tabla2)

lrt = np.array(lr)

pila = list()

class stackElement:
    def __init__(self, cadena, tipo, posicion):
        self.cad = cadena
        self.tipo = tipo
        self.posicion = posicion

    def __repr__(self):
        return str(self.__dict__)

class terminal(stackElement):
    def __init__(self, cadena, tipo, posicion):
        stackElement.__init__(self, cadena, tipo, posicion)

class noterminal(stackElement):
    def __init__(self, cadena, tipo, posicion):
        stackElement.__init__(self, cadena, tipo, posicion)

class estado(stackElement):
    def __init__(self, cadena, tipo, posicion, estado):
        stackElement.__init__(self, cadena, tipo, posicion)
        self.estado = estado


class analizador:
    def __init__(self, input):
        self.input_analizada = input +"~"
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        self.tipo=list()
        self.aux = 0
        

    def lexicoAnalizer(self):
        
        while self.continua:
            c = self.input_analizada[self.i]
            
            if self.edo == 0:                                                   #General
                if c >= "0" and c <= "9":
                    self.edo = 1
                    self.tmp +=c
                    
                elif c == "E":
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = noterminal("E",self.tipo[-1],0)
                    listLexico.append(objlex)
                    self.continua = False
                    
                elif c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_":
                    self.edo = 4
                    self.tmp += c
                elif c == " ":
                    self.edo = 0

                elif c == "'" or c=='"':
                    self.edo = 9
                    self.tmp +=c

                elif (c == "*") or (c == "/"):
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(6)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()

                elif (c == "=") or (c == "!"):    
                    self.clean()
                    self.edo = 5
                    self.tmp +=c
                
                elif (c == "<") or (c == ">"):    
                    self.clean()
                    self.edo = 6
                    self.tmp +=c
                elif (c == "|"):    
                    self.clean()
                    self.edo = 7
                    self.tmp +=c
                elif (c == "&"):    
                    self.clean()
                    self.edo = 8
                    self.tmp +=c

                
                elif (c == "+") or (c == "-"):
                    if self.aux == 1:
                        self.tipo.append(1)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()

                    elif self.aux == 2:
                        
                        self.clean()
                    if c =="+":
                        self.tmp +=c
                        self.tipo.append(1)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                        self.edo = 0
                    else:
                        self.tmp +=c
                        self.tipo.append(5)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                        self.edo = 0
                    
                
                elif c == "$":
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.edo = 0
                elif c == "(":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.edo = 0
                    self.clean()
                elif c == ")":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.edo = 0

                elif c == "{":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.edo = 0
                    self.clean()
                elif c == "}":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.edo = 0
                    
                elif c == "~":
                    self.continua=False
                
            elif self.edo == 1:                                     #Numeros
                if c >= "0" and c <= "9":
                    self.edo = 1
                    self.tmp +=c

                elif c == ".":
                    self.edo = 2
                    self.tmp += c

                elif c == " ":
                    self.edo = 0
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()

                elif c == "~":
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.continua = False
                else:
                    self.edo = 0
                    self.aux = 1
                    self.i-=1

            elif self.edo == 2:                                 #Float
                if c >= "0" and c <= "9":
                    self.edo = 3
                    self.tmp +=c
            
            elif self.edo == 3:                                 #Terminacion Num
                if c >= "0" and c <= "9":
                    self.edo = 3
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.i-=1

            elif self.edo == 4:                                                                         #Letras
                if c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_" or c >= "0" and c <= "9":
                    self.edo = 4
                    self.tmp +=c
                elif c == " ":
                    self.reservado()
                    self.clean()
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    self.reservado()
                    self.continua = False
                else:
                    self.reservado()
                    self.edo = 0
                    self.clean()
                    self.i-=1
                    self.aux=2
            
            elif self.edo == 5:                                 #Terminacion Simbolo
                if c == "=":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(11)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.edo = 0

                elif c == "~":
                    if self.input_analizada[self.i-1]=="=":
                        self.edo = 0
                        self.tipo.append(18)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                    else:
                        self.clean()
                    self.continua = False
                else:
                    if self.input_analizada[self.i-1]=="=":
                        self.edo = 0
                        self.tipo.append(18)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                    else:
                        self.clean()
                    self.i-=1

            elif self.edo == 6:                                 #Terminacion Simbolo
                if c == "=":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.edo = 0

                elif c == "~":
                    self.edo = 0
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.continua = False
                else:
                    self.edo = 0
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                    self.i-=1

            elif self.edo == 7:                                 #Terminacion Simbolo
                if c == "|":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(8)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.clean()
                    self.i-=1

            elif self.edo == 8:                                 #Terminacion Simbolo
                if c == "&":
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(9)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.edo = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 0
                    self.clean()
                    self.i-=1
            
            elif self.edo == 9:                                 #Terminacion Simbolo
                if c == "'" or c == '"':
                    self.edo = 0
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.edo = 9
                    self.tmp +=c
                    

            self.i+=1

        print(self.edo)
        print(self.input_analizada)
        print(self.tmp)
        self.edo = 0
        self.i = 0
        self.tmp =""
        self.continua = True

    def reservado(self):
        strid = self.tmp
        if "while" == strid:
            self.tipo.append(20)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "if" == strid:
            self.tipo.append(19)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "return" == strid:
            self.tipo.append(21)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "else" == strid:
            self.tipo.append(22)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "int" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "float" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        elif "void" == strid:
            self.tipo.append(4)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
            print(strid, " Reservada Tipo", self.tipo[-1])
        else:
            self.tipo.append(0)
            objlex = terminal(self.tmp, self.tipo[-1], 0)
            listLexico.append(objlex)
    
    def clean(self):
        self.edo = 0
        self.tmp =""
        self.continua = True

    def find(self, str):
        for objlex in listLexico:
            if objlex.cad == str:
                return objlex
            else:
                pass



cad = "a+b+c"
print("Cadena ingresada: ", cad)
particionEntrada = cad.split()
particionEntrada.append("$")

particionEntrada.append("E")
for i in range (len(particionEntrada)):
    cadena = analizador(particionEntrada[i])
    cadena.lexicoAnalizer()

particionEntrada2 = list()
print('* * * * * * * * * * * * * * * * * *')
print("Leido        Tipo        posicion")
for objlex in listLexico:
    print(objlex.cad, f"{'':>9}", objlex.tipo, f"{'':>9}", objlex.posicion)
    particionEntrada2.append(objlex.cad)
particionEntrada.clear()    
particionEntrada=particionEntrada2
auxelimna = (len(particionEntrada)-2)*2
fila = 0
columna = 0
accion =0
acept = False

pila.append(cadena.find("$"))
pila.append(estado("0",0,0,0))


i=0

while True:
    fila = pila[-1].tipo
    columna = cadena.find(particionEntrada[i])
    accion = tbl2[fila,columna.tipo]
    accion= estado(str(accion), accion, accion, accion)
    if accion.estado == 0:
        print('Error')
        break
    elif accion.estado > 0:
        i+=1
        pila.append(columna)
        pila.append(accion)
        print('Desplazamiento')
    elif accion.estado  <0:
        if accion.estado == -1:
            print('Aceptado')
            break
        else:
            print('Regla')
            while auxelimna != 0:
                pila.pop()
                auxelimna-=1
            particionEntrada[i-1]="E"
            i-=1
