class Type:
    def __init__(self):
        self.ERROR = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.INT = 12
        self.FLOAT = 13

class Analyzer(Type):
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
            self.FLOAT: self.message_FLOAT,
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
            self.character = self.siguienteCaracter()
            
            switch = {
                0: self.state00,
                1: self.state01,
                2: self.state02
            }
            switch.get(self.state, self.error)()
        
        if self.tipo < 11:
    
            switch = {
                -1: self.error, # ERROR
                2: self.caso00, # Identificador
                3: self.caso01, # Entero
                5: self.caso02, # Real
            }
            switch.get(self.state, self.error)()
    
    def verificarPalabraReservada(self, symbol):
        palabrasReservadas = {
        "int": self.INT,
        "float": self.FLOAT
        }
        self.type = palabrasReservadas.get(symbol, self.type)


    def siguienteCaracter(self):
        if self.terminado():
            return "$"
        character = self.input[self.indice]
        self.indice += 1
        return character

    def siguienteEstado(self, state):      
        self.state = state
        self.symbol += self.character
    
    def retroceso(self):
        if not self.esPeso(self.character):
            self.indice -= 1
        self.continua = False
        self.verificarPalabraReservada(self.symbol)
    
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
    
    #Se definen todos los posibles estados
    def state00(self):
        self.continua = False
    
    def state01(self):
        if self.esPeso(self.character):
            self.siguienteEstado(0)
        elif self.esLetra(self.character):
            self.siguienteEstado(2)
        elif self.esNumero(self.character):
            self.siguienteEstado(3)
        elif self.esEspacio(self.character):
            self.state = 1
        else:
            self.symbol += self.character
            self.continua = False
    
    def state02(self):
        if self.esLetra(self.character):
            self.siguienteEstado(2)
        elif self.esNumero(self.character):
            self.siguienteEstado(2)
        elif self.esEspacio(self.character):
            self.continua = False
            self.verificarPalabraReservada(self.symbol)
        else:
            self.retroceso()
    
    #Tipos validos que pueden tomar
    def error(self):
        self.type = self.ERROR
    
    def caso00(self):
        self.type = self.IDENTIFICADOR
    
    def caso01(self):
        self.type = self.ENTERO
        
    def caso02(self):
        self.type = self.REAL
    
    #Tipos de mensajes
    def message_PESO(self):
        self.typeString = "Fin de Cadena"
    def message_ERROR(self):
        self.typeString = "Undefined"
    def message_IDENTIFICADOR(self):
        self.typeString = "Identificador"
    def message_ENTERO(self):
        self.typeString = "Entero"
    def message_REAL(self):
        self.typeString = "Real"
    def message_INT(self):
        self.typeString = "Int"

    def message_FLOAT(self):
        self.typeString = "Float"