import pygame
from setting import *
from tilesz import *
from player import *
import Level
class level:
    def __init__(self, level_input, surface):
        self.display_surface = surface
        self.level_number = level_input
        self.level(self.level_number)
        self.world_direction = 0
        self.tile_x = 0
        self.tile_y = 0
        self.player_x = 0
        self.player_y = 0
        self.complete = False

    def level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
    
        for row_index,row in enumerate(layout):
            for column_index,cell in enumerate(row):
                y_pos = row_index*title_size
                x_pos = column_index*title_size
                if(cell == 'X'):
                    # positions for the tiles
                    self.tile_x = x_pos
                    self.tile_y = y_pos
                    # creates tile object
                    tile = Tile((self.tile_x,self.tile_y),title_size, title_size, 'blue')
                    # adds tile to screen
                    self.tiles.add(tile)
                if(cell == 'P'):
                    # position of the player
                    self.player_x = x_pos
                    self.player_y = y_pos
                    # makes player object
                    user = Player((self.player_x, self.player_y), Level)
                    # adds player to level
                    self.player.add(user)
                if(cell == 'F'):
                    self.tile_x = x_pos
                    self.tile_y = y_pos
                    tile = Tile((self.tile_x,self.tile_y), title_size, title_size, 'green')
                    self.tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        forward_shift = screen_width - screen_width / 4

        if direction_x < 0:
            if player_x < screen_width / 4:
                self.world_direction = 4
                player.speed = 0
        elif direction_x > 0:
            if player_x > forward_shift:
                self.world_direction = -4
                player.speed = 0
        else:
            self.world_direction = 0
            player.speed = 3
    def x_collision(self):
        player = self.player.sprite
        pos_change = player.direction.x * player.speed
        player.rect.x += pos_change
        # changing orientation depending on collisions
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def y_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        if player.rect.y > screen_height:
            return True
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # print(sprite.rect, self.tiles.sprites()[-1].rect)
                # pygame.draw.rect(self.display_surface, (0, 0, 0), a)
                if self.level_number == level_map_1:
                    if self.tiles.sprites()[-61].rect == sprite.rect:
                        self.complete = True
                elif self.level_number == level_map_2:
                    if self.tiles.sprites()[-1].rect == sprite.rect:
                        self.complete = True
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.update(self.world_direction)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        # player is drawn in level
        self.player.update()
        self.x_collision()
        self.player.draw(self.display_surface)
        # print(self.complete)
        return [self.y_collision(), self.complete]
