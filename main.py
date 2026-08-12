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
y = 650
x = 425
width_rect = 150
height_rect = 50

font = pygame.font.Font(None,25 )
text = font.render('Start', True, (255,255,255))
button_rect =  pygame.Rect(x,y,width_rect,height_rect)
textrect = text.get_rect(center=button_rect.center)

vel = 0

count = 0
running = True
w = False
imp1 = rot_center(imp,0)
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                w = not w
                vel = random.randint(15,25)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x <= mouse[0] <= x + width_rect and y <= mouse[1]<= y+height_rect:
                w = True
                vel = random.randint(15,25)


    screen.fill((255,255,255))
    pygame.display.set_caption(''+str(imp.get_rect()))#pygame.mouse.get_pos()

    if w:
        imp1 = rot_center(imp, count)
        if vel > 0:
            count += vel
            vel -= 0.1
    if x <= mouse[0] <= x + width_rect and y <= mouse[1]<= y+height_rect:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width_rect, height_rect), 0, 3)
        pygame.draw.rect(screen, (255, 255, 0), (x, y, width_rect, height_rect), 3, 3)
    else:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width_rect, height_rect), 0, 3)

    screen.blit(text, textrect)

    screen.blit(imp1, imp1.get_rect(center=screen.get_rect().center))
    pygame.draw.polygon(screen, (255, 0, 0),
                        [[480, 130], [520, 130],
                         [500, 170]])
    pygame.display.flip()
    clock.tick(60)

pygame.display.quit()

pygame.quit()

