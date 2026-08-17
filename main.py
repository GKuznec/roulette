import pygame
import random
pygame.init()
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



screen_w = 1000
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
position = [0,0]
imp = pygame.image.load("images/images.png")
y_start = 650
x_start = 425
width_rect = 150
height_rect = 50
width_pm = 70
height_pm = 40


x_green = 800
y_green = 300
x_red=800
y_red=375
x_black=800
y_black=450
x_minus = 800
y_minus = 520
x_plus = 880
y_plus = 520




font = pygame.font.Font(None,25 )
text = font.render('START', True, (255,255,255))
button_rect =  pygame.Rect(x_start,y_start,width_rect,height_rect)
textrect = text.get_rect(center=button_rect.center)

font_g = pygame.font.Font(None,25)
text_green = font_g.render('BET GREEN',True,(255,255,255))
button_green_rect =  pygame.Rect(x_green,y_green,width_rect,height_rect)
text_green_rect = text_green.get_rect(center=button_green_rect.center)

font_r = pygame.font.Font(None,25)
text_red = font_r.render('BET RED',True,(255,255,255))
button_red_rect =  pygame.Rect(x_red,y_red,width_rect,height_rect)
text_red_rect = text_red.get_rect(center=button_red_rect.center)

font_b = pygame.font.Font(None,25)
text_black = font_b.render('BET BLACK',True,(255,255,255))
button_black_rect =  pygame.Rect(x_black,y_black,width_rect,height_rect)
text_black_rect = text_black.get_rect(center=button_black_rect.center)

score = pygame.font.Font(None,25 )
score_text = font.render('ewfw', True, (0,0,0))
scorerect = score_text.get_rect(center=(500,100))

res = pygame.font.Font(None,25 )
res_text = res.render('', True, (0, 255, 0))
res_text_rect = res_text.get_rect(center=(500, 50))

balance = 1000
bet_amount = 50
step = 50

text_minus = font.render('-',True,(0,0,0))
button_minus_rect =  pygame.Rect(x_minus,y_minus,width_pm,height_pm)
text_minus_rect = text_minus.get_rect(center=button_minus_rect.center)


text_plus = font.render('+',True,(0,0,0))
button_plus_rect =  pygame.Rect(x_plus,y_plus,width_pm,height_pm)
text_plus_rect = text_plus.get_rect(center=button_plus_rect.center)



vel = 0

count = 0
running = True
w = False
game_over = False
imp1 = rot_center(imp,0)
bet = {"Green": False,"Red": False, "Black":False}
color_tuple = {"Green": (0,255,0),"Red": (255,0,0), "Black":(0,0,0)}
betx = {"Green": 14,"Red": 2, "Black": 2}

