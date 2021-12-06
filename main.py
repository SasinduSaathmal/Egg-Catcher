import pygame
from pygame import image, display, time, key, sprite, font, mixer
from sys import exit
from utils import large_img, small_img, scale_desk, blit_text_center
from random import randint, choice

# Load images

pygame.init()

BG = small_img(image.load("assets/bg.png"), 4)
HEN = small_img(image.load("assets/hen.png"), 20)
DESK = scale_desk(image.load("assets/desk.png"), 4, 1.5)
BASKET = small_img(image.load("assets/basket.png"), 3)
WHITE_EGG = small_img(image.load("assets/white.png"), 3.5)
BROWN_EGG = small_img(image.load("assets/brown.png"), 3.5)
BR_BROWN_EGG = small_img(image.load("assets/bb_egg.png"), 2)
BR_WHITE_EGG = small_img(image.load("assets/bw_egg.png"), 2)
BASKET_FULL = small_img(image.load("assets/basket_full.png"), 15)
ICON = image.load("assets/icon.png")
FONT = font.Font("assets/Dark Seed.otf", 100)
BIT_SMALLER_FONT = font.Font("assets/Dark Seed.otf", 80)
SCORE_FONT = font.Font("assets/Dark Seed.otf", 70)
CATCH_SOUND = mixer.Sound("assets/catch.wav")
BROKEN_SOUND = mixer.Sound("assets/broken.wav")
BG_MUSIC = mixer.Sound("assets/bg_music.wav")
BG_MUSIC.set_volume(0.5)
BG_MUSIC.play(-1)

FPS = 60

display.set_icon(ICON)

WIDTH, HEIGHT = BG.get_width(), BG.get_height()
win = display.set_mode((WIDTH, HEIGHT))

display.set_caption("SAVE THE EGG")


class GameInfo():
    LEVELS = 10

    def __init__(self, level, level_catch_eggs):
        self.level = level
        self.level_catch_eggs = level_catch_eggs
        self.started = False

    def next_level(self):
        self.level += 1
        self.level_catch_eggs += 2
        egg.vel += 0.5
        basket.bk_index = 0
        egg.catched_eggs_count = 0
        basket.vel += 0.5
        self.started = False


    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True


class Basket():

    def __init__(self, basket, full_basket, bk_index, vel):
        self.score = 0

        self.bk = basket
        self.bk_full = full_basket
        self.baskets = [self.bk, self.bk_full]
        self.bk_index = bk_index
        self.basket = self.baskets[self.bk_index]
        self.basket_rect = self.basket.get_rect(topleft=(500, 500))
        self.vel = vel
        

    def draw(self, win):
        self.basket = self.baskets[self.bk_index]
        win.blit(self.basket, self.basket_rect)

    def bask_rect(self):
        return self.basket_rect

    def control(self):
        keys = key.get_pressed()

        if keys[pygame.K_LEFT] and self.basket_rect.x > 0:
            self.basket_rect.x -= self.vel

        elif keys[pygame.K_RIGHT] and self.basket_rect.x < WIDTH - 200:
            self.basket_rect.x += self.vel

        elif keys[pygame.K_UP] and self.basket_rect.y > 200:
            self.basket_rect.y -= self.vel

        elif keys[pygame.K_DOWN] and self.basket_rect.y < HEIGHT - 150:
            self.basket_rect.y += self.vel

    def marks(self):
        egg.__init__(choice(["white", "brown", "white", "brown"]), randint(1, 4), egg.catched_eggs_count, egg.vel)
        # lose_text = FONT.render("YOU LOSE!", 1, (255, 10, 10))
        # lose_text_rect = lose_text.get_rect(topleft=(500, 300))
        # win.blit(lose_text, lose_text_rect)
        # display.update()
        self.bk_index = 1
        egg.catched_eggs_count = egg.catched_eggs_count + 1

    def lose(self):
        blit_text_center(win, FONT, "YOU!!", (255, 10, 10), -50)
        blit_text_center(win, FONT, "LOSE!!", (255, 10, 10), 150)
        display.update()
        time.delay(5000)
        pygame.quit()
        with open("assets/score.txt", "w") as f:
            f.write(str(game_info.level))

        with open("assets/eggs.txt", "w") as e:
            e.write(str(egg.catched_eggs_count))
        exit()


