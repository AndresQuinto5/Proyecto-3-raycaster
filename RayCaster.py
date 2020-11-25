import pygame, sys
from gl import *


pygame.init()
screen = pygame.display.set_mode((1000,500), pygame.DOUBLEBUF | pygame.HWACCEL) #, pygame.FULLSCREEN)
screen.set_alpha(None)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def pause():

    click = False
    paused = True
    btn_ctr = 0
    backg = pygame.image.load("./img/sprites/coins/fondo.jpg")
    
    while paused:
         
        screen.fill((0,0,0))

        screen.blit(backg, (0,0))

        draw_text('My Raycaster (Paused)', font, (0, 0, 0), screen, 400, 20)
         
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(425, 100, 200, 50)
        button_2 = pygame.Rect(425, 200, 200, 50)

        if 425 + 200 > mx > 425 and 100 + 50> my > 100 or btn_ctr == 0:
            pygame.draw.rect(screen, (255, 251, 0), button_1)
        else:
            pygame.draw.rect(screen, (254, 253, 189), button_1)

        if 425 + 200 > mx > 425 and 200 + 50 > my > 200 or btn_ctr == 1:
            pygame.draw.rect(screen, (255, 251, 0), button_2)
        else:
            pygame.draw.rect(screen, (254, 253, 189), button_2)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        draw_text('Resume', font, (0, 0, 0), screen, 480, 107)
        draw_text('Exit', font, (0, 0, 0), screen, 505, 203)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_s:
                    btn_ctr += 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_d:
                    btn_ctr += 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_a:
                    btn_ctr -= 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_w:
                    btn_ctr -= 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_RETURN:
                    if btn_ctr == 0:
                        game()
                    if btn_ctr == 1:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)

def main_menu():

    click = False
    btn_ctr = 0

    backg = pygame.image.load("./img/sprites/coins/fondo.jpg")

    while True:
        
        screen.fill((0,0,0))

        screen.blit(backg, (0,0))

        draw_text('My Raycaster', font, (0, 0, 0), screen, 450, 20)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(425, 100, 200, 50)
        button_2 = pygame.Rect(425, 200, 200, 50)

        if 425 + 200 > mx > 425 and 100 + 50> my > 100 or btn_ctr == 0:
            pygame.draw.rect(screen, (255, 251, 0), button_1)
        else:
            pygame.draw.rect(screen, (254, 253, 189), button_1)

        if 425 + 200 > mx > 425 and 200 + 50 > my > 200 or btn_ctr == 1:
            pygame.draw.rect(screen, (255, 251, 0), button_2)
        else:
            pygame.draw.rect(screen, (254, 253, 189), button_2)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
        draw_text('Start', font, (0, 0, 0), screen, 500, 107)
        draw_text('Exit', font, (0, 0, 0), screen, 505, 203)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_s:
                    btn_ctr += 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_d:
                    btn_ctr += 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_a:
                    btn_ctr -= 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_w:
                    btn_ctr -= 1
                    btn_ctr = btn_ctr % 2
                if event.key == pygame.K_RETURN:
                    if btn_ctr == 0:
                        game()
                    if btn_ctr == 1:
                        pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)

r = Raycaster(screen)
r.load_map('map.txt')

def movement():
        keys_control()
        mouse_control()

def mouse_control():
    if pygame.mouse.get_focused():
        halfWidth = int(r.width / 2)
        halfHeight = int(r.height / 2)

        difference = pygame.mouse.get_pos()[0] - halfWidth - 250
        pygame.mouse.set_pos([halfWidth + 250, halfHeight])
        r.player['angle'] += difference * 0.08

def keys_control():

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()

        newX = r.player['x']
        newY = r.player['y']

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pause()
            elif ev.key == pygame.K_w:
                newX += cos(r.player['angle'] * pi / 180) * r.stepSize
                newY += sin(r.player['angle'] * pi / 180) * r.stepSize
            elif ev.key == pygame.K_s:
                newX -= cos(r.player['angle'] * pi / 180) * r.stepSize
                newY -= sin(r.player['angle'] * pi / 180) * r.stepSize
            elif ev.key == pygame.K_a:
                newX -= cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                newY -= sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
            elif ev.key == pygame.K_d:
                newX += cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                newY += sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
            elif ev.key == pygame.K_q:
                r.player['angle'] -= 5
            elif ev.key == pygame.K_e:
                r.player['angle'] += 5

            i = int(newX / r.blocksize)
            j = int(newY / r.blocksize)

            if r.map[j][i] == ' ':
                r.player['x'] = newX
                r.player['y'] = newY

def game():
    isRunning = True
    while isRunning:

        movement()

        r.coin_collide()

        screen.fill(pygame.Color("gray")) #Fondo

        #Techo
        screen.fill(pygame.Color("white"), (int(r.width / 2), 0, int(r.width / 2),int(r.height / 2)))
        
        #Piso
        screen.fill(pygame.Color("dimgray"), (int(r.width / 2), int(r.height / 2), int(r.width / 2),int(r.height / 2)))

        r.render()
        
        # FPS
        screen.fill(pygame.Color("black"), (0,0,30,30))
        screen.blit(updateFPS(), (0,0))
        score = "Score: " + str(r.player['score'])
        draw_text(score, font, (255, 255, 255), screen, 700, 0)
        clock.tick(30)  
        
        pygame.display.update()

    pygame.quit()

main_menu()