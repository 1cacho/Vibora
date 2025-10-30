from random import randrange, choice
from turtle import *
from freegames import vector

# Lista de colores disponibles (excepto rojo)
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar colores aleatorios diferentes a la serpiente y comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def square(x, y, size, color_name):
    """Draw square at position."""
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()
    for count in range(4):
        forward(size)
        left(90)
    end_fill()

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # Mover la comida a una nueva posición aleatoria
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Color aleatorio para la serpiente

    square(food.x, food.y, 9, food_color)  # Color aleatorio diferente para la comida
    update()
    ontimer(move, 100)

# Inicializar la comida
food = vector(0, 0)
food.x = randrange(-15, 15) * 10
food.y = randrange(-15, 15) * 10

# Inicializar la serpiente
snake = [vector(10, 0)]
aim = vector(0, -10)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
