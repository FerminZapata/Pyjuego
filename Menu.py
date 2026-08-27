import pygame,os

def main(width,height,window,clock):

    font = pygame.font.SysFont(None, 50)

    sfont = pygame.font.SysFont(None, 200)

    class button:
        def __init__(self,pos,text,name):
            self.name = name
            self.y = pos
            self.pressed = False
            self.touched = False
            self.surf = pygame.Rect((width/2)-200,self.y,400,100)
            self.edge = pygame.Rect((width/2)-205,self.y-5,410,110)
            self.text = text

        def upd_obj(self):
            text = font.render(self.text,True,(0,0,0))
            pygame.draw.rect(window, (0,0,0), self.edge)
            if self.pressed:
                pygame.draw.rect(window, (100,255,100), self.surf)
            elif self.touched:
                pygame.draw.rect(window, (25,200,25), self.surf)
            else:
                pygame.draw.rect(window, (50,255,50), self.surf)
            window.blit(text,((self.surf.x + self.surf.width/2) - (text.get_width()/2),(self.surf.y + self.surf.height/2) - (font.get_height()/2)))

    title = sfont.render("Un juego sin sentido",True,(0,0,0))
    start = button(height/4*2,"empezar","start")
    quit = button(height/4*3,"salir","quit")

    bgnd_color = (50,255,75)

    buttons = [start,quit]

    end = False

    action = ""

    trans_surf = pygame.surface.Surface((width,height))
    
    trans_effect = 255

    def intro(trans_effect):
        while trans_effect >= 0:
            window.fill(bgnd_color)
            window.blit(title,(width/2 - title.get_width()/2,height/8))
            
            for but in buttons:
                but.upd_obj()

            trans_surf.set_alpha(round(trans_effect))
            window.blit(trans_surf,(0,0))
            trans_effect -= 10

            pygame.display.update()
            clock.tick(60)
        return trans_effect

    def outro(trans_effect):
            while trans_effect <= 255:
                window.fill(bgnd_color)
                window.blit(title,(width/2 - title.get_width()/2,height/8))
                
                for but in buttons:
                    but.upd_obj()
    
                trans_surf.set_alpha(round(trans_effect))
                window.blit(trans_surf,(0,0))
                trans_effect += 5
    
                pygame.display.update()
                clock.tick(60)
            return trans_effect

    trans_effect = intro(trans_effect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        mouse = pygame.mouse.get_pos()
        minputs = pygame.mouse.get_pressed()
        temp = pygame.Rect(mouse[0],mouse[1],1,1)

        window.fill(bgnd_color)
        window.blit(title,(width/2 - title.get_width()/2,height/8))

        if end:
            break

        for but in buttons:
            if not end:
                if temp.colliderect(but.surf) and minputs[0]:
                    but.pressed = True
                    end = True
                    action = but.name
                elif temp.colliderect(but.surf):
                    but.pressed = False
                    but.touched = True
                else:
                    but.touched = False
                    but.pressed = False
            else:
                but.touched = False
                but.pressed = False
            but.upd_obj()

        pygame.display.update()
        clock.tick(60)
    trans_effect = outro(trans_effect)
    return action