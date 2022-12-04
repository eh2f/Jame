import pygame

def __init__(self, pos, Level):
    super().__init__()
    # player class attributes
    self.image = pygame.Surface((32, 64))
    self.image.fill('orange')
    self.rect = self.image.get_rect(topleft=pos)
    self.direction = pygame.math.Vector2(0, 0)
    self.level = Level

    # player movement attributes
    self.speed = 3
    self.gravity = 0.8
    self.jump_speed = -16
    self.jump_count = 0
    self.single_jump = True
    self.double_jump = True
    self.temp_speed = 1