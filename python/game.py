import pygame
from player import Perso
from sol import Sol
from enemie import Enemie
from gold import Gold
from score import Score
pygame.init()
ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Le jeu !")
clock = pygame.time.Clock()
counter, text = 40, '40'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('freesansbold.ttf', 32)
p = Perso(ecran)
s = Score(ecran)
solList = []
golds=[]
enemies=[]

solList.append(Sol(ecran,0,900,1000,50))
solList.append(Sol(ecran,0,850,50,60))
solList.append(Sol(ecran,300,850,50,60))
solList.append(Sol(ecran,600,850,50,60))
solList.append(Sol(ecran,950,715,50,185))
solList.append(Sol(ecran,750,790,50,15))
solList.append(Sol(ecran,800,650,50,15))
solList.append(Sol(ecran,500,575,200,15))
solList.append(Sol(ecran,425,500,30,10))
solList.append(Sol(ecran,325,450,20,10))
solList.append(Sol(ecran,415,400,20,10))
solList.append(Sol(ecran,400,250,200,10))
solList.append(Sol(ecran,125,360,200,10))
solList.append(Sol(ecran,305,330,20,30))
solList.append(Sol(ecran,125,300,10,70))
solList.append(Sol(ecran,700,175,50,10))
solList.append(Sol(ecran,950,400,50,10))
solList.append(Sol(ecran,550,100,50,10))
solList.append(Sol(ecran,0,100,500,10))
solList.append(Sol(ecran,0,60,10,40))
solList.append(Sol(ecran,250,60,10,40))
solList.append(Sol(ecran,150,625,20,10))

golds.append(Gold(ecran,200,880))
golds.append(Gold(ecran,800,880))
golds.append(Gold(ecran,210,340))
golds.append(Gold(ecran,975,380))
golds.append(Gold(ecran,70,80))
golds.append(Gold(ecran,160,605))

enemies.append(Enemie(ecran,200,725,100,"right"))
enemies.append(Enemie(ecran,900,650,200,"left"))
enemies.append(Enemie(ecran,250,200,100,"left"))
enemies.append(Enemie(ecran,250,260,100,"right"))
enemies.append(Enemie(ecran,50,-50,250,"right"))

loop = True
getTicksLastFrame = 0
while loop:
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    p.Update(deltaTime)
    for sol in solList:
        sol.Collision(p)
        for en in enemies:
            sol.Collision(en)
    for en in enemies:
        en.Collision(p)
        en.Update(deltaTime)
    for gold in golds:
        gold.Collision(p,s)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if p.canjump:
                    p.canjump = False
                    p.sautForce = p.maxSautForce
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else pygame.quit()
        if event.type == pygame.QUIT:
            loop = False
    else:
        ecran.fill((0,0,0))
        ecran.blit(font.render(text, True, (255, 255, 255)), (950, 10))

    for sol in solList:
        sol.Draw()
    for gold in golds:
        gold.Draw()
    for en in enemies:
        en.Draw()
    p.Draw()
    s.Show_score(en)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()