
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pink Heart ❤️")

pen = turtle.Turtle()
pen.speed(3)
pen.color("#ff1493")
pen.fillcolor("#ff69b4")
pen.pensize(3)

pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()

pen.hideturtle()

turtle.done()
