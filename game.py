"""The main file of our game"""

import pygame as pg

# pygame setup gemäss quickstart vorlage - pygame.org
pg.init()
screen: pg.Surface = pg.display.set_mode((1280, 720))
WIDTH: int = 16
HEIGHT: int = 9
clock: pg.time.Clock = pg.time.Clock()
running: bool = True

# background
grass_tile_og = pg.image.load(
    "./assets/tiles/towerDefense_tile231.png"
).convert()  # load the image
grass_tile = pg.transform.scale(
    grass_tile_og, (1280 / WIDTH, 720 / HEIGHT)
)  # scale the image

# fill the screen with the grass tile
for i in range(WIDTH):
    for j in range(HEIGHT):
        screen.blit(grass_tile, (i * (1280 / WIDTH), j * (720 / HEIGHT)))

while running:
    for event in pg.event.get():
        if event.type == pg.constants.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(24)  # limits FPS to 24

pg.quit()
