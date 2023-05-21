from pygame import *

class Sprite(sprite.Sprite):
    def __init__(self,img_name,width,height,x,y, health = 100):
        self.image2 = transform.scale(image.load(img_name), (width, height))
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.clicked = False

    def draw(self,window):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0 :
            self.clicked = False

        window.blit(self.image2,(self.rect.x,self.rect.y))

        return action
        

