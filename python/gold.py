import pygame
import math

class Gold:
    def __init__ (self,ecran,x,y):
        self.x = x
        self.y = y
        self.ecran = ecran

    def Draw(self):
        pygame.draw.circle(self.ecran,(255,215,0),(self.x,self.y),20)

    def Collision(self,player,score) :
        if math.sqrt((player.x-self.x)**2+(player.y - self.y)**2) <= 40:
            self.x = 5000
            self.y = 5000
            score.score_value += 1