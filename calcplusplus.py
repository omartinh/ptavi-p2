#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import sys
import calcoohija

fich = sys.argv[1]
calculadora = calcoohija.CalculadoraHija()   # problemas a la hora de operar

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
        num2 = int(elem[2])
        nums = elem[3:]
        if operacion == "suma":
            result = calculadora.suma(num1, num2)
            for num in nums:
                result = result + int(num)
            print(result)
        elif operacion == "resta":
            if(num1 > num2):
                result = calculadora.resta(num1, num2)
                for num in nums:
                    result = result - int(num)
                print(result)
            else:
                print("Error operandos resta")
        elif operacion == "multiplica":
            result = calculadora.mult(num1, num2)
            for num in nums:
                result = result * int(num)
            print(result)
        elif operacion == "divide":
            if num2 != 0:
                result = calculadora.div(num1, num2)
                for num in nums:
                    if int(num) != 0:
                        result = result / int(num)
                        print(result)
                    else:
                        print("Division by zero is not allowed")
            else:
                print("Division by zero is not allowed")
