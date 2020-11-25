#AndresQ - 18288
import pygame

screen = pygame.display.set_mode((1000,500), pygame.DOUBLEBUF | pygame.HWACCEL)
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

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

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

def pause():
    
    click = False
    paused = True
    btn_ctr = 0
    backg = pygame.image.load("./img/sprites/coins/fondo.jpg")
    
    while paused:
         
        screen.fill((0,0,0))

        screen.blit(backg, (0,0))

        draw_text('My Raycaster (Paused)', font, (255, 255, 255), screen, 400, 20)
         
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(425, 100, 200, 50)
        button_2 = pygame.Rect(425, 200, 200, 50)

        if 425 + 200 > mx > 425 and 100 + 50> my > 100 or btn_ctr == 0:
            pygame.draw.rect(screen, (200, 0, 0), button_1)
        else:
            pygame.draw.rect(screen, (255, 0, 0), button_1)

        if 425 + 200 > mx > 425 and 200 + 50 > my > 200 or btn_ctr == 1:
            pygame.draw.rect(screen, (200, 0, 0), button_2)
        else:
            pygame.draw.rect(screen, (255, 0, 0), button_2)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        draw_text('Resume', font, (255, 255, 255), screen, 480, 107)
        draw_text('Exit', font, (255, 255, 255), screen, 505, 203)
 
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
        mainClock.tick(60)