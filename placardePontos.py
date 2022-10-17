from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.pontos_e = 0
        self.pontos_d = 0
        self.pontuacao()

    def pontuacao(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.pontos_e, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.pontos_d, align="center", font=("Courier", 80, "normal"))

    def ponto_e(self):
        self.pontos_e += 1
        self.pontuacao()

    def ponto_d(self):
        self.pontos_d += 1
        self.pontuacao()
