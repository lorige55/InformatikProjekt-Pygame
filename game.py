"""The main file of our game"""

import pygame as pg

pg.init()
pg.font.init()
screen: pg.Surface = pg.display.set_mode((1280, 720))
WIDTH: int = 16
HEIGHT: int = 9
clock: pg.time.Clock = pg.time.Clock()
running: bool = True
title_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Blocks.ttf", 36)
subtitle_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Future.ttf", 18)


class Game:
    """Stores Variables needed to control the game."""

    state: str = "start"


# background
grass_tile_og = pg.image.load(
    "./assets/tiles/towerDefense_tile231.png"
).convert()  # load the image
grass_tile = pg.transform.scale(
    grass_tile_og, (1280 / WIDTH, 720 / HEIGHT)
)  # scale the image

while running:
    for event in pg.event.get():
        if event.type == pg.constants.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and Game.state == "start":
                Game.state = "game"

    # start screen if:
    if Game.state == "start":
        for i in range(WIDTH):
            for j in range(HEIGHT):
                screen.blit(grass_tile, (i * (1280 / WIDTH), j * (720 / HEIGHT)))
        # title:
        welcome_title = title_font.render(
            "Welcome to Tower Defense!", True, (187, 127, 68)
        )
        welcome_title_rect = welcome_title.get_rect(center=(640, 340))
        screen.blit(welcome_title, welcome_title_rect)
        # subtitle:
        welcome_subtitle = subtitle_font.render(
            "Press Space to start Game.", True, (187, 127, 68)
        )
        welcome_subtitle_rect = welcome_subtitle.get_rect(center=(640, 380))
        screen.blit(welcome_subtitle, welcome_subtitle_rect)
    elif Game.state == "game":
        # TODO for Gabriel: Render Map
        print("This works.")

    pg.display.flip()

    clock.tick(24)  # limits FPS to 24

pg.quit()
