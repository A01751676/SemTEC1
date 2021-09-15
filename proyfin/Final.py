import HCRfinal

import pygame

def redrawGameWindow(Dir, p1, p2):
    """
    Redibuja la pestaña cada que se mueve una imagen para conservar el fondo 

    Parameters
    ----------
    Dir : string
        representa la dirección del movimiento o las acciones de la imagen.
    p1 : string
        personaje a colocar.
    p2 : string
        personaje a colocar.

    Returns
    -------
    None.

    """
    global x, y, Side_A, Side_B
            
    win.blit(rio,(0,0))
    ypos = 300
    for item in Side_A:
        win.blit(item,(5,ypos))
        ypos = ypos - 60

    ypos = 300
    for item in Side_B:
        win.blit(item,(450,ypos))
        ypos = ypos - 60

    if p1 != 'Unknown':
        if right:
            win.blit(botederecha,(x,y))
            win.blit(granjero,(x,y-50))
            if p2 != granjero:
                win.blit(p2,(x+50,y-50))           
        elif left:
            win.blit(boteizquierda,(x,y))
            win.blit(granjero,(x,y-50))
            if p2 != granjero:
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(botederecha,(x, y))
    pygame.display.update()

def get_characters(d, p1, p2):
    """
    Asigna una imagen a cada uno de los personajes de la lista

    Parameters
    ----------
    d : string
        Dirección del movimiento de las imagenes en ese momento.
    p1 : string
        Un personaje a colocar.
    p2 : string
        Dirección del movimiento de las imagenes en ese momento..

    Returns
    -------
    d : NONE
        No disponible.
    farmer : pygame object
        la imagen del granjero.
    character : pygame object
        Imagen del personaje requerido.

    """
    if p2 == 'Zorro':
        character = zorro
    elif p2 == 'Maiz':
        character = maiz
    elif p2 == 'Ganzo':
        character = ganso
    else:
        character = granjero
    return (d, granjero, character)

def Embark_characters(B, p1, p2):
    """
    Borra los personajes de una lista simulando que suben al bote

    Parameters
    ----------
    B : list
        Lista con los personajes de un lado del río.
    p1 : string
        personaje.
    p2 : string
        personaje.

    Returns
    -------
    None.

    """
    #Si el personaje seleccionado se encuentra en la lista B, se borra de la lista.
    if p1 in B:
        B.remove(p1)     
    if p2 in B:
        B.remove(p2)
 
def Disembark_characters(A, p1, p2):
    """
    Agrega los personajes a la lista A, simulando que bajan del bote

    Parameters
    ----------
    A : list
        lista con los personajes del otro lado del río.
    p1 : string
        personaje.
    p2 : list
        personaje.

    Returns
    -------
    None.

    """
    if p1 not in A:
        A.append(p1)
    if p2 not in A:
        A.append(p2)
    
def HCR_animacion(P):
    """
    Función que ejecuta toda la animación, tanto el movimiento de los personajes,
    como el bote. Esto lo realiza llamando a las demás funciones para poder 
    ejecutarse

    Parameters
    ----------
    P : list
        lista con la solución a animar.

    Returns
    -------
    None.

    """
    global x, y, left, right, vel
    global Side_A, Side_B

    clock = pygame.time.Clock()
    run = True
    move = 0
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_B, p1, p2)
                for step in range(65):
                    x -= vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2)

        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2)
                for step in range(65):
                    x += vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2)
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown')
        

    pygame.quit()

def Busca_solucion():
    """
    Se manda a llamar la funcion HCR que genera una solución al problema, si
    esta solución es la mejor la regresa, sino genera otra solución

    Returns
    -------
    P : list
        Lista con la solución obtenida.

    """
    P = HCRfinal.HCR()
    while len(P) > 22:
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCRfinal.HCR()
    print (P)
    print (len(P))
    print ('\n =====> Solución encontrada:')
    return (P)

 
            
P = Busca_solucion()
print ('Aquí su animación')

pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Como cruzar un rio")

rio = pygame.image.load('rio.png')
rio = pygame.transform.scale(rio, (600, 600))
botederecha = pygame.image.load('botederecha.png')
botederecha = pygame.transform.scale(botederecha, (150, 150))
boteizquierda = pygame.image.load('boteizquierda.png')
boteizquierda = pygame.transform.scale(boteizquierda, (150, 150))
#char = pygame.image.load('BoteRight.png')
zorro = pygame.image.load('zorro.png')
zorro = pygame.transform.scale(zorro, (75, 75))
maiz = pygame.image.load('maiz.png')
maiz = pygame.transform.scale(maiz, (75, 75))
ganso = pygame.image.load('ganso.png')
ganso = pygame.transform.scale(ganso, (75, 75))
granjero = pygame.image.load('granjero.png')
granjero = pygame.transform.scale(granjero, (75, 100))
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

Side_A = [granjero, zorro, ganso, maiz]
Side_B = []

HCR_animacion(P)




