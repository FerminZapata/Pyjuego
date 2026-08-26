import pygame, Gameplay

pygame.init()

font = pygame.font.SysFont(None, 30)

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Gameplay.main(font,width,height,window,clock)

    window.fill("white")
    
    pygame.display.update()
    clock.tick(60)