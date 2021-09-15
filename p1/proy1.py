# -*- coding: utf-8 -*-
"""
Equipo 1
    Ana Patricia Islas Mainou A01751676
    Luis Humberto Romero Pérez A01752789
    Rodrigo Mejía Jiménez A01752113
"""
import matplotlib.pyplot as plt
import numpy as np

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

#Funcion para crear las graficas
def histograma(palabras,repeticion):
    #Histograma
    plt.hist(repeticion,color = (0.5,0.1,0.5,0.8))
    plt.title("Histograma de repetición de palabras")
    plt.ylabel("Cantidad de palabras")
    plt.xlabel("Frecuencia")
    #Grafica de barras
    etiquetas = np.arange(len(palabras))
    figura,ax = plt.subplots()
    ax.bar(etiquetas,repeticion,tick_label=palabras,color = (0.5,0.1,0.5,0.8))
    plt.title("Frecuencia de palabras repetidas")
    plt.ylabel("Repeticiones")
    plt.xlabel("Palabras")
    figura.autofmt_xdate(rotation = 90)
    plt.show()
    return 
    
def main():   
    palabras, repeticion = conteo(obtenerdatos())
    histograma(palabras,repeticion)
    
main()


    


