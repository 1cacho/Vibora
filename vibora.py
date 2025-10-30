from random import randrange, choice
from turtle import *
from freegames import vector

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

def move_food():
    """Move food randomly one step at a time without going outside window."""
    # Lista de posibles direcciones (arriba, abajo, izquierda, derecha)
    directions = [(0, 10), (0, -10), (10, 0), (-10, 0)]
    
    # Filtrar direcciones que mantengan la comida dentro de los límites
    valid_directions = []
    
    for dx, dy in directions:
        new_x = food.x + dx
        new_y = food.y + dy
        # Verificar que la nueva posición esté dentro de los límites
        if -200 < new_x < 190 and -200 < new_y < 190:
            valid_directions.append((dx, dy))
    
    # Si hay direcciones válidas, elegir una al azar
    if valid_directions:
        dx, dy = choice(valid_directions)
        food.x += dx
        food.y += dy

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
    
    # Mover la comida aleatoriamente en cada turno
    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
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
