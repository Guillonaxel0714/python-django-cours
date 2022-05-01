import pygame

class Score:
    def __init__ (self,ecran):
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.ecran = ecran
        self.win = self.font.render("C'EST GAGNÉ !",True, (0,0,0))

    def Show_score(self,enemie):
        self.score_text = self.font.render("Score : " + str(self.score_value), True, (255,255,255))
        self.ecran.blit(self.score_text, (10, 10))
        if self.score_value == 6:
            enemie.speed = 0
            self.ecran.fill((255,255,255))
            self.ecran.blit(self.win, (400, 480))


