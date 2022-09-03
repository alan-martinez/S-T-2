import numpy as np

listLexico = list()

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
        self.input = input +"~"
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
                        self.estado = 0
                    else:
                        self.tmp +=c
                        self.tipo.append(5)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                        self.estado = 0

                elif c == "$":
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.estado = 0
                elif c == "(":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.estado = 0
                    self.clean()
                elif c == ")":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.estado = 0

                elif c == "{":
                    self.tmp +=c
                    self.tipo.append(14)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.estado = 0
                    self.clean()
                elif c == "}":
                    self.tmp +=c
                    self.tipo.append(15)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.estado = 0
                    

                
                elif c == "~":
                    self.continua=False
            
            elif self.estado == 1:                                     #Numeros
                if c >= "0" and c <= "9":
                    self.estado = 1
                    self.tmp +=c

                elif c == ".":
                    self.estado = 2
                    self.tmp += c

                elif c == " ":
                    self.estado = 0
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                    #self.tmp +=c

                elif c == "~":
                    self.tipo.append(1)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.continua = False
                else:
                    self.estado = 0
                    self.aux = 1
                    self.i-=1

            elif self.estado == 2:                                 #Float
                if c >= "0" and c <= "9":
                    self.estado = 3
                    self.tmp +=c
            
            elif self.estado == 3:                                 #Terminacion Num
                if c >= "0" and c <= "9":
                    self.estado = 3
                    self.tmp +=c
                    self.tipo.append(2)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.estado = 0
                    self.i-=1

            elif self.estado == 4:                                                                         #Letras
                if c >= "a" and c <= "z" or c >= "A" and c <= "Z" or c == "_" or c >= "0" and c <= "9":
                    self.estado = 4
                    self.tmp +=c
                elif c == " ":
                    self.reservada()
                    self.clean()
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    self.reservada()
                    self.continua = False
                else:
                    self.reservada()
                    self.estado = 0
                    self.clean()
                    self.i-=1
                    self.aux=2
            
            elif self.estado == 5:                                 #Terminacion Simbolo
                if c == "=":
                    self.estado = 0
                    self.tmp +=c
                    self.tipo.append(11)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    if self.cadena_analizada[self.i-1]=="=":
                        self.estado = 0
                        #self.tmp +=c
                        self.tipo.append(18)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                    else:
                        self.clean()
                    self.continua = False
                else:
                    if self.cadena_analizada[self.i-1]=="=":
                        self.estado = 0
                        #self.tmp +=c
                        self.tipo.append(18)
                        objlex = terminal(self.tmp, self.tipo[-1], 0)
                        listLexico.append(objlex)
                        self.clean()
                    else:
                        self.clean()
                    self.i-=1

            elif self.estado == 6:                                 #Terminacion Simbolo
                if c == "=":
                    self.estado = 0
                    self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    self.estado = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    #self.clean()
                    self.continua = False
                else:
                    self.estado = 0
                    #self.tmp +=c
                    self.tipo.append(7)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                    self.i-=1

            elif self.estado == 7:                                 #Terminacion Simbolo
                if c == "|":
                    self.estado = 0
                    self.tmp +=c
                    self.tipo.append(8)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.estado = 0
                    self.clean()
                    self.i-=1

            elif self.estado == 8:                                 #Terminacion Simbolo
                if c == "&":
                    self.estado = 0
                    self.tmp +=c
                    self.tipo.append(9)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                
                elif c == " ":
                    self.estado = 0
                    #self.tmp +=c

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.estado = 0
                    self.clean()
                    self.i-=1
            
            elif self.estado == 9:                                 #Terminacion Simbolo
                if c == "'" or c == '"':
                    self.estado = 0
                    self.tmp +=c
                    self.tipo.append(3)
                    objlex = terminal(self.tmp, self.tipo[-1], 0)
                    listLexico.append(objlex)
                    self.clean()
                

                elif c == "~":
                    
                    self.continua = False
                else:
                    self.estado = 9
                    self.tmp +=c
                    

            self.i+=1
        
        print(self.estado)
        print(self.input)
        print(self.tmp)
        self.estado = 0
        self.i = 0
        self.tmp =""
        self.continua = True
        bandera =0


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


entrada = "a+b+c"
print("Cadena ingresada: ", entrada)
formatearCadena = entrada.split()
formatearCadena.append("$")

formatearCadena.append("E")
for i in range (len(formatearCadena)):
    cadena = analizador(formatearCadena[i])
    cadena.analizador()

formatearCadena2 = list()
print('------------------------')
print("Leido        Tipo        Pos")
for objlex in listLexico:
    print(objlex.cad, f"{'':>9}", objlex.tipo, f"{'':>9}", objlex.pos)
    formatearCadena2.append(objlex.cad)
formatearCadena.clear()    
formatearCadena=formatearCadena2
auxelimna = (len(formatearCadena)-2)*2
fila = 0
columna = 0
accion =0
acept = False

pila.append(cadena.find("$"))
pila.append(estado("0",0,0,0))


i=0


while True:
    #print(pila)
    fila = pila[-1].tipo
    columna = cadena.find(formatearCadena[i])
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
            formatearCadena[i-1]="E"
            i-=1