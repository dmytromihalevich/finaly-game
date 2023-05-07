from pygame import *

class Sprite(sprite.Sprite):
    def __init__(self,img_name,width,height,x,y):
        self.image = transform.scale(image.load(img_name), (width, height))
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))
