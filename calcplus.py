#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import calcoo

calculadora=Calculadora # problemas a la hora de operar
fichero = open('fich_operaciones','r')
lineas = fichero.readlines()

for linea in lineas:
    elem = linea.split(',')
    operacion = elem[0]
    num1 = elem[1]
    num2=elem[2]
    
    if operacion == "suma":
        result = calcoo.suma(num1,num2)
        for signum in linea:
           result = result+ signum
            
        
print(result) 

