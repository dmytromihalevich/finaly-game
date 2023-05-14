from pygame import *
from button import Button
from sprite import Sprite

window = display.set_mode((600,500 ))

game = True
clock = time.Clock()

btn1 = Button("exit.png", 100,100,100,50)
btn2 = Button("start.png", 100,200,100,100)
font.init()
font1 = font.SysFont(None,20) 
count = 0 
ing = font1.render(str(count),True,(255,255,255))
pausa = True 

monster1 = Sprite("monstr_0.png", 100,100,32,32)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if pausa:
        window.fill((0,0,0))
        if btn1.draw(window):
            game = False 
        if btn2.draw(window):
            pausa = False

    else:
        window.fill((255,0,0))
        if monster1.draw(window):
            print("ggd")

    

    display.update()
    clock.tick(60)