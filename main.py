import pygame
import time
import random
pygame.font.init() #font of game

WIDTH, HEIGHT = 1550, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shokhir KHELA")
TG = pygame.transform.scale(pygame.image.load("tg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 18
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicscans", 50) # Create a font object


# brackround image
def draw(player, elapsed_time, stars):
    WIN.blit(TG, (0, 0))

    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 0, 255), player)

    for star in stars:
        pygame.draw.rect(WIN, "white" , star)

    pygame.display.update()


def main():
    run = True
    # making a character that can move
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()       # it ensures constant speed
    start_time = time.time()
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0

    stars = []

    while run:   # this loop sees whether can I exit the game or not
        star_count += clock.tick(60)  # ensures precise TIME
        elapsed_time = time.time() - start_time  # time we have played the game

        if star_count > star_add_increment:
            for _ in range(3):



                # _ a place holder variable
                star_x = random.randint(0, WIDTH - STAR_WIDTH) #
                star = pygame.Rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) # gonna get negative y coordinate (its gonna make the stars enter the screen
                stars.append(star)

            star_add_increment = max(200,star_add_increment-50)
            star_count = 0






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: # (code for the left arrow key) I can assign any key to move it for example a b c
            player.x -= PLAYER_VEL # we substract cuz we want it to move to left

        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:# CODE FOR RIGHT KEY
            player.x += PLAYER_VEL  # WE USE X  FOR GETTING THE X COORDINATE, WE CAN USE Y HEIGHT AND OTHERS

        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0 :
            player.y -= PLAYER_VEL

        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT :
            player.y += PLAYER_VEL
        #star phenomena

        for star in stars[:]:
            star.y += STAR_VEL  #adding means goes down
            if star.y > HEIGHT:
                stars.remove(star)

            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break




        draw(player, elapsed_time, stars)


    pygame.quit()


if __name__ == "__main__":
    main()

