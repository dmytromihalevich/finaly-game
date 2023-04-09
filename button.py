from pygame import *

class Batton(sprite.Sprite):
    def __init__(self,btn_image_name,x,y,width,height):
        self.image = image.transform(image.load(btn_image_name),(wxidth,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self,window):
        action = False
        pos = mouse.get_pos()

        if self.rect.colidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0 :
            self.clicked = False

        window.blit(self.image(self.rect.x,self.rect.y))

        return action
        return self.clicked

