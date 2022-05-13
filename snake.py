"""Snake, classic arcade game.

Exercise

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
#from random import randit
from random import choice

colors = ['blue','black','yellow','pink','green']
#colorcito = randint(0, 4)
#colorcito2 = randint(0, 4)
colores = [0,1,2,3,4]
selection = choice(colores)
selection2 = choice(colores)

snake = [[10, 0]]
aim = [0, -10]
food = [20, 0]

def change(x, y):
  aim[0] = x
  aim[1] = y
  
def draw_square(x, y, size, name):
    up()
    goto(x, y)
    down()
    color(name)
    begin_fill()

    for count in range(4):
      forward(size)
      left(90)

    end_fill()
  
def inside(head):
    return -200 < head[0] < 190 and -200 < head[1] < 190
    
def move():
  head = [snake[-1][0] + aim[0], snake[-1][1] + aim[1]]

  if not inside(head) or head in snake:
    draw_square(head[0], head[1], 9, 'red')
    update()
    return

  snake.append(head)
  
  if head == food:
    food[0] = randrange(-15, 15) * 10
    food[1] = randrange(-15, 15) * 10
  else:
    snake.pop(0)
    
  clear()
  
  for body in snake:
    draw_square(body[0], body[1], 9, colors[selection])
    
  draw_square(food[0], food[1], 9, colors[selection2])
  update()
  Screen().ontimer(move, 100)

Screen().setup(420, 420, 370, 0)
hideturtle()
Screen().tracer(0, 0)

Screen().listen()
Screen().onkey(lambda: change(10, 0), 'Right')
Screen().onkey(lambda: change(-10, 0), 'Left')
Screen().onkey(lambda: change(0, 10), 'Up')
Screen().onkey(lambda: change(0, -10), 'Down')

move()

done()
