
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

#Bucle para solo cerrar la ventana al presionar el boton de cerrar
while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  pygame.display.update()
