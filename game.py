"""The main file of our game"""

import pygame as pg

pg.init()
pg.font.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TILED_WIDTH: int = 16
TILED_HEIGHT: int = 9
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
    grass_tile_og, (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT)
)  # scale the image

# swedish flag
swedish_flag_og = pg.image.load("./assets/custom/Swedish Flag.png").convert()
swedish_flag = pg.transform.scale(swedish_flag_og, (50, 31))  # scale the image
swedish_flag_rect = swedish_flag.get_rect()
swedish_flag_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    for event in pg.event.get():
        if event.type == pg.constants.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and Game.state == "start":
                Game.state = "game"

    # start screen if:
    if Game.state == "start":
        for i in range(TILED_WIDTH):
            for j in range(TILED_HEIGHT):
                screen.blit(
                    grass_tile,
                    (
                        i * (SCREEN_WIDTH / TILED_WIDTH),
                        j * (SCREEN_HEIGHT / TILED_HEIGHT),
                    ),
                )
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

    # display swedish flag
    screen.blit(swedish_flag, swedish_flag_rect)

    pg.display.flip()

    clock.tick(24)  # limits FPS to 24

pg.quit()
