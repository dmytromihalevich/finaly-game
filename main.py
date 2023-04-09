from pygame import *
from button import Button

window = display.set_mode((600,500 ))

game = True
clock = time.Clock()

btn1 = Button("exit.png", 100,100,100,50)

while game:
    for i in event.get():
        if e.type == QUIT:
            game = False


    if btn1.draw(window):
        print("PRESSED")
    display.update()
    clock.tick(60)