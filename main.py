from pygame import *
from button import Button
from sprite import Sprite

window = display.set_mode((600,500 ))
display.set_caption("Clicker")

game = True
clock = time.Clock()


btn1 = Button("ex.png", 250,250,100,100)
btn2 = Button("st.png", 250,100,100,100)
btn3 = Button("+10.png", 50,250,100,100)
btn4 = Button("+1.png", 50,100,100,100)
btn5 = Button("super.png", 50,375,100,100)
font.init()
font1 = font.SysFont(None,100) 
count = 0 
bg = image.load("bg.png")
bg2 = image.load("bg2.png")
coins = 0
health = 10000
power = 1
ing = font1.render(str(101),True,(255,0,0))
text_coin = font1.render("coins " + str(0),True,(255,0,0))
pausa = True 



monster1 = Sprite("monstr_1.png", 250,250,200,100)
monster2 = Sprite("monstr_2.png", 250,250,200,100)
monster3 = Sprite("monstr_3.png", 250,250,200,100)
monster4 = Sprite("monstr_5.png", 250,250,200,100)
monster5 = Sprite("pituh.png", 250,250,200,100)
monster6 = Sprite("monstr_0.png", 250,250,200,100)
monster7 = Sprite("zoidberg.png", 250,250,200,100)

scr = monster1
savePower = power
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pausa = not pausa

    if pausa:
        window.blit(bg2,(0,0))
        if btn1.draw(window):
            game = False 
        if btn2.draw(window):
            pausa = False

    else:
        window.blit(bg,(0,0))
        if btn5.draw(window):
            if coins >= 15:
                coins -= 15
                savePower = power
                power = 1000
        if btn4.draw(window):
            if coins >= 1:
                coins -= 1
                power += 1

        if btn3.draw(window):
            if coins >= 10:
                coins -= 10
                power += 10
        text_coin = font1.render("coins " + str(coins),True,(255,0,0))
        print(coins)
        window.blit(ing,(0,0))
        window.blit(text_coin,(200,0))
        if scr.draw(window):
            if monster1.health > 0:
                monster7.health = 100000
                monster1.health -= power
                power = savePower
                coins = round(coins + 0.25, 2) 
                ing = font1.render(str(monster1.health),True,(255,255,255))

            elif monster2.health > 0:
                scr = monster2
                monster2.health -= power
                power = savePower
                coins = round(coins + 0.35, 2) 
                ing = font1.render(str(monster2.health),True,(255,255,255))
            
            elif monster3.health > 0:
                scr = monster3
                monster3.health -= power
                power = savePower
                coins = round(coins + 0.4, 2) 
                ing = font1.render(str(monster3.health),True,(255,255,255))

            elif monster4.health > 0:
                scr = monster4
                monster4.health -= power
                power = savePower
                coins = round(coins + 0.5, 2) 
                ing = font1.render(str(monster4.health),True,(255,255,255))

            elif monster5.health > 0:
                scr = monster5
                monster5.health -= power
                power = savePower
                coins = round(coins + 0.55, 2) 
                ing = font1.render(str(monster5.health),True,(255,255,255))

            elif monster6.health > 0:
                scr = monster6
                monster6.health -= power
                power = savePower
                coins = round(coins + 0.6, 2) 
                ing = font1.render(str(monster6.health),True,(255,255,255))

            elif monster7.health > 0:
                scr = monster7
                monster7.health -= power
                power = savePower
                coins = round(coins + 0.7, 2) 
                ing = font1.render(str(monster7.health),True,(255,255,255))

            else:
                scr = monster1
                monster1.health = 100000
                monster2.health = 100000
                monster3.health = 100000
                monster4.health = 100000
                monster5.health = 100000
                monster6.health = 100000
                monster7.health = 100000

                    
        



    

    display.update()
    clock.tick(60)