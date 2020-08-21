from random import choice as random_choice
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

###########################
# Sounds.
boom = pygame.mixer.Sound('boom.wav')
obema = pygame.mixer.music.load('chelovek.mp3') # 4 seconds

# Constants.
W = 400
H = 400
GREY =  (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
CARS_SURF = []

sc = pygame.display.set_mode((W, H))

# List of car images (variants).
for i in ('car1.png', 'car2.png', 'car3.png'):
    CARS_SURF.append(pygame.image.load(i).convert_alpha())

car_w = CARS_SURF[0].get_width()

# Paths on which cars will drive
ROAD_LINES = []
x = W
for i in range(W // car_w):
    x -= car_w
    ROAD_LINES.append(x)

del x, car_w

###########################


class Car(pygame.sprite.Sprite):
    """Class that represents each NPC car on screen."""
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed = random_choice((2, 2.5, 3))
 
    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()

def test():
    pygame.draw.rect(sc, GREEN, rect, 1)
    for npc_car in cars:
        pygame.draw.rect(sc, GREEN, npc_car.rect, 1)
 
cars = pygame.sprite.Group()

Car(random_choice(ROAD_LINES), random_choice(CARS_SURF), cars)

car = pygame.image.load('car.png')
rect = car.get_rect(center=(W // 2, H - car.get_width()))
rot = car.copy()

font = pygame.font.Font(None, 50)
game_over = font.render("GAME OVER", 0, WHITE,)
text_rect = game_over.get_rect(center=(200, 200))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.USEREVENT:
            Car(random_choice(ROAD_LINES), random_choice(CARS_SURF), cars)

    # Player controls.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rot = car.copy()
        rect.centery -= 3
    if keys[pygame.K_DOWN]:
        rot = pygame.transform.flip(car, 0, 1)
        rect.centery += 3
    if keys[pygame.K_RIGHT]:
        rot = pygame.transform.rotate(car, -90)
        rect.centerx += 3
    if keys[pygame.K_LEFT]:
        rot = pygame.transform.rotate(car, 90)
        rect.centerx -= 3

    # Conditions of defeat.
    for npc_car in cars:
        if rect.colliderect(npc_car):
            
            boom.play()
            pygame.time.delay(500)
            pygame.mixer.music.play(start=2)
            sc.blit(game_over, text_rect)
            pygame.display.update()
            while True:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT: exit()

    if rect.y < -rect.height:
        pygame.mixer.music.play(start=0)
        sc.blit(game_over, text_rect)
        pygame.display.update()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
        
            
 
    sc.fill(GREY)
    rect = rot.get_rect(center=rect.center)
    sc.blit(rot, rect)
    ###########
    test()
    ###########    
    cars.draw(sc)
    pygame.display.update()
    pygame.time.delay(20)
    cars.update()
