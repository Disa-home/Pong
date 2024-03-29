'''
Created on Jan 21, 2023

Updated on Nov 04, 2023

@authors: salnr, eddiesalvador
'''

import turtle

wn = turtle.Screen()
wn.title("Pong by Salnr")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
winner = 5

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Winner
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("blue")
pen1.penup()
pen1.hideturtle()

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

    
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        if score_a >= winner:
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
            pen1.write("Player A WON!!!", align="center", font=("Courier", 24, "normal")) 
            ball.reset()
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

         
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        if score_b >= winner:
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
            pen1.write("Player B WON!!!", align="center", font=("Courier", 24, "normal")) 
            ball.reset()
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        
    # Paddle and ball collisions 
    if (ball.xcor() > 330 and ball.xcor() < 335) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(330)
        ball.dx *= -1
        
    if (ball.xcor() < -330 and ball.xcor() > -335) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-330)
        ball.dx *= -1        
        
        
        # Blank comment