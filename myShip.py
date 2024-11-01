import arcade

class Ship(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling) 
        self.change_x = 0
        self.change_y = 0
    
    def update(self):
        """
         This update method is automatically called to update the sprite's
        position
        """
        self.center_x += self.change_x
        self.center_y += self.change_y


