#!/usr/bin/python3

import sys

archivo = sys.argv[1]
cantPalabras = 0
f = open(archivo)
for linea in f:
    a = linea.strip().split()
    cantPalabras += len(a)

print("Cantidad de palabras del archivo %s es %d" % (archivo,cantPalabras))
