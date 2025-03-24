import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Shooting Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Draw borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-250, -250)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -220)
player.setheading(90)

# Create the bullet turtle
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Create targets
num_targets = 5
targets = []

for _ in range(num_targets):
    target = turtle.Turtle()
    target.color("green")
    target.shape("circle")
    target.penup()
    target.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(0, 250)
    target.setposition(x, y)
    targets.append(target)

# Move player left and right
player_speed = 15


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -240:
        x = -240
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 240:
        x = 240
    player.setx(x)


# Fire bullet
bullet_speed = 20


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    return distance < 20


# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    wn.update()

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check for a collision between the bullet and the target
    for target in targets:
        if is_collision(bullet, target):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            target.setposition(random.randint(-200, 200), random.randint(100, 250))

    # Check for collision between the player and the target
    for target in targets:
        if is_collision(player, target):
            player.hideturtle()
            target.hideturtle()
            print("Game Over")
            break

turtle.done()