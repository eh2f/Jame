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

