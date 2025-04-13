import pygame
pygame.init

screen = pygame.display.set_mode((640,420))

# load files
#bg_music = pygame.mixer.Sound("sound/sneaky snitch.mp3")
#bg_music.play(loops =-1)

# background
sky_service = pygame.image.load("image/sky.jpg")
ground_surface = pygame.image.load("image/grass.jpg")

clock = pygame.time.Clock()

# game loop 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_service,(0,0))
    screen.blit(ground_surface,(0,320))
    pygame.display.update()
    clock.tick(60)
            
        