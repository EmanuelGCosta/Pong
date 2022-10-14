import turtle
from bola import Bola
from jogador import Jogador
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

jogador_d = Jogador((350, 0))
jogador_e = Jogador((-350, 0))
bola = Bola()

screen.listen()
screen.onkey(jogador_d.cima, "w")
screen.onkey(jogador_d.baixo, "s")
screen.onkey(jogador_e.cima, "Up")
screen.onkey(jogador_e.baixo, "Down")


jogo_ligado = True
while jogo_ligado:
    screen.update()
    time.sleep(0.016)
    bola.mexer()

    #Detectando colisão com a parede
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.quicar_y()
    #Detectando colisão com o jogador
    if bola.distance(jogador_d) < 100 and bola.xcor() > 320 or bola.distance(jogador_e) < 100 and bola.xcor() > -320:
        bola.quicar_x()


    print(bola.movimento_y, bola.movimento_x)

screen.exitonclick()