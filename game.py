import pygame, os, json, colorsys
from random import randrange
accel = 0.1
sd = {
    "score1": 0,
    "fails": 0
}
pygame.mixer.init()
pygame.font.init()
food = pygame.Rect(randrange(900), randrange(450), 150, 100)
food2 = pygame.Rect(randrange(900), randrange(450), 150, 50)
food3 = pygame.Rect(randrange(900), randrange(450), 150, 50)
food4 = pygame.Rect(randrange(900), randrange(450), 150, 50)
food5 = pygame.Rect(randrange(900), randrange(450), 150, 50)
fps = 60
vel = 0
xvel = 10
clock = pygame.time.Clock()
APPLEHIT = pygame.mixer.Sound(os.path.join("sfx", "applehit.wav"))
BANANAHIT = pygame.mixer.Sound(os.path.join("sfx", "bananahit.wav"))
BERRYHIT = pygame.mixer.Sound(os.path.join("sfx", "berryhit.wav"))
LEMONHIT = pygame.mixer.Sound(os.path.join("sfx", "lemonhit.wav"))
ORANGEHIT = pygame.mixer.Sound(os.path.join("sfx", "orangehit.wav"))
TXT = pygame.font.SysFont('comicsans', 40)
FAILS = pygame.font.SysFont('comicsans', 40)
WIDTH, HEIGHT = 1000, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COMPUTER = pygame.image.load(os.path.join("gfx", "computer.jpg"))
FOOD_IMG = pygame.image.load(os.path.join("gfx", "apple.png"))
FOOD2_IMG = pygame.image.load(os.path.join("gfx", "orange.png"))
FOOD3_IMG = pygame.image.load(os.path.join("gfx", "bry.png"))
FOOD4_IMG = pygame.image.load(os.path.join("gfx", "banana.png"))
FOOD5_IMG = pygame.image.load(os.path.join("gfx", "lemon.png"))
BASKINS = pygame.transform.scale(pygame.image.load(os.path.join("gfx", "baskins.jpg")), (WIDTH, HEIGHT))
compos = pygame.Rect(200, 200, 100, 100)
pygame.display.set_caption("Fruit Attack!")
pygame.display.set_icon(FOOD4_IMG)
try:
    with open("score.txt") as score_file:
        sd = json.load(score_file)
except:
    pass
score = sd["score1"]
RUNNING = True
def drawToWindow():
    WIN.blit(BASKINS, (0, 0))
    WIN.blit(COMPUTER, (compos.x, compos.y))
    WIN.blit(FOOD_IMG, (food.x, food.y))
    if sd["score1"] >= 10:
        WIN.blit(FOOD2_IMG, (food2.x, food2.y))
    if sd["score1"] >= 50:
        WIN.blit(FOOD3_IMG, (food3.x, food3.y))
    if sd["score1"] >= 300:
        WIN.blit(FOOD4_IMG, (food4.x, food4.y))
    if sd["score1"] >= 1000:
        WIN.blit(FOOD5_IMG, (food5.x, food5.y))
    myTXT = TXT.render("Score: " + str(sd["score1"]), None, (0, 0, 0))
    myFAILS = FAILS.render("Fails: " + str(sd["fails"]), None, (0,0,0))
    WIN.blit(myTXT, (WIDTH - myTXT.get_width() - 10, 10))
    WIN.blit(myFAILS, (WIDTH - myFAILS.get_width() - 10, 100))
    pygame.display.update()
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("score.txt", "w") as score1:
                json.dump(sd, score1)
            quit()
        if compos.y >= HEIGHT - 100:
            compos.y = HEIGHT - 100
            sd["fails"] += 1
            with open("score.txt", "w") as score1:
                json.dump(sd, score1)
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                vel = -5
    color = colorsys.hsv_to_rgb(1, 1, 1)
    pygame.BLEND_ADD
    clock.tick(fps)
    vel += accel
    compos.x += xvel
    compos.y += vel
    if compos.x >= WIDTH - 100 or compos.x <= 10:
        xvel *= -1
    if compos.colliderect(food):
        food = pygame.Rect(randrange(WIDTH - 100), randrange(HEIGHT - 100), 150, 100)
        APPLEHIT.play()
        sd["score1"] += 1
    if sd["score1"] >= 10:
        if compos.colliderect(food2):
            food2 = pygame.Rect(randrange(WIDTH - 100), randrange(HEIGHT - 100), 150, 100)
            ORANGEHIT.play()
            sd["score1"] += 2
    if sd["score1"] >= 50:
        if compos.colliderect(food3):
            food3 = pygame.Rect(randrange(WIDTH - 100), randrange(HEIGHT - 100), 150, 100)
            BERRYHIT.play()
            sd["score1"] += 5
    if sd["score1"] >= 300:
        if compos.colliderect(food4):
            food4 = pygame.Rect(randrange(WIDTH - 100), randrange(HEIGHT - 100), 150, 100)
            BANANAHIT.play()
            sd["score1"] += 10
    if sd["score1"] >= 1000:
        if compos.colliderect(food5):
            food5 = pygame.Rect(randrange(WIDTH - 100), randrange(HEIGHT - 100), 150, 100)
            LEMONHIT.play()
            sd["score1"] += 25
    drawToWindow()