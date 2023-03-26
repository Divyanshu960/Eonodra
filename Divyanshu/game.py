import pygame as pg
from sys import exit
  
pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption('Runner')
clock = pg.time.Clock()
test_font = pg.font.Font('font/Pixeltype.ttf',50)
 
sky_surface = pg.image.load('graphics/sky.png').convert()
ground_surface = pg.image.load('graphics/ground.png').convert()
score_surf = test_font.render(' My game ',False,'Black')
score_rect = score_surf.get_rect(center=(400,50))

snail_surf = pg.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(80,300))

player_surf = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom =(80,300))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.update()
            exit()
        if event.type == pg.MOUSEMOTION:
            if (player_rect.collidepoint(event.pos)):
                print("Collision")
        if event.type == pg.KEYUP:
            print('keydown')
        if event.type == pg.KEYDOWN:
            print('keyup')
        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    pg.draw.rect(screen,'Pink',score_rect)
    pg.draw.rect(screen,'Pink',score_rect,10)
    pg.draw.ellipse(score_surf,'Gold',pg.Rect(50,200,100,100))
    screen.blit(score_surf,score_rect)


    if (snail_rect.right<=0):snail_rect.left=800
    snail_rect.left-=4

    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        print('jump')
    # pg.draw.line(screen,'Black',(0,0),(800,400),width=4)
    # if player_rect.colliderect(snail_rect):
    # mousepos=pg.mouse.get_pos()
    # if player_rect.collidepoint(mousepos):
    #    print(pg.mouse.get_pressed())    

    pg.display.update()
    clock.tick(30)
