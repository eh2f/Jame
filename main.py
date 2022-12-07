#Eric Feng E.F, Shivam Saravanakumar S.S, Vignesh Bhavananthan V.B, Labeeb Nasir L.N

import pygame
import sys
import Level
from setting import *

# initialization of pygame and pygame fonts
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
velX = 3
velY = 2
clock = pygame.time.Clock()
clock_main = pygame.time.Clock()
jumping = False
top = 450


# Function returns the text you would like to display on the screen, uses built-in pygame function
def fonts(size, write, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(write, True, color)
    return text


# Simply checks collision between the mouse and a specified rectangle return true or false
def over_mouse(mouse, another):
    return True if mouse.collidepoint(another[0], another[1]) else False


# Same as the last checks for collision between 2 rectangles returns true or false
def over_rect(rect, another):
    return True if rect.colliderect(another) else False


def animation_fill(color):
    working = True
    pygame.display.set_caption('animating')
    start_rect = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    another_clock = pygame.time.Clock()

    while working:
        another_clock.tick(30)

        pygame.draw.rect(screen, color, start_rect)

        start_rect.x -= 15
        start_rect.y -= 15
        start_rect.width += 30
        start_rect.height += 30

        if start_rect.x < 0 and start_rect.y < 0:
            working = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        pygame.display.update()


# Complete screen which will be shown when the player or user completes a level
def complete():
    working = True
    pygame.display.set_caption('Victory')

    # render the completion text using fonts()
    complete_text = fonts(60, 'Level Complete', (0, 0, 0))
    complete_rect = complete_text.get_rect()

    # sets the complete_text position and uses its center as its reference
    complete_rect.center = (screen_width // 2, screen_height // 2)
    c_rect = pygame.Rect(complete_rect.x - 25, complete_rect.y - 25, complete_rect.width + 50, complete_rect.height + 50)
    c_color = '#57ef58'

    # while true loop to display all things on screen
    while working:
        screen.fill('green')

        # getting mouse position every time the screen is updated
        mouse_pos = pygame.mouse.get_pos()

        # checking for user input to close or quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # checking if mouse and rect collide
            if over_mouse(complete_rect, mouse_pos):
                # this change in color will give a hovering effect where when user hovers above the text it will change
                # colors
                c_color = '#57ef58'
                # only when mouse is hovered above the rectangle and mouse is clicked will this while true loop break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
            else:
                c_color = '#17d918'

        # Just drawing the box that will give the text a hovering effect
        pygame.draw.rect(screen, c_color, c_rect)

        # display both text on to the screen
        screen.blit(complete_text, complete_rect)

        pygame.display.update()


# death screen
def dead():
    working = True
    pygame.display.set_caption('death (use mouse)')

    # render the restart text
    restart_text = fonts(60, 'U dead, Restart', (0, 0, 0))
    restart_rect = restart_text.get_rect()
    restart_rect.center = (screen_width // 2, screen_height // 2)
    r_rect = pygame.Rect(restart_rect.x - 25, restart_rect.y - 25, restart_rect.width + 50, restart_rect.height + 50)
    r_color = '#d32730'

    while working:
        screen.fill('red')
        # getting mouse position every time the screen is updated
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if over_mouse(r_rect, mouse_pos):
                r_color = '#ef575f'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
            else:
                r_color = '#d32730'

        pygame.draw.rect(screen, r_color, r_rect)
        # display both text on to the screen
        screen.blit(restart_text, restart_rect)

        pygame.display.update()


# moving of the character in the level screen
def moving(keys, character, left_right=True):
    global jumping, top

    # check for right key and has to be left_right to be true as if its not true that means that user is going
    # into a level
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and left_right:
        character.x += velX

    # check for left and move left
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and left_right:
        character.x -= velX

    # check for up key, and character has to be on the ground or else character will be able to fly
    if (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]) and character.y == screen_height - 200:
        jumping = True

    # logic for making sure that the character or player has to come down as well not only up
    if jumping:
        if character.y <= top:
            jumping = False
        else:
            character.y -= velY
    else:
        # checking for when character is overlapping the holes as here there is no ground so character should fall
        # all the way down
        first = screen_width / 3 < character.x < screen_width * 1 / 3 + 50
        second = screen_width * 2 / 3 < character.x < screen_width * 2 / 3 + 50

        if first or second:
            lower_bound = screen_height
        else:
            lower_bound = screen_height - 200

        if top <= character.y < lower_bound:
            character.y += velY


def playing(level):
    # creates level object to be printed on screen
    level = Level.Level(level, screen)
    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (screen_width,screen_height))
    # stop process for game
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # fills screen

        # screen.fill('black')
        screen.blit(background,(i,0))
        screen.blit(background,(screen_width+i,0))
        if i == -screen_width:
            screen.blit(background,(screen_width + i,0))
            i = 0
        i -= 1
        # prints all the tiles on the level

        completion = level.run()
        if completion[0]:
            animation_fill('red')
            dead()
            return

        if completion[1]:
            animation_fill('green')
            complete()
            return

        pygame.display.update()
        clock.tick(60)


def leveling():
    # initialization of variables required for the function
    working = True
    pygame.display.set_caption('levels')
    ground = pygame.Rect(0, screen_height - 100, screen_width, 100)
    character = pygame.Rect(100, screen_height - 200, 50, 100)
    another_clock = pygame.time.Clock()

    # main text generation
    text = fonts(60, 'Pick Your Level', (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, 100)

    # level 1 text generation
    level_one_text = fonts(40, 'Level 1', (0, 0, 0))
    level_one_rect = level_one_text.get_rect()
    level_one_rect.topleft = (screen_width // 3, 500)

    # level 1 text generation
    level_two_text = fonts(40, 'Level 2', (0, 0, 0))
    level_two_rect = level_two_text.get_rect()
    level_two_rect.topleft = ((screen_width // 3) * 2, 500)

    # explanation text generation
    explain_text = fonts(20, 'Use A, W, D or arrows to move into a hole', (0, 0, 0))
    explain_rect = explain_text.get_rect()
    explain_rect.topleft = (25, 400)

    # making the rectangle for each level, this will be the hole that the user will jump into to start the level
    level_one = pygame.Rect(screen_width / 3, screen_height - 100, 100, 100)
    level_two = pygame.Rect(screen_width * 2 / 3, screen_height - 100, 100, 100)

    while working:
        another_clock.tick(60)
        screen.fill('grey')

        # rendering all texts
        screen.blit(text, text_rect)
        screen.blit(level_one_text, level_one_rect)
        screen.blit(level_two_text, level_two_rect)
        screen.blit(explain_text, explain_rect)

        keyboard = pygame.key.get_pressed()

        # checks if character or player's rect collides with either level holes
        if over_rect(level_one, character) and over_rect(character, ground):
            # character will no longer be able to move left and right
            moving(keyboard, character, False)
            # renders transition screen
            animation_fill('orange')
            # moves into the playing level
            playing(level_map_1)
            # once everything has been run it means that game will no longer be played so break the loop
            working = False
        elif over_rect(level_two, character) and over_rect(character, ground):
            moving(keyboard, character, False)
            animation_fill('orange')
            # playing(level_map_2)
            working = False

        else:
            moving(keyboard, character)

        # rendering of rectangle for ground, holes and character
        pygame.draw.rect(screen, 'blue', ground)
        pygame.draw.rect(screen, 'black', level_one)
        pygame.draw.rect(screen, 'black', level_two)
        pygame.draw.rect(screen, (0, 0, 0), character)

        # checking for user input to close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        pygame.display.update()


def menu():
    working = True
    pygame.display.set_caption('menu (use mouse)')

    # render the main menu text
    main_text = fonts(60, 'JAME', (0, 0, 0))
    main_rect = main_text.get_rect()
    main_rect.center = (screen_width // 2, 100)

    # render the play text
    play_text = fonts(60, 'PLAY', (0, 0, 0))
    play_rect = play_text.get_rect()
    play_rect.center = (screen_width // 2, 400)
    p_rect = pygame.Rect(play_rect.x-25, play_rect.y-25, play_rect.width+50, play_rect.height+50)
    p_color = '#ebd094'

    # render the quit text
    quit_text = fonts(60, 'QUIT', (0, 0, 0))
    quit_rect = quit_text.get_rect()
    quit_rect.center = (screen_width // 2, 550)
    q_rect = pygame.Rect(quit_rect.x - 25, quit_rect.y - 25, quit_rect.width + 50, quit_rect.height + 50)
    q_color = '#ebd094'
    while working:
        screen.fill('orange')

        # getting mouse position every time the screen is updated
        mouse_pos = pygame.mouse.get_pos()

        # event handler handles all the actions that user can click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if over_mouse(p_rect, mouse_pos):
                p_color = '#d39e27'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    leveling()
            elif over_mouse(q_rect, mouse_pos):
                q_color = '#d39e27'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    working = False
            else:
                p_color = '#ebd094'
                q_color = '#ebd094'

        pygame.draw.rect(screen, p_color, p_rect)
        pygame.draw.rect(screen, q_color, q_rect)
        # updating frame rate

        # display both text on to the screen
        screen.blit(main_text, main_rect)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

        clock_main.tick(60)

        # updating screen
        pygame.display.update()

    pygame.quit()


menu()