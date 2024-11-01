import random
import arcade
import os 
import enemy 
import laser 
import myShip
from settings import *



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.player_list = None
        self.alien_list = None
        self.bullet_list = None
        self.powerful_bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.powerful_bullets_left = 10  # Start med 10 kraftige kugler

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = myShip.Ship(PATH_TO_MYSHIP, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the aliens
        for i in range(ALIEN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            alien = enemy.Alien(PATH_TO_ALIEN, SPRITE_SCALING_ALIEN)

            # Position the coin
            alien.center_x = random.randrange(SCREEN_WIDTH)
            alien.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.alien_list.append(alien)
            
            

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.alien_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        # Render teksten for antallet af kraftige kugler tilbage
        arcade.draw_text(f"Kraftige kugler tilbage: {self.powerful_bullets_left}", 10, 50, arcade.color.WHITE, 14)

    
        

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = laser.Bullet(PATH_TO_BULLET, SPRITE_SCALING_LASER)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        # bullet.angle = 90

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)
    
    def on_key_press(self, key, modifiers):
        """den vil blive kaldt på når man trykker på keyboarded"""

        if key == arcade.key.SPACE:
            #Her har lavet en if statement der rent faktisk tjekker
            # det er space der bliver trykket på 
           
            if self.powerful_bullets_left > 0:
                # if statement i forhold til om der bliver tjekket at der er 0 kraftige laser tilbage
            # Det nedenunder er koden der Skyder en kraftigere laser
                powerful_bullet = laser.Bullet(PATH_TO_POWERFUL_BULLET, SPRITE_SCALING_LASER * 3)
            # Jeg starter med at kalde på klassen - den sprite jeg ville have og forstørre den
                powerful_bullet.center_x = self.player_sprite.center_x
                powerful_bullet.center_y = self.player_sprite.center_y
            # det her er for er x og y position på laseren 
                powerful_bullet.change_y = 20  
            # det her er hastigheden på den kraftig laser op ad y aksen
                self.bullet_list.append(powerful_bullet)

            #den fjerne 1 med hvor mange kraftige laser vi har tilbage
                self.powerful_bullets_left -= 1

            




       





            

                  

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.alien_list.update()
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.alien_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for alien in hit_list:
                alien.remove_from_sprite_lists()
                self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
