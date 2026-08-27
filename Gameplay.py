import pygame,os,random

def main(font,width,height,window,clock):
    g = 0.8

    vx = 0
    vy = 0

    speed = 1

    jumped = False

    end = False

    bgnd = pygame.image.load(os.path.join(os.path.dirname(__file__),"bgnd.png")).convert_alpha()
    bgnd = pygame.transform.scale(bgnd,(width,height))

    textbox = pygame.Rect(0,50,350,75)

    player = pygame.Rect(450,100,50,50)

    collision = [pygame.Rect(0,height-50,width,50), # piso
                 pygame.Rect(0,height-200,100,200),  # mini pared
                 pygame.Rect(width/6,height-400,width/4,50), # plataforma 1
                 pygame.Rect((width - width/4) - width/6,height-400,width/4,50), # plataforma 2
                 pygame.Rect(-10,0,10,height), # pared 1
                 pygame.Rect(width,0,10,height) # pared 2
                 ]

    points = []

    point_count = 0

    class point:
        def __init__(self,type):
            self.last = None
            self.cool = 10000
            self.type = type
            self.pos = (random.randint(50,width-50),0)
            if type == 1:
                size = 15
                self.points = 10
                self.color = (75,235,235)
            elif type == 2:
                size = 30
                self.points = 20
                self.color = (226,80,248)
            elif type == 3:
                        size = 40
                        self.points = 30
                        self.color = (255,100,100)
            else:
                size = 15
                self.points = 5
                self.color = (75,235,235)
            self.surf = pygame.Rect(self.pos[0],self.pos[1],size,size)
            self.delete = False

        def update(self):
            self.surf.y += 4
            for surf in collision:
                if surf.colliderect(self.surf):
                    if self.last == None:
                        self.last = pygame.time.get_ticks()
                    self.surf.bottom = surf.top
                    now = pygame.time.get_ticks()
                    if now - self.last >= self.cool:
                        self.delete = True
            if self.surf.colliderect(player):
                self.delete = True
            pygame.draw.rect(window, self.color, self.surf)

    def create_points():
        obj = point(random.randint(1,3))
        return obj

    def draw():
        window.blit(bgnd,(0,0))
        for obj in collision:
            pygame.draw.rect(window, (70,130,53), obj)
        for obj in points:
            obj.update()
        pygame.draw.rect(window, (0,0,255), player)
        pygame.draw.rect(window, (0,0,0), textbox)
        text = font.render(f"OBJETIVO: conseguir 600 puntos",True,(0,255,0))
        window.blit(text, (10,65))
        if end:
            text = font.render(f"     Objetivo completado",True,(0,255,0))
        else:
            text = font.render(f"Puntaje: {point_count}",True,(0,255,0))
        window.blit(text, (10,95))

    def update_points(points):
        score = point_count
        for obj in points:
            if obj.delete and obj.surf.colliderect(player):
                score += obj.points
                points.remove(obj)
            elif obj.delete:
                points.remove(obj)
        return points,score

    trans_surf = pygame.surface.Surface((width,height))
    
    trans_effect = 255

    def intro(trans_effect):
        while trans_effect >= 0:
            draw()
            trans_surf.set_alpha(round(trans_effect))
            window.blit(trans_surf,(0,0))
            trans_effect -= 10
            pygame.display.update()
            clock.tick(60)
        return trans_effect

    def outro(trans_effect):
        while trans_effect <= 255:
            draw()
            trans_surf.set_alpha(round(trans_effect))
            window.blit(trans_surf,(0,0))
            trans_effect += 5
            pygame.display.update()
            clock.tick(60)
        return trans_effect
    trans_effect = intro(trans_effect)
    
    last = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    points.append(create_points())

        if not end:
            if pygame.time.get_ticks() - last > 2000:
                points.append(create_points())
                last = pygame.time.get_ticks()

        keys = pygame.key.get_pressed()

        if not end:
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

        points, point_count = update_points(points)

        if point_count >= 600:
            point_count = 0
            end = True
            points.clear()
            last = pygame.time.get_ticks()

        if end:
            if pygame.time.get_ticks() - last >= 3000:
                break

        pygame.display.update()
        clock.tick(60)
    trans_effect = outro(trans_effect)