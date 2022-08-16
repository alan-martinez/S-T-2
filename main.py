import sys
from lex import Analyzer

def main():

    leer = str(input("Dijite el codigo a evaluar: "))
   
    if len(leer) <= 0:
        print(leer + " No es un valor valido")
    else:
        analizador = Analyzer(leer)

        print("\n\n")
        print("Resultado del analisis lexico:")
        print("\n")
        print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))

        while analizador.caracter != "$":
            analizador.nextSymbol()
            print('{:<30}'.format(analizador.simbolo) + '{:<30}'.format(analizador.tipoCadena(analizador.tipo)) + '{:<5}'.format(str(analizador.tipo)))

if __name__ == '__main__':
    main()