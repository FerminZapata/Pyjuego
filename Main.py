import pygame, math

width = 1000
height = 800

g = 0.8

vx = 0
vy = 0

speed = 1

jumped = False

pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

player = pygame.Rect(450,100,50,50)

collision = [pygame.Rect(0,700,1000,100), # piso
             pygame.Rect(0,600,100,800),  # mini pared
             pygame.Rect(150,400,200,50), # plataforma 1
             pygame.Rect(700,400,200,50) # plataforma 2
             ]

def draw():
    window.fill("white")
    for obj in collision:
        pygame.draw.rect(window, (0,255,0), obj)
    pygame.draw.rect(window, (0,0,255), player)

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
    if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not jumped:
        jumped = True
        vy -= 19

    # Actualizacion de la posicion del jugador y checkeo de colision en el eje X
    vx = vx * 0.9
    player.x += round(vx)

    for obj in collision:
        if player.colliderect(obj):
            if vx > 0:
                player.right = obj.left
                vx = 0
            elif vx < 0:
                player.left = obj.right
                vx = 0
    
    # Actualizacion de la posicion del jugador y checkeo de colision en el eje Y
    vy += g
    player.y += round(vy)

    for obj in collision:
        if player.colliderect(obj):
            if vy < 0:
                player.top = obj.bottom
                vy = 0
            elif vy > 0:
                jumped = False
                player.bottom = obj.top
                vy = 0

    draw()
    pygame.display.update()
    clock.tick(60)