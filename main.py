from pygame import *
from button import Button
from sprite import Sprite

window = display.set_mode((600,500 ))
display.set_caption("Click to")

game = True
clock = time.Clock()


btn1 = Button("exit.png", 250,250,100,100)
btn2 = Button("start.png", 250,100,100,100)
font.init()
font1 = font.SysFont(None,20) 
count = 0 
bg = image.load("bg.png")
health = 100
ing = font1.render(str(100),True,(255,255,255))
pausa = True 



monster1 = Sprite("monstr_1.png", 250,250,200,100)
monster2 = Sprite("monstr_2.png", 250,250,200,100)
monster3 = Sprite("monstr_3.png", 250,250,200,100)
monster4 = Sprite("monstr_5.png", 250,250,200,100)
monster5 = Sprite("pituh.png", 250,250,200,100)
monster6 = Sprite("monstr_0.png", 250,250,200,100)
monster7 = Sprite("zoidberg.png", 250,250,200,100)

scr = monster1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if pausa:
        window.blit(bg,(0,0))
        if btn1.draw(window):
            game = False 
        if btn2.draw(window):
            pausa = False

    else:
        window.blit(bg,(0,0))
        window.blit(ing,(0,0))
        if scr.draw(window):
            if monster1.health > 0:
                monster1.health -= 10
                print(monster1.health)
                ing = font1.render(str(monster1.health),True,(255,255,255))

            elif monster2.health > 0:
                scr = monster2
                monster2.health -= 10
                print(monster2.health)
                ing = font1.render(str(monster2.health),True,(255,255,255))
            
            elif monster3.health > 0:
                scr = monster3
                monster3.health -= 10
                print(monster3.health)
                ing = font1.render(str(monster3.health),True,(255,255,255))

            elif monster4.health > 0:
                scr = monster4
                monster4.health -= 10
                print(monster4.health)
                ing = font1.render(str(monster4.health),True,(255,255,255))

            elif monster5.health > 0:
                scr = monster5
                monster5.health -= 10
                print(monster5.health)
                ing = font1.render(str(monster5.health),True,(255,255,255))

            elif monster6.health > 0:
                scr = monster6
                monster6.health -= 10
                print(monster6.health)
                ing = font1.render(str(monster6.health),True,(255,255,255))

            elif monster7.health > 0:
                scr = monster7
                monster7.health -= 10
                print(monster7.health)
                ing = font1.render(str(monster7.health),True,(255,255,255))
        



    

    display.update()
    clock.tick(60)