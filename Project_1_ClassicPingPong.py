from turtle import*
from playsound import playsound

# Screen
Screen = TurtleScreen
title("Classic Ping Pong by Ivan")
bgcolor("purple")
setup(width=800, height=600)
tracer(1)

# Paddle a
paddle_a = Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle b
paddle_b = Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball 
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Ivan: 0  Villain: 0", align="center", font=("Courier", 24, "normal"))

pin = Turtle()
pin.speed(0)
pin.color("yellow")
pin.penup()
pin.hideturtle()
pin.goto(0, 260)
pin.write("SCOREBOARD", align="center", font=("Courier", 24, "normal"))

titlez = Turtle()
titlez.speed(0)
titlez.color("white")
titlez.penup()
titlez.hideturtle()
titlez.goto(0, 50)
titlez.write("Classic Ping Pong by Ivan", align="center", font=("Courier", 14, "normal"))

congratz = Turtle()
congratz.speed(0)
congratz.color("white")
congratz.penup()
congratz.hideturtle()
congratz.goto(0, 0)

# Score
score_a = 0
score_b = 0

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
listen()
onkeypress(paddle_a_up, "w")
onkeypress(paddle_a_down, "s")
onkeypress(paddle_b_up, "Up")
onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        playsound('C:\\Users\\ivana\\Documents\\Win.wav')
        pen.write("Ivan: {}  Villain: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        playsound('C:\\Users\\ivana\\Documents\\Win.wav')
        pen.write("Ivan: {}  Villain: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    
# Paddle and Ball Collusion
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


# Main Game Loop
done()