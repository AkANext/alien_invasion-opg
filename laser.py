import random 
import arcade 
from settings import *

class Bullet(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        speed = random.randint(8, 20)
        # det her er for at der bliver en tilfældig hastighed mellem og 8 og 20 der bliver generet for hver tryk
        self.change_x = 0  
        self.change_y = speed

    def update(self):
        # Move the bullet
        self.center_x += self.change_x
        self.center_y += self.change_y

        


