#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
    
    def mult (self, op1, op2):
        return op1 * op2
        
    def div (self, op1, op2):
        return op1 / op2        
          
if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])     
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = CalculadoraHija()
        
    if  sys.argv[2] == "resta":
        resultado=calculadora.resta(operando1,operando2)
    elif sys.argv[2]=="suma":
        resultado=calculadora.suma(operando1,operando2)
    elif sys.argv[2]=="divide":
        if sys.argv[3] == "0":
            sys.exit("Division by zero is not allowed")
        else:
           resultado = calculadora.div(operando1, operando2)
    elif sys.argv[2]=="multiplica":
        resultado = calculadora.mult(operando1, operando2)         
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicacion o division.')
        
    print(resultado)
    

