from time import perf_counter, sleep, strftime
from random import randint
from pygame import mixer
from pygame.time import delay

def minutes_to_miliseconds(minutes):
    return minutes*60*1000

def print_time(to):
    seconds = 0
    minutes = 0
    while True:
        if seconds > 58:
            minutes += 1
            seconds = -1
            
        if minutes > to:
            break
        
        if seconds > 9:
            print(f'0{minutes}:{seconds}')
        elif minutes > 9 and seconds > 9:
            print(f'{minutes}:{seconds}')
        else:
            print(f'0{minutes}:0{seconds}')
            
        seconds += 1
        sleep(1)
    return
        
def find_user_sounds():
    pass

mixer.init()

# Standart sounds.
work_sound = mixer.Sound('let_the_cornage_begin.ogg')
rest_sound = mixer.Sound('jake_scores_nockout.wav')

mixer.music.set_volume(0.5)

# Randomize between two background songs.
num = randint(0, 1)
if num:
    print("\nCurrently playing: Rock'n'roll Racer - Paranoid\n\n")
    mixer.music.load('paranoid.mp3')
if not num:
    print("\nCurrently playing: Rock'n'roll Racer - Bad To The Bone\n\n")
    mixer.music.load('bad_to_the_bone.mp3')
mixer.music.play()

ERROR = "\nWrong input"

# Main loop.
while True:
    timer_type = input("Enter timer type - long/short: ")
    if timer_type.lower() == 'long':
        work = 45 # minutes
        rest = 15 # minutes
    elif timer_type.lower() == 'short':
        work = 25
        rest = 5 
    else:
        print(ERROR)
        continue

    try:
        rounds = int(input("How many rounds?: "))
    except:
        print(ERROR)
        continue
    
    sounds = input("Do you want set your own sounds?: ")
    if sounds.lower() in ('y', 'yes'):
        find_user_sounds()

    music = input("Do you want to turn off music?: ")
    if music.lower() in ('y', 'yes'):
        mixer.music.stop()
        
    for i in range(rounds):
        print("WORK")
        work_sound.play()
        print_time(work)
        print("REST")
        rest_sound.play()
        print_time(rest)
