import pygame

width = 1000
height = 900

g = 0.1

vx = 0
vy = 0

pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

player = pygame.Rect(450,400,50,80)

gnd = pygame.Rect(0,800,1000,100)

def correct():
    while player.colliderect(gnd):
        player.y -= 1
        if player.colliderect(gnd) != True:
            player.y += 1
            return


def draw():
    window.fill("white")
    pygame.draw.rect(window, (0,0,255), player)
    pygame.draw.rect(window, (0,255,0), gnd)

jumped = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_d]:
        player.x += 10
    if keys[pygame.K_w] and jumped == False:
        jumped = True
        vy -= 5

    player.y += vy

    if player.colliderect(gnd):
        jumped = False
        vy = 0
        correct()
    elif player.colliderect(gnd) != True:
        vy += g
        
    draw()
    pygame.display.update()
    clock.tick(60)