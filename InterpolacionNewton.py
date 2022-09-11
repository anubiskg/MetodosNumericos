#!/usr/bin/python3

from math import *
from prettytable import PrettyTable
import csv


tabla_resultados = PrettyTable()
columnas = []

def NewtonPol(datos):
    n = len(datos) - 1
    
    

    F = [[0 for x in datos] for x in datos]


    for i, p in enumerate(datos):
        F[i][0] = p[1]


    for i in range (1, n+1):
        for j in range (1, i+1):
            F[i][j] = (F[i][j-1]-F[i-1][j-1]) / (datos[i][0] - datos [i-j][0])
            
    def L(k, x):
        out = 1.0
        for i, p in enumerate(datos):
            if i <= k:
                out *= (x-p[0])
        return out

    def P(x):
        newt = 0.0
        for i in range(1, n+1):
            newt += F[i][i] * L(i-1, x)
        return newt + F[0][0]

    return F, P

"""
Se crea esta función para cargar los datos desde el archivo
'interpolacion_newton.csv', que debe tener los valores separados por comas
"""
datost = []
with open('interpolacion_newton.csv') as file:
   reader = csv.reader(file)
   datost = [(float(row[0]), float(row[1])) for row in reader]
print(datost)


T, P = NewtonPol(datost)

print ("Tabla de diferencias divididas:" + "\n")

for i in range (len(T)):
    columnas.append(f"Diferencia {i}")
    tabla_resultados.add_row(T[i])

tabla_resultados.field_names = columnas

print(tabla_resultados)
#Esto no es relevante por el momento
#print("Polinomio en x=10")
#print(P(10.0))
