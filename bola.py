from turtle import Turtle


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.velocidade()


    def mexer(self):
        new_x = self.xcor() + self.movimento_x
        new_y = self.ycor() + self.movimento_y
        self.goto(new_x, new_y)

    def quicar_y(self):
        self.movimento_y *= -1

    def quicar_x(self):
        self.movimento_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.quicar_x()

    def velocidade(self):
        self.movimento_x = 3
        self.movimento_y = 3

    def velocidade_mov(self):
        if self.xcor() > 0:
            self.movimento_x -= 1

        if self.xcor() < 0:
            self.movimento_x += 1

        if self.ycor() > 0:
            self.movimento_y -= 1

        if self.ycor() < 0:
            self.movimento_y += 1