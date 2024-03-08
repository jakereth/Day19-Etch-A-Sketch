from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def moveForward():
    turt.forward(1)

def moveBackward():
    turt.backward(1)

def turnLeft():
    turt.left(1)

def turnRight():
    turt.right(1)

def clear_Screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.down()

screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="c", fun=clear_Screen)
screen.exitonclick()