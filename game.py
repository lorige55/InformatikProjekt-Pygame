import pygame

# pygame setup gemäss quickstart vorlage - pygame.org
pygame.init()
screen = pygame.display.set_mode((1280, 720))
width = 16
height = 9
clock = pygame.time.Clock()
running = True

# background
grassTileOG = pygame.image.load("./assets/tiles/towerDefense_tile231.png").convert()    # load the image
grassTile = pygame.transform.scale(grassTileOG, (1280/width, 720/height))   # scale the image
# fill the screen with the grass tile
for i in range(width):
    for j in range(height):
        screen.blit(grassTile, (i * (1280/width), j * (720/height)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()