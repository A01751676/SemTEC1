# -*- coding: utf-8 -*-
"""
Equipo 1
    Ana Patricia Islas Mainou A01751676
    Luis Humberto Romero Pérez A01752789
    Rodrigo Mejía Jiménez A01752789
"""

def obtenerdatos():
    archivo = open("GEH.txt", "r")
    contenido = ""
    
    # leer archivo 
    for linea in archivo:
        contenido = contenido + " " + linea.strip() + " "
        
    archivo.close()
    
    # arreglar datos
    contenido = contenido.split()
    
    for i in range(0,len(contenido)):
        contenido[i] = contenido[i].upper()
    
    return contenido
        

def conteo(contenido):
    palabras = list(set(contenido))
    repeticion =[]
    
    for i in range(0,len(palabras)):
        repeticion.append(contenido.count(palabras[i]))
    
    print("Hay " + str(len(palabras)) + " palabras diferentes en el archivo")
    return palabras, repeticion

# poner aqui la cosa que grafica ------------
# -------------------------------------------
# -------------------------------------------
    
def main():   
    palabras, repeticion = conteo(obtenerdatos())
    
main()


    


