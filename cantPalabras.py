#!/usr/bin/python3

cantPalabras = 0
f = open('datos.txt','r')
for linea in f:
    a = linea.strip().split()
    cantPalabras += len(a)

print("Cantidad de Palabras del archivo datos.txt es %d" % cantPalabras)
