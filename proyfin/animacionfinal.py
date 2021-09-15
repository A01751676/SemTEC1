
import pygame
from pygame.locals import *
import sys
import os
#Creacion de ventana
pygame.init()
pantalla = pygame.display.set_mode((626,456))
fondo = pygame.image.load("rio.png")
pantalla.blit(fondo,(0,0))
pygame.display.set_caption("Animacion")

#Asignacion de imagenes a variables
granjero = pygame.image.load("granjero.png")
zorro = pygame.image.load("zorro.png")
maiz = pygame.image.load("maiz.png")
barco = pygame.image.load("bote.png")
ganso = pygame.image.load("ganso.png")

# 
def mov(img, vel, pos):
    pantalla.blit(fondo,(0,0))
    pantallas.blit(granjero, (0,pos + vel))
    

pantalla.blit(maiz,(5,10))
#Bucle para solo cerrar la ventana al presionar el boton de cerrar
while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  pygame.display.update()
  