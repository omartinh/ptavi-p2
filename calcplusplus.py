#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import sys
import calcoohija

fich = sys.argv[1]
calculadora = calcoohija.CalculadoraHija()   # problemas a la hora de operar

if __name__ == "__main__":

    try:
        fichero = open(fich, 'r')
    except:
        sys.exit("Error: fich name not found")

    with open(fich) as fichoperaciones:
        datos = csv.reader(fichoperaciones)
        for linea in datos:
            elem = linea
            operacion = elem[0]
            num1 = int(elem[1])
            nums = elem[2:]
            if operacion == "suma":
                result = num1
                for num in nums:
                    result = calculadora.suma(result, int(num))
                print(result)
            elif operacion == "resta":
                    result = num1
                    for num in nums:
                        if(result > int(num)):
                            result = calculadora.resta(result, int(num))
                        else:
                            result = 0  # cuando el primer valor es menor que el segundo dara 0
                    print(result)
            elif operacion == "multiplica":
                result = num1
                for num in nums:
                    result = calculadora.mult(result, int(num))
                print(result)
            elif operacion == "divide":
                    result = num1
                    for num in nums:
                        if int(num) != 0:
                            result = calculadora.div(result, int(num))
                        else:
                            sys.exit("Division by zero is not allowed")
                    print(result)
