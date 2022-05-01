import math
import pygame

class Enemie:
    def __init__ (self,ecran,x,y,speed,direction):
        self.x = x
        self.y = y
        self.vit = speed
        self.dir = direction
        self.ecran = ecran

    def Draw(self):
        pygame.draw.circle(self.ecran,(255,0,0),(self.x,self.y),20)
    def Update(self, deltatime) :
        if self.dir == "right":
            self.x += deltatime* self.vit
        elif self.dir == "left":
            self.x -= deltatime* self.vit
        self.y += deltatime * 200

    def Collision(self,player) :
        if math.sqrt((player.x-self.x)**2+(player.y - self.y)**2) <= 40:
            pygame.quit()