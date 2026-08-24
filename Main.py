import pygame

width = 1000
height = 700

g = 0.8

vx = 0
vy = 0

pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

player = pygame.Rect(450,100,50,80)

gnd = pygame.Rect(0,600,1000,100)

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

speed = 0.8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        vx -= speed
    if keys[pygame.K_d]:
        vx += speed
    if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and jumped == False:
        jumped = True
        vy -= 15

    vx = vx * 0.9

    player.y += vy
    player.x += vx

    if player.colliderect(gnd):
        jumped = False
        vy = 0
        correct()
    elif player.colliderect(gnd) != True:
        vy += g
        
    draw()
    pygame.display.update()
    clock.tick(60)