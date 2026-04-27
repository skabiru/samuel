import turtle
import numpy as np #setting up the libraries i will be using
import time
#background
screen = turtle.Screen()
screen.setup(width = 900, height = 700)
screen.bgcolor("black")
screen.title("Asteroid Destroyer")
screen.tracer(0)
#stats tracking
stats = {"score": 0, "lives": 3}
t = turtle.Turtle()
t.hideturtle()
t.color("white")
t.penup()
t.goto(-350,310)
#func that updates the game constantly
def update_screen():
    t.clear()
    t.write(f"Score: {stats['score']} Lives: {stats['lives']}", align = "center", font = ("Arial", 16, "bold"))
update_screen()
#creating the player
shooter = turtle.Turtle()
shooter.color("red")
shooter.shape("turtle")
shooter.shapesize(2, 2)
shooter.penup()
shooter.setheading(90)
shooter.goto(0,-300)
#movement
def move_left():
    x = shooter.xcor()    
    if x > -410: 
        shooter.setx(x - 25)     
def move_right():
    x = shooter.xcor()    
    if x < 410: 
        shooter.setx(x + 25)    
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_right, "d")
#making the bullets and asteroids
bullets = []
asteroids = []
def fire_bullet():
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("yellow")
    bullet.shapesize(0.5, 2)
    bullet.speed(0)
    bullet.penup()
    bullet.setheading(90)
    bullet.goto(shooter.xcor(), shooter.ycor() + 20)
    bullets.append(bullet)
def create_asteroid():
    ast = turtle.Turtle()
    ast.shape("circle")
    ast.color("pink")
    ast.shapesize(2, 2)
    ast.penup()
    ast.setheading(90)
    x_pos = np.random.randint(-410, 410)
    ast.goto(x_pos, 350)
    asteroids.append(ast)
screen.onkeypress(fire_bullet, "space")
screen.onkeypress(fire_bullet, "Up")

while True:
    screen.update()
    update_screen()
    if np.random.rand() < 0.02:
        create_asteroid()
    for bullet in bullets[:]:
        bullet.forward(20)
        if bullet.ycor() > 350:
            bullet.hideturtle()
            bullets.remove(bullet)
    for asteroid in asteroids[:]:
        asteroid.backward(1)
        if asteroid.distance(shooter) < 35:
            asteroid.hideturtle()
            stats["lives"] -= 1
            if asteroid in asteroids:
                asteroids.remove(asteroid)
                shooter.goto(0,-300)
        elif asteroid.ycor() < -350:
            stats["lives"] -= 1
            asteroid.hideturtle()
            asteroids.remove(asteroid)
    for asteroid in asteroids[:]:
        for bullet in bullets[:]:
            if bullet.distance(asteroid) < 20:
                asteroid.hideturtle()
                bullet.hideturtle()
                if asteroid in asteroids:
                    asteroids.remove(asteroid)
                if bullet in bullets:
                    bullets.remove(bullet)
                stats["score"] += 20
    if stats["lives"] == 0:
        t.goto(0, 0)
        t.write("GAME OVER :(", font=("Arial", 60, "bold"), align = "center")
        screen.update()
        break
    time.sleep(0.023)