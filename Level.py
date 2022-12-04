import pygame


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
                    user = Player((self.player_x, self.player_y), LVL)
                    # adds player to level
                    self.player.add(user)
                if(cell == 'F'):
                    self.tile_x = x_pos
                    self.tile_y = y_pos
                    tile = Tile((self.tile_x,self.tile_y), title_size, title_size, 'green')
                    self.tiles.add(tile)
    def run(self):
        pass
