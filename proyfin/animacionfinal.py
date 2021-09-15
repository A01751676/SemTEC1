
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
granjero = pygame.transform.scale(granjero, (75, 100))
zorro = pygame.image.load("zorro.png")
zorro = pygame.transform.scale(zorro, (75, 75))
maiz = pygame.image.load("maiz.png")
maiz = pygame.transform.scale(maiz, (75, 75))
barco = pygame.image.load("bote.png")
barco = pygame.transform.scale(barco, (150, 150))
ganso = pygame.image.load("ganso.png")
ganso = pygame.transform.scale(ganso, (75, 75))

pantalla.blit(granjero,(5,300))
pantalla.blit(zorro,(5,230))
pantalla.blit(maiz,(5,50))
pantalla.blit(ganso,(5,150))
pantalla.blit(barco,(100,350))
#Bucle para solo cerrar la ventana al presionar el boton de cerrar
while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  pygame.display.update()
  