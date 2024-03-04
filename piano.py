import pygame
import time
import piano_lists as pl
import serial.tools.list_ports

serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = "/dev/cu.usbmodem11301"
serialInst.open()

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)

fps = 60
timer = pygame.time.Clock()
WIDTH = 40 * 35
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH, HEIGHT])

active_keys = []

def draw_piano(keys, played):
    key_rects = []
    for i in range(10):
        rect = pygame.draw.rect(screen, 'white', [i * 140, HEIGHT - 600, 140, 600], 0, 2)
        key_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 140, HEIGHT - 600, 140, 600], 2, 2)
        key_label = font.render(pl.notes[i], True, 'black')
        screen.blit(key_label, (i * 140 + 3, HEIGHT - 60))

    notice_label = medium_font.render("(Sharps/flats don't work :P)", True, 'black')
    screen.blit(notice_label, (0, 0))
    pygame.draw.rect(screen, 'black', [110, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [250, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [530, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [670, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [810, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [1090, HEIGHT - 600, 60, 325], 0, 2)
    pygame.draw.rect(screen, 'black', [1230, HEIGHT - 600, 60, 325], 0, 2)


    for i in range(len(keys)):
        if keys[i][1] > 0:
            j = keys[i][0]
            pygame.draw.rect(screen, 'green', [j * 140, HEIGHT - 600, 140, 600], 2, 2)
            keys[i][1] -= 1
    
    play_rect = pygame.draw.rect(screen, 'white', [500, 0, 400, 100], 0, 2)
    pygame.draw.rect(screen, 'black', [500, 0, 400, 100], 2, 2)
    play_label = medium_font.render("PLAY", True, 'black')
    screen.blit(play_label, (670, 25))

    if played:
        pygame.draw.rect(screen, 'green', [500, 0, 400, 100], 2, 2)
    
    return key_rects, keys, play_rect
    
played_keys = []
pauses = []

played = False
run = True

def current_milli_time():
    return round(time.time() * 1000)

prev = None
while run:
    timer.tick(fps)
    screen.fill('gray')
    
    keys, active_keys, play_rect = draw_piano(active_keys, played)
    played = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Using keyboard to play notes
        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key)

            if key_pressed == 'a':
                active_keys.append([0, 30])
                played_keys.append(pl.notes[0])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                    
                prev = current_milli_time()
            elif key_pressed == 's':
                active_keys.append([1, 30])
                played_keys.append(pl.notes[1])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'd':
                active_keys.append([2, 30])
                played_keys.append(pl.notes[2])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'f':
                active_keys.append([3, 30])
                played_keys.append(pl.notes[3])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'g':
                active_keys.append([4, 30])
                played_keys.append(pl.notes[4])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'h':
                active_keys.append([5, 30])
                played_keys.append(pl.notes[5])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'j':
                active_keys.append([6, 30])
                played_keys.append(pl.notes[6])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'k':
                active_keys.append([7, 30])
                played_keys.append(pl.notes[7])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == 'l':
                active_keys.append([8, 30])
                played_keys.append(pl.notes[8])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()
            elif key_pressed == ';':
                active_keys.append([9, 30])
                played_keys.append(pl.notes[9])

                if prev is not None:
                    diff = current_milli_time() - prev
                    pauses.append(diff)
                        
                prev = current_milli_time()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(keys)):
                if keys[i].collidepoint(event.pos):
                    active_keys.append([i, 30])           
                    played_keys.append(pl.notes[i])  
                    
                    if prev is not None:
                        diff = current_milli_time() - prev
                        pauses.append(diff)
                        
                    prev = current_milli_time()
            
            if play_rect.collidepoint(event.pos):
                played = True

                played_notes = ""

                # Alternate popping from notes and pauses
                while len(played_keys) > 0 and len(pauses) > 0:
                    # Pop from notes first
                    played_notes += played_keys.pop(0)
                    # then pop from pauses
                    curr_pause = pauses.pop(0)
                    while curr_pause > 0:
                        played_notes += 'X'
                        curr_pause = curr_pause - 10
                
                print(played_keys)
                if len(played_keys) > 0:
                    played_notes += played_keys.pop(0)

                print(played_notes)

                played_keys = []
                pauses = []
                prev = None

                serialInst.write(played_notes.encode('utf-8'))
                serialInst.reset_input_buffer()
                serialInst.reset_output_buffer()
                    
    pygame.display.flip()

pygame.quit()

    
