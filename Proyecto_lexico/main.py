import sys
from lex import Lexico

def main():

    entrada = str(input("Introduce codigo: "))
   
    if len(entrada) <= 0:
        print(entrada + " tiene errores, no valido")
    else:
        analyzer = Lexico(entrada)

        print("\n\n")
        print("**** Resultado: ")
        print("\n")
        print('{:<30}'.format("Entrada") + '{:<30}'.format("Simbolo") + '{:<5}'.format("Tipo"))

        while analyzer.character != "$":
            analyzer.nextSymbol()
            print('{:<30}'.format(analyzer.symbol) + '{:<30}'.format(analyzer.tipoCadena(analyzer.type)) + '{:<5}'.format(str(analyzer.type)))

if __name__ == '__main__':
    main()