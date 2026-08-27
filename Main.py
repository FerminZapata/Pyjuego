import pygame, Gameplay,Menu

pygame.init()

font = pygame.font.SysFont(None, 30)

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

while True:
    action = Menu.main(width,height,window,clock)
    if action == "quit":
        pygame.quit()
        exit()
    elif action == "start":
        Gameplay.main(font,width,height,window,clock)