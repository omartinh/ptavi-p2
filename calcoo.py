#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def suma (self, op1, op2):
        return op1 + op2
        
    def resta (self, op1 , op2):
        return op1 - op2
        
          
if __name__ == "__main__":
    
    operando1 = int(sys.argv[1])
    operando2 = int(sys.argv[3])
    calculadora=Calculadora()
    if  sys.argv[2] == "resta":
        resultado=calculadora.resta(operando1,operando2)
    elif sys.argv[2]=="suma":
        resultado=calculadora.suma(operando1,operando2)
    print(resultado)
    

