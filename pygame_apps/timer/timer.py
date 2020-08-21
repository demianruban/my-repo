import pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# First appearance of the app
sc = pygame.display.set_mode((400, 300))
sc.fill(BLACK)
        
font = pygame.font.Font(None, 30)
button = font.render("Set timer", 1, BLACK, WHITE)
b_rect = button.get_rect(center=(200, 150))

sc.blit(button, b_rect)

pygame.display.update()

##############################
# Text input phase variables (second-third appearance).
note = font.render("Enter work time (minutes):", 1, WHITE)
note_rect = note.get_rect(center=(200, 150))

work_time = ''
input_work_time = False
rest_time = ''
input_rest_time = False
field = font.render(work_time, 1, BLACK, WHITE)
field_rect = field.get_rect(center=(200, 150+b_rect.height))

enable_text_input = False

##############################

# FPS handler
clock = pygame.time.Clock()

print(pygame.NUMEVENTS)

while 1:
    sc.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

        if enable_text_input:
            if i.type == pygame.KEYDOWN:
                key = pygame.key.name(i.key)
                if key in [str(x) for x in range(10)]:
                    if input_work_time:
                        work_time += key
                        string = work_time
                    elif input_rest_time:
                        rest_time += key
                        string = rest_time
                elif key == 'return' and len(string) > 1:
                    if input_work_time:
                        input_work_time = False
                    elif input_rest_time:
                        input_rest_time = False
                    print(work_time)
                    print(rest_time)
                    input_rest_time = True
                    note = font.render("Enter rest time:", 1, WHITE)
                    note_rect = note.get_rect(center=(200, 150))

    if enable_text_input:
        sc.blit(note, note_rect)
        if input_work_time:
            field = font.render(work_time, 1, BLACK, WHITE)
        elif input_rest_time:
            field = font.render(rest_time, 1, BLACK, WHITE)
        field_rect = field.get_rect(center=(200, 150+b_rect.height))
        sc.blit(field, field_rect)
        pygame.display.update()

    pos = pygame.mouse.get_pos()


    if not enable_text_input:
        if b_rect.collidepoint(pos):
            button = font.render("Set timer", 1, (100, 100, 100), WHITE)
            sc.blit(button, b_rect)
            pygame.display.update()
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                enable_text_input = True
                input_work_time = True
        else:
            button = font.render("Set timer", 1, BLACK, WHITE)
            sc.blit(button, b_rect)
            pygame.display.update()

    clock.tick(30)
    
