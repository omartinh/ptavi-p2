#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich=sys.argv[1]
calculadora=calcoohija.CalculadoraHija() #problemas a la hora de operar

if __name__ == "__main__":

    try:
        fichero = open(fich,'r')
    except:
        sys.exit("Error: fich name not found")

    
    lineas = fichero.readlines()   
    
    for linea in lineas:
        elem = linea.split(',')
        operacion = elem[0]
        num1 = int(elem[1])
        num2=int(elem[2])
        nums=elem[3:]
    
        if operacion == "suma":
            result = calculadora.suma(num1,num2)
            for num in nums: 
                result = calculadora.suma(result,int(num))
            print(result)
        
        elif operacion == "resta":
            if(num1>num2):
                result = calculadora.resta(num1,num2)
                for num in nums:
                    result = calculadora.resta(result,int(num))
                print(result)
            else:
                print("Error operandos resta" )
        
        elif operacion == "multiplica":
            result = calculadora.mult(num1,num2)
            for num in nums:
                result = calculadora.mult(result,int(num))
            print(result)
        
        elif operacion == "divide": 
            if num2!=0:
                result = calculadora.div(num1,num2)
                for num in nums:
                    if int(num)!= 0 :
                        result = calculadora.div(result,int(num))
                        print(result)
                    else:
                        print("Division by zero is not allowed")     
            else: 
                print("Division by zero is not allowed")    


