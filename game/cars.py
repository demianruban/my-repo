from random import choice as random_choice
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1500)

boom = pygame.mixer.Sound('boom.wav')

W = 400
H = 400
GREY = (100, 100, 100)
CARS_SURF = []

sc = pygame.display.set_mode((W, H))
 
for i in ('car1.png', 'car2.png', 'car3.png'):
    CARS_SURF.append(pygame.image.load(i).convert_alpha())

CAR_W = CARS_SURF[0].get_width()


ROAD_LINES = []
x = W
for i in range(W // CAR_W):
    x -= CAR_W
    ROAD_LINES.append(x)


class Car(pygame.sprite.Sprite):
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
 
cars = pygame.sprite.Group()

cars_on_screen = [Car(random_choice(ROAD_LINES), random_choice(CARS_SURF), cars)]

car = pygame.image.load('car.png')
rect = car.get_rect(center=(W // 2, H - car.get_width()))
rot = car.copy()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.USEREVENT:
            cars_on_screen.append(
            Car(random_choice(ROAD_LINES), random_choice(CARS_SURF), cars))

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

    for npc_car in cars_on_screen:
        if rect.colliderect(npc_car):
            boom.play()
            sc.blit(pygame.font.Font(None, 50).render("Eblan", 0, (255, 255, 255)), (200, 200))
            pygame.display.update()
            pygame.time.wait(1500)
            exit()
 
    sc.fill(GREY)
    sc.blit(rot, rect)
    cars.draw(sc)
    pygame.display.update()
    pygame.time.delay(20)
    cars.update()
