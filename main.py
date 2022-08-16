import sys
from lex import Analyzer

def main():

    leer = str(input("Digite el codigo a evaluar: "))
   
    if len(leer) <= 0:
        print(leer + " No es un valor valido")
    else:
        analizador = Analyzer(leer)

        print("\n\n")
        print("Resultado del analisis lexico:")
        print("\n")
        print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))

        while analizador.character != "$":
            analizador.nextSymbol()
            print('{:<30}'.format(analizador.symbol) + '{:<30}'.format(analizador.tipoCadena(analizador.type)) + '{:<5}'.format(str(analizador.type)))

if __name__ == '__main__':
    main()