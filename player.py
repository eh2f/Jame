import pygame

class Player(pygame.sprite.Sprite):
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

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # adds positive value to x component of movement vector
            self.direction.x = self.temp_speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # adds negative value to x component of movement vector
            self.direction.x = -self.temp_speed
        else:
            self.direction.x = 0

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and (self.direction.y == 0):
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
