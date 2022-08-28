#!/usr/bin/python3

"""
Scripts de python para el módulo virtual de métodos numéricos suministrados
en la lectura fundamental 1, adaptados por Raúl Moncada.
"""

from math import *

#Acá se define la función a evaluar, recibe como parámetro X
def f(x):

    return 10*x**4-3*x*exp(x)-3*exp(x)

"""
Función que calcula p, se detiene al momento de que x es menor a la tolerancia 
o al llegar al número de iteraciones a evaluar
"""
def biseccion(f, punto_a, punto_b, tolerancia, iteraciones_evaluar):

    iteraciones=1
    while iteraciones <= iteraciones_evaluar:
        p=punto_a+(punto_b-punto_a)/2.0
        print("Iteración", "%03d" % iteraciones, ": p=", "%.14f" %p)
        if abs(f(p)) <= 1e-15 or (punto_b - punto_a)/2.0 < tolerancia:
            return p
        iteraciones += 1
        if f(punto_a) * f(p) > 0:
            punto_a=p
        else:
            punto_b=p
    print("Interacciones agotadas: Error")
    return

print("\n"+r"Metodo de la Bisección:"+"\n")
"""
Llama a la función bisección y le pasa como parámetros:
- La función a evaluar
- el intervalo inicial a evaluar (a,b)
- La tolerancia a error
- El número de itereaciones donde se quiere detener el proceso
"""
biseccion(f,-1.0, -0.25, 1e-4, 10)