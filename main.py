import pygame
import sys
from Level import *
from setting import *

# initialization of pygame and pygame fonts
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))


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

