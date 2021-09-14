
"""
Equipo 1
    Ana Patricia Islas Mainou A01751676
    Luis Humberto Romero Pérez A01752789
    Rodrigo Mejía Jiménez A01752789
"""

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def movercomida(x, y):

    global food
    x=(x//10)*10
    y=(y//10)*10
    food=vector(x,y)
    


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head):
        
        if aim.x==0 and aim.y==10:
            change(-10,0)
            
            
        elif aim.x==0 and aim.y==-10:
            change(10,0)
        elif aim.x==10 and aim.y==0:
            change(0,10)
        elif aim.x==-10 and aim.y==0:
            change(0,-10)
            
            
        
        
        update()
        
       
    
    elif head in snake:
        
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100) #cambio de velocidad


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
onscreenclick(movercomida)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()