class Egg():

    def __init__(self, colour, pos, catched_eggs, vel):
        self.show_egg = True
        self.x = 105
        self.y = 150
        self.catched_eggs_count = catched_eggs
        self.vel = vel

        if colour == "white":
            self.egg = WHITE_EGG
            self.br_egg = BR_WHITE_EGG

            if pos == 1:
                self.egg_rect = self.egg.get_rect(topleft=(75, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(75, 500))

            elif pos == 2:
                self.egg_rect = self.egg.get_rect(topleft=(425, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(425, 500))

            elif pos == 3:
                self.egg_rect = self.egg.get_rect(topleft=(775, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(775, 500))

            elif pos == 4:
                self.egg_rect = self.egg.get_rect(topleft=(1125, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(1125, 500))

        elif colour == "brown":
            self.egg = BROWN_EGG
            self.br_egg = BR_BROWN_EGG

            if pos == 1:
                self.egg_rect = self.egg.get_rect(topleft=(75, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(75, 500))

            elif pos == 2:
                self.egg_rect = self.egg.get_rect(topleft=(425, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(425, 500))

            elif pos == 3:
                self.egg_rect = self.egg.get_rect(topleft=(775, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(775, 500))

            elif pos == 4:
                self.egg_rect = self.egg.get_rect(topleft=(1125, 150))
                self.br_egg_rect = self.br_egg.get_rect(topleft=(1125, 500))


    def draw(self, win, basket_rect):
        # 105, 150
        # 455, 150
        # 807, 150
        # 1157, 150
        # (self.egg_rect.x) in (range(basket_rect.x), basket_rect.x + 200) and not (self.egg_rect.y + 50) in (range(basket_rect.y), basket_rect.y + 150)
        if self.show_egg == True:
            if not self.egg_rect.colliderect(basket_rect):
                if self.egg_rect.y < 585:
                    win.blit(self.egg, self.egg_rect)
                else:
                    win.blit(self.br_egg, self.br_egg_rect)
                    self.show_egg = False
                    BROKEN_SOUND.play()
                    basket.lose()
            else:
                CATCH_SOUND.set_volume(10)
                CATCH_SOUND.play()
                time.delay(10)
                self.show_egg = False
                basket.marks()

        else:
            pass
            

    def move(self):
        if self.egg_rect.y < 585:
            self.egg_rect.y += self.vel


    def handle_levels(self):
        if self.catched_eggs_count == game_info.level_catch_eggs:
            game_info.next_level()



def draw_game():
    win.blit(BG, (0, 0))
    win.blit(DESK, (0, 445))
    pygame.draw.line(win, "dark green", (0, 160), (WIDTH, 160), 10)
    win.blit(HEN, (0, -50))
    win.blit(HEN, (350, -50))
    win.blit(HEN, (700, -50))
    win.blit(HEN, (1050, -50))
    # win.blit(BASKET, (400, 400)) 
    basket.draw(win)
    # win.blit(WHITE_EGG, (600, 400)) 
    egg.draw(win, basket.bask_rect())
    egg.handle_levels()
    score_text = SCORE_FONT.render(f"CATHCED EGGS: {egg.catched_eggs_count} / {game_info.level_catch_eggs}", 1, (20, 20, 255))
    score_text_rect = score_text.get_rect(topleft=(40, 220))
    win.blit(score_text, score_text_rect)
    display.update()


with open("assets/score.txt", "r") as f:
    level = int(f.read())

with open("assets/eggs.txt", "r") as e:
    egg_count = int(e.read())

def score(level):
    return level * 2

game_info = GameInfo(level, score(level))
vel = 10 + (0.5 * level)
basket = Basket(BASKET, BASKET_FULL, 0, vel)
egg = Egg(choice(["white", "brown", "white", "brown"]), randint(1, 4), egg_count, 1 + (0.25 * level)) # ,

run = True
clock = time.Clock()

# Game Loop
# 

while run:
    clock.tick(FPS)
    keys = key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     m_x, m_y = pygame.mouse.get_pos()
    #     print(f"x: {m_x}, y: {m_y}")

    if keys[pygame.K_q]:
        pygame.quit()
        exit()

    draw_game()
    while not game_info.started:
        if egg.catched_eggs_count > 0:
            basket.bk_index = 1
            blit_text_center(
                win, BIT_SMALLER_FONT, f"Press Any Key To Continue  Level {game_info.level} !", (200, 200, 200))
            blit_text_center(
                win, SCORE_FONT, f"Objective : Need  {game_info.level_catch_eggs - egg.catched_eggs_count}  More  Eggs", (0, 255, 255), +300)
            display.update()
            blit_text_center(
                win, SCORE_FONT, f"To Complete the Level!", (0, 255, 255), +500)
            display.update()
        else:
            blit_text_center(
                win, FONT, f"Press Any Key To Start Level  {game_info.level} !", (200, 200, 200))
            blit_text_center(
                win, FONT, f"Objective : Collect  {game_info.level_catch_eggs}  Eggs !", (0, 255, 255), +300)
            display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN:
            time.delay(500)
            game_info.start_level()

    basket.control()
    if egg.show_egg == True:
        egg.move()
    else:
        pass


exit()
