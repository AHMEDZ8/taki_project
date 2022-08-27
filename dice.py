import pygame
from sys import exit
import random
a=0

def show(m,y,a):
    k=20
    if a<m:
        for i in range (m):
            screen.blit(puzzle[m], (300+3*k, 110+k))
            k+=20
    
    if tab[m-1]==tab[y-1]:
        m+=1

        screen.blit(puzzle[m-1], (300+3*k, 110+k))
        screen.blit(puzzle[m], (300+3*k, 110+2*k))
    if tab[m-1]!=tab[y-1]:
        m+=1
        screen.blit(puzzle[m], (300+3*k, 100+k))
    if m ==8:
        b = pygame.image.load('graphics/b.png')
        screen.blit(b,(300,150))

   



pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Dice Roll Stimulator")

background_image = pygame.image.load('graphics/background1.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
roll_message = font.render("press the space bar to roll the dice", True, (255, 235, 193))

dice_images = []
dice_rolling_images = []
puzzle = []
b = pygame.image.load('graphics/b.jpg')



for num in range(1, 7):
    dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
    dice_images.append(dice_image)


for num in range(1, 9):
    dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
    dice_rolling_images.append(dice_rolling_image)
for num in range(1, 10):
    d = pygame.image.load('graphics/hu/capture' + str(num) + '.png')
    puzzle.append(d)

rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]
first = True
tab=[]
i=0
k=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_image, (0, 0))
    screen.blit(roll_message, (50, 300))
    a+=1
    


    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        is_rolling = True
        rolling_aud.play()
        rand_num = random.randint(0, 5)
        dice_num_image = dice_images[rand_num]
        screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
        rolling_images_counter += 1
        first = True
        tab.append(rand_num)
        k+=40
        i+=1
        if len(tab)>=2 and len(tab)%2==0:
            show(i-1,i,a-1)



    else:
        d=0
        if is_rolling:
            screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                is_rolling = False
                rolling_images_counter = 0
                screen.blit(b,(700,150))
            if len(tab)>=2 and len(tab)%2==0:
                show(i-1,i,a-1)
          
            
        else:
            d=0
            screen.blit(dice_num_image, (250, 150))
            if first:
                rolling_stop_aud.play()
                first = False
                screen.blit(b,(700,150))
                
            if len(tab)>=2 and len(tab)%2==0:
                show(i,i,a-1)


    pygame.display.update()
    clock.tick(13)
