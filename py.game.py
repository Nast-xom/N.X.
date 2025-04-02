

import pygame



pygame.init()

biryuzoviy = (121, 255, 251)
pink = (215, 106, 255)
blue = (124, 111, 244)
red = (189,40,40)
grey = (156,156,156)
walls=[
    pygame.Rect(300,290,50,10),(350,300,10,200),(290,300,10,210),(300,310,30,10),(320,340,30,10),(300,370,30,10),(320,400,30,10),(300,430,30,10)
]
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


dis_width = 1000
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height)) # set_mode((x, y))
pygame.display.update()
pygame.display.set_caption('Tower')

game_over = False
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x1_change = - 5
        y1_change = 0
    elif keys[pygame.K_RIGHT]:
        x1_change = 5
        y1_change = 0
    elif keys[pygame.K_UP]:
        x1_change = 0
        y1_change = - 5
    elif keys[pygame.K_DOWN]:
        x1_change = 0
        y1_change = 5
    else:
        x1_change = 0
        y1_change = 0


    x1 += x1_change
    y1 += y1_change
    dis.fill(grey)
    for wall in walls:
        pygame.draw.rect(dis, red, wall)
    pygame.draw.rect(dis, biryuzoviy, [x1,y1, 10, 10])
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
