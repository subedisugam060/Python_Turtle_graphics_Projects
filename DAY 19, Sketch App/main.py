from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fun_for_forward():
    tim.forward(10)
def fun_for_backward():
    tim.setheading(tim.heading() + 180)
    tim.forward(10)

def fun_for_clearing():
    tim.clear()
    tim.penup()   # so that it doesnot draw when it moves towards home
    tim.home()
    tim.pendown()  # for next draw

def fun_for_clockwise():
    tim.setheading(tim.heading() - 5)

def fun_for_counterclockwise():
    tim.setheading(tim.heading() + 5)


screen.listen()
# this makes turtle listen to the user input
screen.onkey(fun = fun_for_counterclockwise, key = "a" )
#  onkey is the screen method that takes a key as an argument when
# when pressed calls the function which is given to it as argument
#  reaserch about higher order functions (function that has another function as arguement)
# note that paranthesis is not used after function name because we are using function as arguemnt
screen.onkey(key = "s", fun = fun_for_backward)
screen.onkey(key = "w", fun = fun_for_forward)
screen.onkey(key = "d", fun = fun_for_clockwise)
screen.onkey(key = "c", fun = fun_for_clearing)





screen.exitonclick()