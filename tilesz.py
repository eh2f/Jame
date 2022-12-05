import pygame

# class made to create tiles in the screen
class Tile (pygame.sprite.Sprite):
    def __init__(self, pos, x_size, y_size, colour):
        super().__init__()
        # tiles attributes
        self.image = pygame.Surface((x_size, y_size))
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)

    # moves tiles along screen
    def update(self, translate):
        self.rect.x = self.rect.x + translate