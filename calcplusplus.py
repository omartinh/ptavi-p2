import calcplus
import sys
import csv


def main():
    pass


if __name__ == '__main__':
    Calculadora = calcplus.CalculadoraPlus()
    NombreFichero = sys.argv[1]
    with open(NombreFichero) as HojadeCalculo:
        Operaciones = csv.reader(HojadeCalculo)
        for line in Operaciones:
            print(line)
            Operacion = line[0]
            if Operacion == "sumar" or Operacion == "suma":
                OperTotal = 0
                for next in line:
                    if next != "sumar" and next != "suma":
                        Calculadora.introAgmt(OperTotal, next, Operacion)
                        OperTotal = Calculadora.sumar()

            if Operacion == "restar" or Operacion == "resta":
                Entrar = True
                OperTotal = 0
                for next in line:
                    if next != "restar" and next != "resta":
                        Siguiente = next
                        Primero = line[1]
                        if next == Primero and Entrar:
                            Siguiente = -int(next)
                            Entrar = False
                        try:
                            Siguiente = int(Siguiente)
                        except ValueError:
                            sys.exit("Non numerical parameters")
                        Calculadora.introAgmt(OperTotal, Siguiente, Operacion)
                        OperTotal = Calculadora.restar()

            if Operacion == "multiplicar" or Operacion == "multiplica":
                OperTotal = 1
                for next in line:
                    if next != "multiplicar" and next != "multiplica":
                        Calculadora.introAgmt(OperTotal, next, Operacion)
                        OperTotal = Calculadora.multiplicar()
            if Operacion == "dividir" or Operacion == "divide":
                OperTotal = 1
                for next in line:
                    if next != "dividir" and next != "divide":
                        Siguiente = next
                        Primero = line[1]
                        if next == Primero:
                            OperTotal = Siguiente
                            Siguiente = 1
                        try:
                            Siguiente = int(Siguiente)
                        except ValueError:
                            sys.exit("Non numerical parameters")
                        Calculadora.introAgmt(OperTotal, Siguiente, Operacion)
                        OperTotal = Calculadora.dividir()
            print(OperTotal)
