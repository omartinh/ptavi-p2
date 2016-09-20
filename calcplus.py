#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

calculadora=calcoohija.CalculadoraHija() # problemas a la hora de operar
fichero = open('fich_operaciones','r')
lineas = fichero.readlines()

for linea in lineas:
    elem = linea.split(',')
    operacion = elem[0]
    num1 = int(elem[1])
    num2=int(elem[2])
    nums=elem[3:]
    
    if operacion == "suma":
        print("___esta es la suma___")
        result = calculadora.suma(num1,num2)
        for num in nums: 
           result = result + int(num)
        print(result)
        
    elif operacion == "resta":
        print("___esta es la resta___")
        result = calculadora.resta(num1,num2)
        for num in nums:
            result = result - int(num)
        print(result)
        
    elif operacion == "multiplica":
        print("___esta es la multiplicacion___")
        result = calculadora.mult(num1,num2)
        for num in nums:
            result = result * int(num)
        print(result)
        
    elif operacion == "divide":
        print("___esta es la division___")
        if num2!=0:
            result = calculadora.div(num1,num2)
            for num in nums:
                if int(num)!= 0 :
                    result = result / int(num)
                    print(result)
                else:
                   print("Division by zero is not allowed")     
        else: 
            print("Division by zero is not allowed")    


