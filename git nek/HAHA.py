import pygame
import os #this library alow you to get sth from your file
WIDTH,HEIGHT =900,500 
# điểm (0,0) nằm ở góc trái trên cùng
BLUE = (200,255,250)
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT) #rect store : (where it put,it's size)

VEL = 5

FPS = 60 
X,Y = 40,50 #spaceship width and height
BULLET_VEL = 10

DICKHEAD = pygame.image.load(os.path.join('Assets','spaceship_yellow.png')) #join image

DICKHEAD2 = pygame.image.load(os.path.join('Assets','spaceship_red.png'))

DICKHEAD_RESIZE = pygame.transform.scale(DICKHEAD,(X,Y))

DICKHEAD_ROTATE = pygame.transform.rotate(DICKHEAD_RESIZE,90)

DICKHEAD2_RESIZE = pygame.transform.scale(DICKHEAD2,(X,Y))

DICKHEAD2_ROTATE = pygame.transform.rotate(DICKHEAD2_RESIZE,270)

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #width and height of the window

pygame.display.set_caption('dong anh dzai 102') #name the window
#define function

def yellow_movement(keys_pressed,yellow) :
        if keys_pressed[pygame.K_a] and yellow.x-VEL > 0 : #LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH/2-5 - 20 : #RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #DOWN
            yellow.y += VEL

def red_movement(keys_pressed,red) :
        if keys_pressed[pygame.K_LEFT] and red.x-VEL > BORDER.x + 20  : #LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH : #RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : #UP
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT : #DOWN
            red.y += VEL

def draw_window(red,yellow):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN,BLACK,BORDER) #where to draw (on the screen),corlor and the figures that you have gived
    WIN.blit(DICKHEAD_ROTATE,(yellow.x,yellow.y)) # để cập nhập cái red với yellow trong cái main()
    WIN.blit(DICKHEAD2_ROTATE,(red.x,red.y))
    pygame.display.update() #put it at the end,cập nhật các thay đổi về hình ảnh

def main(): #the game operates mainly here
    #create to if the player quit the game
    red = pygame.Rect(700, 300, X , Y)
    yellow = pygame.Rect(100,300, X ,Y)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS) # bảo đảm con game chạy ở 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False #quit the game

        keys_pressed = pygame.key.get_pressed() #track down what key you pressed and store it for 60 times per sec
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed,red)

        draw_window(red,yellow)
    pygame.quit()

if __name__ == '__main__':
    main()
    #quit pygame and close the window
#if we dont call this function press x is no use closing the pygame window