while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not w:
                w = True
                game_over = False
                vel = random.randint(15,25)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x_start <= mouse[0] <= x_start + width_rect and y_start <= mouse[1]<= y_start+height_rect and not w:
                if balance >= bet_amount:
                    balance -= bet_amount
                    w = True
                    game_over = False
                    vel = random.randint(15,25)
            if not w:
                if x_green <= mouse[0] <= x_green + width_rect and y_green <= mouse[1] <= y_green+ height_rect :
                     bet = {"Green": True,"Red": False,"Black": False}
                if x_red<= mouse[0] <= x_red + width_rect and y_red <= mouse[1] <= y_red+ height_rect :
                    bet = {"Green": False, "Red": True, "Black": False}
                if x_black <= mouse[0] <= x_black + width_rect and y_black<= mouse[1] <= y_black+ height_rect:
                    bet = {"Green": False, "Red": False, "Black": True}

                if x_plus <= mouse[0] <= x_plus + width_pm and y_plus <= mouse[1] <= y_plus + height_pm:
                    if bet_amount + step <= balance:
                        bet_amount += step
                if x_minus <= mouse[0] <= x_minus + width_pm and y_minus <= mouse[1] <= y_minus + height_pm:
                    if bet_amount - step >= step:
                        bet_amount -= step

    screen.fill((255,255,255))


    if x_start <= mouse[0] <= x_start + width_rect and y_start <= mouse[1]<= y_start+height_rect:
        pygame.draw.rect(screen, (0, 255, 0), (x_start, y_start, width_rect, height_rect), 0, 3)
        pygame.draw.rect(screen, (255, 255, 0), (x_start, y_start, width_rect, height_rect), 3, 3)
    else:
        pygame.draw.rect(screen, (0, 255, 0), (x_start, y_start, width_rect, height_rect), 0, 3)

    screen.blit(text, textrect)

    if x_green <= mouse[0] <= x_green + width_rect and y_green <= mouse[1]<= y_green+height_rect:
        pygame.draw.rect(screen, (0, 120, 0), (x_green, y_green, width_rect, height_rect), 0, 3)
        pygame.draw.rect(screen, (255, 255, 0), (x_green, y_green, width_rect, height_rect), 3, 3)
    else:
        pygame.draw.rect(screen, (0, 120, 0), (x_green, y_green, width_rect, height_rect), 0, 3)

    screen.blit(text_green, text_green_rect)

    if x_red <= mouse[0] <= x_red + width_rect and y_red <= mouse[1]<= y_red+height_rect:
        pygame.draw.rect(screen, (255, 0, 0), (x_red, y_red, width_rect, height_rect), 0, 3)
        pygame.draw.rect(screen, (255, 255, 0), (x_red, y_red, width_rect, height_rect), 3, 3)
    else:
        pygame.draw.rect(screen, (255, 0, 0), (x_red, y_red, width_rect, height_rect), 0, 3)

    screen.blit(text_red, text_red_rect)

    if x_black <= mouse[0] <= x_black + width_rect and y_black <= mouse[1]<= y_black+height_rect:
        pygame.draw.rect(screen, (0, 0, 0), (x_black, y_black, width_rect, height_rect), 0, 3)
        pygame.draw.rect(screen, (255, 255, 0), (x_black, y_black, width_rect, height_rect), 3, 3)
    else:
        pygame.draw.rect(screen, (0, 0, 0), (x_black, y_black, width_rect, height_rect), 0, 3)

    screen.blit(text_black, text_black_rect)


    screen.blit(imp1, imp1.get_rect(center=screen.get_rect().center))
    pygame.draw.polygon(screen, (255, 0, 0),
                        [[480, 150], [520, 150],
                         [500, 185]])

    color = screen.get_at((500, 190))

    if w:
        count += vel
        vel -= 0.1
        imp1 = rot_center(imp, count)

        if vel <=0:
            vel = 0
            w = False
            game_over = True
            spin_result = None
            if color[1] >= 100:
                spin_result = "Green"
            elif color[0] >= 100:
                spin_result ="Red"
            else:
                spin_result = "Black"

            score_text = font.render(spin_result,True, color_tuple[spin_result])

            if bet[spin_result]:
                payout = bet_amount * betx[spin_result]
                balance += payout
                res_text = res.render(f'You won! +{payout}',True,color_tuple[spin_result])
            else:

                res_text = res.render(f'You lost! -{bet_amount}',True,(0,0,255))

            bet = {"Green": False,"Red":False, "Black":False}

    pygame.draw.rect(screen,(70,70,70),button_minus_rect,0,3)
    pygame.draw.rect(screen,(70,70,70),button_plus_rect,0,3)
    screen.blit(text_minus, text_minus_rect)
    screen.blit(text_plus,text_plus_rect)
    font_bet = pygame.font.Font(None, 35)
    bet_text = font.render(f"Bet:        {bet_amount}",True,(0,0,0))
    balance_text = font_bet.render(f"Balance: {balance}",True,(0,0,0))
    screen.blit(bet_text,(800,580))
    screen.blit(balance_text,(800,100))

    if game_over:
        res_text_rect = res_text.get_rect(center=(500, 50))
        screen.blit(res_text,res_text_rect)
        scorerect = score_text.get_rect(center=(500, 100))
        screen.blit(score_text, scorerect)

    pygame.display.flip()
    clock.tick(60)

pygame.display.quit()

pygame.quit()

