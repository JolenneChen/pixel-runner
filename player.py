import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super.init()
        player_walk_1= pygame.image.load("images/player/princess_walk1.png")
        player_walk_2= pygame.image.load("images/player/princess_walk2.png")

        