import random
import arcade
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

# Importere screen height og width fra settings så vi kan kalde på den for at sprite bouncer fra limit væggen 

class Alien(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling) 

        self.change_x = 0
        self.change_y = 0
        
        # Jeg definere en værdi for x og y så det give mening af tilføje og trække fra 

        speed_x = random.randint(2, 3)
        speed_y = random.randint(2, 3)
        # det for at give en random fart i x og y ligesom jeg har gjort med laseren

        self.change_x += speed_x
        self.change_y += speed_y
    # fordi jeg har defineret værdien og pluser med speed sker der en ændring til i 
    #forhold til forhendværende kode hvor det var 0+0 er det nu 0 + random mellem 2 og 3

    def update(self):
        """
         This update method is automatically called to update the sprite's
        position
        """
        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

            # stærkt inspiret fra kapitiel 22.1. Moving Sprites Down

