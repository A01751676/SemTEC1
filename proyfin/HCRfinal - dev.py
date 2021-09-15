
import random

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

def seleccion(L):
    """
    Funcion seleccion elige de manera aleatoria un personaje

    Parameters
    ----------
    L : list
        Lista de opciones de personajes que pueden ser elegidos.

    Returns
    -------
    string
        contiene el personaje elegido de manera aleatoria.

    """
    # op es la opcion aleatoria que se elige
    op = random.randint(0,len(L)-1)
    return (L[op])

def Viaje(F, D):
    """
    Mueve una pareja de presonajes de 1 lado del rio a otro

    Parameters
    ----------
    F : list
        lista con los personajes del lado derecho del rio.
    D : list
        lista con los personajes del lado izquierdo del rio.

    Returns
    -------
    str
        personaje del granjero siempre regresa.
    p1 : TYPE
        define que personaje regresa con el granjero.

    """
    # p1 nos da el personaje para cruzar el rio
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    
    # mueve al personaje de un ladodel rio al otro
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1)

def valida_estado(L):
    """
    Valida si la eleccion de personaje es valido y si la combinacion que se 
    queda en la orilla es valida. 

    Parameters
    ----------
    L : lsit
        lista con personajes de cierto lado del rio.

    Returns
    -------
    bool
        nos indica si la eleccion termina en un estado valido o invalido.

    """
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
    return True

def reiniciar_sistema():
    """
    Reinicia el sistema colocando a todos los personajes del lado izquierdo

    Returns
    -------
    None.

    """
    
    # mueve las variables globales a su posicion de inicio
    global Lado_A, Lado_B, Path
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
    Lado_B = []
    Path = []
    

def HCR():
    """
    Encuetra los pasos para llegar a una solucion

    Returns
    -------
    Path : list
        Lista solucion con los pasos a seguir para curzar al otro lado.

    """
    
    F = Lado_A #llado derecho
    D = Lado_B #ldao izquierdo
    
    # sigue realizando viajes de un lado del rio al otro hasta cruzar a
    # todos los personajes
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        
        # revisa que el estado sea valido cada vez que se mueve un personaje
        if valida_estado (F) and valida_estado (D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)
            
            Temp = F
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    return (Path)


def main():
    """
    Programa principal

    Returns
    -------
    None.

    """
    P = HCR() # contiene la solucion
    
    # revisa que sea la solucion optima y repite el proceso hasta encontrarla
    while len(P) > 22:
        reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print (P)
    print (len(P))
            
main()

  
