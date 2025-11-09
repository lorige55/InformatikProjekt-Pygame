"""The main file of our game"""

import pygame as pg

pg.init()
pg.font.init()
TILED_WIDTH: int = 16
TILED_HEIGHT: int = 9
TILE_SIZE: int = 80
SCREEN_WIDTH: int = TILED_WIDTH * TILE_SIZE
SCREEN_HEIGHT: int = TILED_HEIGHT * TILE_SIZE
screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pg.time.Clock = pg.time.Clock()
running: bool = True
title_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Blocks.ttf", 36)
subtitle_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Future.ttf", 18)


class Game:
    """Stores Variables needed to control the game."""

    state: str = "start"


# load and scale tiles
grass_tile_og = pg.image.load(
    "./assets/tiles/towerDefense_tile231.png"
).convert()  # load the image
grass_tile = pg.transform.scale(
    grass_tile_og, (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT)
)  # scale the image

grass_road_tile_og = pg.image.load(
    "./assets/tiles/towerDefense_tile001.png"
)  # road tile with grass on bottom side
grass_road_tile = pg.transform.scale(
    grass_road_tile_og, (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT)
)

grass_road_tile_turning_upleft_og = pg.image.load(  # tile going turning left going up
    "./assets/tiles/towerDefense_tile004.png"
)
grass_road_tile_turning_upleft = pg.transform.scale(
    grass_road_tile_turning_upleft_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_turning_upright_og = pg.image.load(  # tile going turning right going up
    "./assets/tiles/towerDefense_tile003.png"
)
grass_road_tile_turning_upright = pg.transform.scale(
    grass_road_tile_turning_upright_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_turning_downleft_og = pg.image.load(
    "./assets/tiles/towerDefense_tile027.png"
)  # road tile turning left going down
grass_road_tile_turning_downleft = pg.transform.scale(
    grass_road_tile_turning_downleft_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_turning_downright_og = pg.image.load(
    "./assets/tiles/towerDefense_tile026.png"
)  # road tile turning right going down
grass_road_tile_turning_downright = pg.transform.scale(
    grass_road_tile_turning_downright_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

grass_road_tile_down_left_og = pg.image.load(
    "./assets/tiles/towerDefense_tile025.png"
)  # road tile with grass on left side
grass_road_tile_down_left = pg.transform.scale(
    grass_road_tile_down_left_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_down_right_og = pg.image.load(
    "./assets/tiles/towerDefense_tile023.png"
)  # road tile with grass on right side
grass_road_tile_down_right = pg.transform.scale(
    grass_road_tile_down_right_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_bigturn_downleft_og = pg.image.load(
    "./assets/tiles/towerDefense_tile048.png"
)  # road tile with big bombaclat turn
grass_road_tile_bigturn_downleft = pg.transform.scale(
    grass_road_tile_bigturn_downleft_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
grass_road_tile_reverse_og = pg.image.load(
    "./assets/tiles/towerDefense_tile047.png"
)  # road tile with grass on top side
grass_road_tile_reverse = pg.transform.scale(
    grass_road_tile_reverse_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

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
        grass_road_tile_positions = [
            [4, 2],
            [3, 2],
        ]  # for all tiles that have a grass road where the grass part is on the bottom side
        for i in grass_road_tile_positions:
            screen.blit(
                grass_road_tile,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )
        grass_road_tile_down_left_positions = [
            [4, 0],
            [9, 0],
        ]  # for all tiles that have a grass road where the grass part is on the left side
        for i in grass_road_tile_down_left_positions:
            screen.blit(
                grass_road_tile_down_left,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )
        grass_road_tile_down_right_positions = [
            [5, 0],
            [5, 1],
        ]  # for all tiles that have a grass road where the grass part is on the right side
        for i in grass_road_tile_down_right_positions:
            screen.blit(
                grass_road_tile_down_right,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )
        grass_road_tile_bigturn_downleft_positions = [
            [4, 1],
            [8, 1],
        ]  # for all tiles that have a big bombaclat turn
        for i in grass_road_tile_bigturn_downleft_positions:
            screen.blit(
                grass_road_tile_bigturn_downleft,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )
        grass_road_tile_turning_downleft_positions = [
            [5, 2],
            [8, 2],
        ]  # for all tiles that have a big bombaclat turn
        for i in grass_road_tile_turning_downleft_positions:
            screen.blit(
                grass_road_tile_turning_downleft,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )
        grass_road_tile_reverse_positions = [
            [3, 1],
            [8, 3],
        ]  # for all tiles that have grass on top
        for i in grass_road_tile_reverse_positions:
            screen.blit(
                grass_road_tile_reverse,
                (
                    i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                    i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                ),
            )

    # display swedish flag
    screen.blit(swedish_flag, swedish_flag_rect)

    pg.display.flip()

    clock.tick(24)  # limits FPS to 24

pg.quit()
