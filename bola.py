from turtle import Turtle


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movimento_x = 2.5
        self.movimento_y = 2.5

    def mexer(self):
        new_x = self.xcor() + self.movimento_x
        new_y = self.ycor() + self.movimento_y
        self.goto(new_x, new_y)

    def quicar_y(self):
        self.movimento_y *= -1

    def quicar_x(self):
        self.movimento_x *= -1