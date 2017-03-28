import pygame as pg
from pygame.locals import *
import sys, time, pyglet
from random import randint, uniform


class Game():
    def __init__(self, acceleration_step):
        self.set_screen()
        pg.key.set_repeat(400,30)
        self.bgcolor = 0, 0, 0
        self.x_speed, self.y_speed = 0, 10
        self.x_acceleration, self.y_acceleration = 0, 0
        self.load_player()
        self.salade()
        self.tomate()
        self.poulet()
        self.sauce()
        self.acceleration_step = acceleration_step


    #Get surface of default monitor
    def get_monitor_surface(self):
        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        screen = display.get_default_screen()
        screen_width = screen.width
        screen_height = screen.height
        return [screen_width, screen_height]

    #Define screen parameters
    def set_screen(self):
        self.screen = pg.display.set_mode((self.get_monitor_surface()[0], self.get_monitor_surface()[1]), pg.FULLSCREEN)
        self.screen_width = pg.display.Info().current_w
        self.screen_height = pg.display.Info().current_h

    #Load player sprite
    def load_player(self):
        self.kebab_player = pg.image.load("images/kebab.png")
        self.kebab_rect = self.kebab_player.get_rect()
        self.kebab_rect.center = int(self.screen_width/2), int(self.screen_height-100)
        self.screen.blit(self.kebab_player, self.kebab_rect.center)
        pg.display.flip()

    def tomate(self):
        self.kebab_tomate = pg.image.load("images/tomate.png")
        self.tomate_rect = self.kebab_tomate.get_rect()
        self.tomate_rect.left = randint(0, self.screen_width-100)
        pg.display.flip()

    def salade(self):
        self.kebab_salade = pg.image.load("images/salade.png")
        self.salade_rect = self.kebab_salade.get_rect()
        self.salade_rect.left = randint(0, self.screen_width-100)
        pg.display.flip()

    def poulet(self):
        self.kebab_poulet = pg.image.load("images/poulet.png")
        self.poulet_rect = self.kebab_poulet.get_rect()
        self.poulet_rect.left = randint(0, self.screen_width-100)
        pg.display.flip()

    def sauce(self):
        self.kebab_sauce = pg.image.load("images/sauce.png")
        self.sauce_rect = self.kebab_sauce.get_rect()
        self.sauce_rect.center = int(self.screen_width/2), 100
        self.screen.blit(self.kebab_sauce, self.sauce_rect)

class set_bgimg():
    def __init__(self, img_path):
        #Call sprite in this class
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]

game = Game(50)
bg = set_bgimg("images/bg.png")

while True:
    if game.tomate_rect.top < game.screen_width-game.tomate_rect.width :
        game.tomate_rect = game.tomate_rect.move(game.x_speed, game.y_speed)
        if game.tomate_rect.bottom > game.screen_height:
            game.tomate_rect.top, game.tomate_rect.left = 0, randint(0, game.screen_width-100)

    if game.poulet_rect.top < game.screen_width-game.poulet_rect.width :
        game.poulet_rect = game.poulet_rect.move(game.x_speed, game.y_speed)
        if game.poulet_rect.bottom > game.screen_height :
            game.poulet_rect.top, game.poulet_rect.left = 0, randint(0, game.screen_width-100)

    if game.salade_rect.top < game.screen_width-game.salade_rect.width :
        game.salade_rect = game.salade_rect.move(game.x_speed, game.y_speed)
        if game.salade_rect.bottom > game.screen_height :
            game.salade_rect.top, game.salade_rect.left = 0, randint(0, game.screen_width-100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                if game.kebab_rect.left > game.screen_width-game.kebab_rect.width:
                    game.x_acceleration = 0
                else:
                    game.x_acceleration = game.acceleration_step
                game.kebab_rect = game.kebab_rect.move(game.x_acceleration, game.y_acceleration)
            elif event.key == pg.K_LEFT:
                if game.kebab_rect.left < 0:
                    game.x_acceleration = 0
                else:
                    game.x_acceleration = -(game.acceleration_step)
                game.kebab_rect = game.kebab_rect.move(game.x_acceleration, game.y_acceleration)
            elif event.key == pg.K_ESCAPE:
                sys.exit()



    game.screen.fill(game.bgcolor)
    game.screen.blit(pg.transform.scale(bg.image, (game.screen_width, game.screen_height)), (0, 0))
    game.screen.blit(game.kebab_player, game.kebab_rect)
    game.screen.blit(game.kebab_tomate, game.tomate_rect)
    game.screen.blit(game.kebab_salade, game.salade_rect)
    game.screen.blit(game.kebab_poulet, game.poulet_rect)
    game.screen.blit(game.kebab_sauce, game.sauce_rect)
    pg.display.flip()
