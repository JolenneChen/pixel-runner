import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super.init()
        player_walk_1= pygame.image.load("images/player/princess_walk1.png")
        player_walk_2= pygame.image.load("images/player/princess_walk2.png")

        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("images/player/princess_jumping1")
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.sound("sound/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def clear_input(self): 
        keys = pygame.ket.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 :
            self.gravity = -20
            self.jump_sound.play()

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player.jump()
        else :
            self.player_index += 0.1
            if self.player_index  >= len(self.walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300 :
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        

        

        