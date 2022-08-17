class Type:
    def __init__(self):
        self.ERROR = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.CADENA = 3
        self.TIPO = 4
        self.OPSUMA = 5
        self.OPRESTA = 6
        self.OPMULTIPLICACION = 7
        self.OPDIVISION = 8
        self.OPOR = 9
        self.OPAND = 10
        self.OPNOT = 11
        self.OPMAYORQ = 12
        self.OPMENORQ = 13
        self.OPMAYOROIGUAL = 14
        self.OPMENOROIGUAL = 15
        self.OPIGUAL = 16
        self.OPESIGUAL = 17
        self.OPESDIFERENTE = 18
        self.PUNTOYCOMA = 19
        self.COMA = 20
        self.PARENTESIOSABIERTO = 21
        self.PARENTESISCERRADO = 22
        self.LLAVEABIERTA = 23
        self.LLAVECERRADA = 24
        self.BRACKETABIERTO = 25
        self.BRACKETCERRADO = 26
        self.DOSPUNTOS = 27
        self.IF = 50
        self.WHILE = 51 
        self.RETURN = 52
        self.ELSE = 53
        self.INT = 54
        self.FLOAT = 55
        self.VOID = 56
        self.PESO = 34
        
        
class Lexico(Type):
    def __init__(self, input, indice = 0, continua = True, character = "", state = 1, symbol = "", type = -1, typeString = ""): 
        self.input = input
        self.indice = indice
        self.continua = continua
        self.character = character
        self.state = state
        self.symbol = symbol
        self.type = type
        self.typeString = typeString

        Type.__init__(self)

    def tipoCadena(self, type):
        self.typeString = ""

        switch = {
            self.ERROR: self.message_ERROR,
            self.IDENTIFICADOR: self.message_IDENTIFICADOR,
            self.ENTERO: self.message_ENTERO,
            self.REAL: self.message_REAL,
            self.CADENA: self.message_CADENA,
            self.OPSUMA: self.message_OPMAS,
            self.OPRESTA: self.message_OPMENOS,
            self.OPMULTIPLICACION: self.message_OPMULTI,
            self.OPDIVISION: self.message_OPDIV,
            self.OPMAYORQ: self.message_MAYORQUE,
            self.OPMENORQ: self.message_MENORQUE,
            self.OPMAYOROIGUAL: self.message_MAYORIGUAL,
            self.OPMENOROIGUAL: self.message_MENORIGUAL,
            self.OPOR: self.message_OR,
            self.OPAND: self.message_AND,
            self.OPNOT: self.message_NOT,
            self.OPIGUAL: self.message_IGUAL,
            self.OPESIGUAL: self.message_ESIGUAL,
            self.OPESDIFERENTE: self.message_ESDIFERENTE,
            self.PUNTOYCOMA: self.message_PUNTOCOMA,
            self.COMA: self.message_COMA,
            self.PARENTESIOSABIERTO: self.message_PARENTESISABIERTO,
            self.PARENTESISCERRADO: self.message_PARENTESISCERRADO,
            self.LLAVEABIERTA: self.message_LLAVEABIERTA,
            self.LLAVECERRADA: self.message_LLAVECERRADA,
            self.BRACKETABIERTO: self.message_BRACKETABIERTO,
            self.BRACKETCERRADO: self.message_BRACKETCERRADO,
            self.DOSPUNTOS: self.message_DOSPUNTOS,
            self.IF: self.message_IF,
            self.WHILE: self.message_WHILE,
            self.RETURN: self.message_RETURN,
            self.ELSE: self.message_ELSE,
            self.INT: self.message_INT,
            self.FLOAT: self.message_FLOAT,
            self.VOID: self.message_VOID,
            self.PESO: self.message_PESO
        }

        switch[type]()

        return self.typeString

    def nextSymbol(self):
        self.state = 1
        self.continua = True
        self.symbol = ""
        self.type = -1

        while self.continua:
            self.character = self.nextCharacter()

            switch = {
                0: self.state00,
                1: self.state01,
                2: self.state02,
                3: self.state03,
                4: self.state04,
                5: self.state05,
                6: self.state06,
                7: self.state07,
                8: self.state08,
                9: self.state09,
                10: self.state10,
                11: self.state11,
                
            }

            switch.get(self.state, self.error)()

        if self.type < 11:

            switch = {
                -1: self.error, # ERROR
                2: self.tipo00, # Identificador
                3: self.tipo01, # Entero
                5: self.tipo02, # Real
                12: self.tipo09 # Peso
            }

            switch.get(self.state, self.error)()


    def nextCharacter(self):
        if self.terminado():
            return "$"
        character = self.input[self.indice]
        self.indice += 1
        return character

    def nextState(self, state):      
        self.state = state
        self.symbol += self.character

        
    def retroceso(self):
        if not self.esPeso(self.character):
            self.indice -= 1
        self.continua = False

    def terminado(self):
        return self.indice >= len(self.input)

    def esPeso(self, character):
        return character == "$"

    def esEspacio(self, character):
        return character == " "

    def esCaracter(self, character):
        return ord(character) == 32 or ord(character) == 33 or ord(character) >= 35 and ord(character) <= 126

    def esLetra(self, character):
        return character.isalpha() or character == "_"

    def esNumero(self, character):
        return character.isdigit()

    def esPunto(self, character):
        return character == "."
   
    # TODO posibles estados

    def state00(self):
        self.continua = False

    def state01(self):
        if self.esPeso(self.character):
            self.nextState(0)
        elif self.esLetra(self.character):
            self.nextState(2)
        elif self.esNumero(self.character):
            self.nextState(3)
        elif self.esEspacio(self.character):
            self.state = 1
        else:
            self.symbol += self.character
            self.continua = False

    def state02(self):
        if self.esLetra(self.character):
            self.nextState(2)
        elif self.esNumero(self.character):
            self.nextState(2)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state03(self):
        if self.esNumero(self.character):
            self.nextState(3)
        elif self.esPunto(self.character):
            self.type = -1
            self.nextState(4)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state04(self):
        if self.esNumero(self.character):
            self.nextState(5)
        else:
            self.retroceso()

    def state05(self):
        if self.esNumero(self.character):
            self.nextState(5)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state06(self):
        if self.esCaracter(self.character):
            self.nextState(6)
        else:
            self.retroceso()
    
    def state07(self):
        self.retroceso()

    def state08(self):
        self.retroceso()

    def state09(self):
        self.retroceso()

    def state10(self):
        self.retroceso()

    def state11(self):
        self.retroceso()
        
    # Tipos validos

    def error(self):
        self.type = self.ERROR

    def tipo00(self):
        self.type = self.IDENTIFICADOR

    def tipo01(self):
        self.type = self.ENTERO
    
    def tipo02(self):
        self.type = self.REAL

    def tipo09(self):
        self.type = self.PESO

    
    # Tipos posibles
    
    def message_PESO(self): # Cortar la cadena
        self.typeString = "Fin de Cadena"

    def message_ERROR(self):
        self.typeString = "No esta definido"
    
    def message_IDENTIFICADOR(self):
        self.typeString = "Identificador"

    def message_ENTERO(self):
        self.typeString = "Entero"

    def message_REAL(self):
        self.typeString = "Real"
        
    def message_CADENA(self):
        self.tipoCadenaMensaje = "Cadena"

    def message_OPMAS(self):
        self.tipoCadenaMensaje = "Mas"

    def message_OPMENOS(self):
        self.tipoCadenaMensaje = "Menos"

    def message_OPMULTI(self):
        self.tipoCadenaMensaje = "Multiplicacion"

    def message_OPDIV(self):
        self.tipoCadenaMensaje = "Division"

    def message_MAYORQUE(self):
        self.tipoCadenaMensaje = "Mayor que"

    def message_MENORQUE(self):
        self.tipoCadenaMensaje = "Menor que"

    def message_MAYORIGUAL(self):
        self.tipoCadenaMensaje = "Mayor o igual que"

    def message_MENORIGUAL(self):
        self.tipoCadenaMensaje = "Menor o igual que"

    def message_OR(self):
        self.tipoCadenaMensaje = "Or"

    def message_AND(self):
        self.tipoCadenaMensaje = "And"

    def message_NOT(self):
        self.tipoCadenaMensaje = "Not"

    def message_IGUAL(self):
        self.tipoCadenaMensaje = "Igual"

    def message_ESIGUAL(self):
        self.tipoCadenaMensaje = "Es igual a"

    def message_ESDIFERENTE(self):
        self.tipoCadenaMensaje = "Es diferente de"

    def message_PUNTOCOMA(self):
        self.tipoCadenaMensaje = "Punto y coma"

    def message_COMA(self):
        self.tipoCadenaMensaje = "Coma"

    def message_PARENTESISABIERTO(self):
        self.tipoCadenaMensaje = "Parentesis abierto"

    def message_PARENTESISCERRADO(self):
        self.tipoCadenaMensaje = "Parentesis abierto"

    def message_LLAVEABIERTA(self):
        self.tipoCadenaMensaje = "Llave abierta"

    def message_LLAVECERRADA(self):
        self.tipoCadenaMensaje = "Llave cerrada"

    def message_BRACKETABIERTO(self):
        self.tipoCadenaMensaje = "Bracket abierto"

    def message_BRACKETCERRADO(self):
        self.tipoCadenaMensaje = "Bracket cerrado"

    def message_DOSPUNTOS(self):
        self.tipoCadenaMensaje = "Dos puntos"

    def message_IF(self):
        self.tipoCadenaMensaje = "If"

    def message_WHILE(self):
        self.tipoCadenaMensaje = "While"

    def message_RETURN(self):
        self.tipoCadenaMensaje = "Return"

    def message_ELSE(self):
        self.tipoCadenaMensaje = "Else"

    def message_INT(self):
        self.tipoCadenaMensaje = "Int"

    def message_FLOAT(self):
        self.tipoCadenaMensaje = "Float"

    def message_VOID(self):
        self.tipoCadenaMensaje = "Void"
