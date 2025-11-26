"""The main file of our game"""

import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()
TILED_WIDTH: int = 16
TILED_HEIGHT: int = 9
TILE_SIZE: int = 80
SCREEN_WIDTH: int = TILED_WIDTH * TILE_SIZE
SCREEN_HEIGHT: int = TILED_HEIGHT * TILE_SIZE
VELOCITY: int = 2
screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pg.time.Clock = pg.time.Clock()
title_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Blocks.ttf", 36)
subtitle_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Future.ttf", 18)


# load and scale grass (road) tiles
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

grass_tile_blank_tower_og = pg.image.load(
    "./assets/tiles/towerDefense_tile042.png"
)  # grass tile with possible/ blank tower
grass_tile_blank_tower = pg.transform.scale(
    grass_tile_blank_tower_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

grass_tile_mechanic_tower_og = pg.image.load(
    "./assets/tiles/towerDefense_tile043.png"
)  # grass tile with mechanic tower
grass_tile_mechanic_tower = pg.transform.scale(
    grass_tile_mechanic_tower_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

grass_tile_cross_tower_og = pg.image.load(
    "./assets/tiles/towerDefense_tile044.png"
)  # grass tile with cross tower
grass_tile_cross_tower = pg.transform.scale(
    grass_tile_cross_tower_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

grass_tile_circle_tower_og = pg.image.load(
    "./assets/tiles/towerDefense_tile045.png"
)  # grass tile with circle tower
grass_tile_circle_tower = pg.transform.scale(
    grass_tile_circle_tower_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

mountain_on_bottom_og = pg.image.load(
    "./assets/photoshopped/mountain_on_bottom.png"
)  # grass tile with mountain on bottom
mountain_on_bottom = pg.transform.scale(
    mountain_on_bottom_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

mountain_on_bottom_and_side_og = pg.image.load(
    "./assets/photoshopped/mountain_on_bottom_and_side.png"
)  # grass tile with mountain on bottom and side
mountain_on_bottom_and_side = pg.transform.scale(
    mountain_on_bottom_and_side_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

mountain_on_corner_og = pg.image.load(
    "./assets/photoshopped/mountain_on_corner.png"
)  # grass tile with mountain on corner
mountain_on_corner = pg.transform.scale(
    mountain_on_corner_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

stone_tower_blank_og = pg.image.load(
    "./assets/tiles/towerDefense_tile088.png"
)  # stone tower blank
stone_tower_blank = pg.transform.scale(
    stone_tower_blank_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

stone_tower_mechanic_og = pg.image.load(
    "./assets/tiles/towerDefense_tile089.png"
)  # stone tower mechanic
stone_tower_mechanic = pg.transform.scale(
    stone_tower_mechanic_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

stone_tower_cross_og = pg.image.load(
    "./assets/tiles/towerDefense_tile090.png"
)  # stone tower cross
stone_tower_cross = pg.transform.scale(
    stone_tower_cross_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

stone_tower_circle_og = pg.image.load(
    "./assets/tiles/towerDefense_tile091.png"
)  # stone tower circle
stone_tower_circle = pg.transform.scale(
    stone_tower_circle_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
mountain_on_bottom_and_side_22_og = pg.image.load(
    "./assets/photoshopped/mountain_on_bottom_and_side_22.png"
)  # grass tile with mountain on bottom and side
mountain_on_bottom_and_side_22 = pg.transform.scale(
    mountain_on_bottom_and_side_22_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
mountain_on_bottom_and_side_3_og = pg.image.load(
    "./assets/photoshopped/mountain_on_bottom_and_side_3.png"
)  # grass tile with mountain on bottom and side
mountain_on_bottom_and_side_3 = pg.transform.scale(
    mountain_on_bottom_and_side_3_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
mountain_on_side_22_og = pg.image.load(
    "./assets/photoshopped/mountain_on_side_21.png"
)  # grass tile with mountain on side
mountain_on_side_22 = pg.transform.scale(
    mountain_on_side_22_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
mountain_road_bottom_og = pg.image.load("./assets/tiles/towerDefense_tile011.png")
mountain_road_bottom = pg.transform.scale(
    mountain_road_bottom_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)

mountain_og = pg.image.load("./assets/tiles/towerDefense_tile034.png")
mountain = pg.transform.scale(
    mountain_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)


# swedish flag
swedish_flag_og = pg.image.load("./assets/custom/Swedish Flag.png").convert()
swedish_flag = pg.transform.scale(swedish_flag_og, (50, 31))  # scale the image
swedish_flag_rect = swedish_flag.get_rect()
swedish_flag_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

# load entities
loris_entity_og = pg.image.load("./assets/custom/loris_entity.png").convert_alpha()
gabriel_entity_og = pg.image.load("./assets/custom/gabriel_entity.png").convert_alpha()
gabriel_entity2_og = pg.image.load(
    "./assets/custom/gabriel_entity2.png"
).convert_alpha()
phillippe_entity_og = pg.image.load(
    "./assets/custom/phillippe_entity.png"
).convert_alpha()

# load weapons
soldier1_og = pg.image.load("./assets/tiles/towerDefense_tile245.png")
soldier1 = pg.transform.scale(
    soldier1_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
soldier2_og = pg.image.load("./assets/tiles/towerDefense_tile246.png")
soldier2 = pg.transform.scale(
    soldier2_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
missile_launcher_og = pg.image.load("./assets/tiles/towerDefense_tile204.png")
missile_launcher = pg.transform.scale(
    missile_launcher_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
turret_og = pg.image.load("./assets/tiles/towerDefense_tile250.png")
turret = pg.transform.scale(
    turret_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)


class Game:
    """Stores Variables and methods needed to control the game."""

    state: str = "start"

    player_hp: float = 1000

    entities: list["Entity"] = []

    def __init__(self) -> None:
        running: bool = True

        self.entities.append(Entity(loris_entity_og))

        pg.mixer.music.load("intro.mp3")
        pg.mixer.music.play(loops=0)
        pg.mixer.music.stop()
        pg.mixer.music.load("afterintro.mp3")
        pg.mixer.music.play(loops=-1)

        while running:
            for event in pg.event.get():
                if event.type == pg.constants.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and self.state == "start":
                        self.state = "game"
                        self.reset(1)

            # start screen if:
            if self.state == "start":
                self.reset(2)
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

            elif self.state == "game":
                # rerender background
                self.reset(2)

                grass_road_tile_positions = [
                    [4, 2],
                    [3, 2],
                    [2, 7],
                    [3, 7],
                    [4, 7],
                    [5, 7],
                    [6, 7],
                    [7, 7],
                    [8, 7],
                    [9, 7],
                    [10, 7],
                    [12, 5],
                    [13, 5],
                    [14, 5],
                    [15, 5],
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
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [1, 5],
                    [1, 6],
                    [10, 5],
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
                    [2, 3],
                    [2, 4],
                    [2, 5],
                    [11, 6],
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
                    [4, 1, 0],
                    [2, 2, 180],
                    [2, 6, 270],
                    [10, 6, 0],
                    [11, 5, 180],
                ]  # for all tiles that have a big bombaclat turn
                for i in grass_road_tile_bigturn_downleft_positions:
                    screen.blit(
                        pg.transform.rotate(grass_road_tile_bigturn_downleft, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_road_tile_turning_downleft_positions = [
                    [5, 2],
                    [11, 7],
                ]  # for all tiles that turn left downwards
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
                    [2, 1],
                    [3, 6],
                    [4, 6],
                    [5, 6],
                    [6, 6],
                    [7, 6],
                    [8, 6],
                    [9, 6],
                    [11, 4],
                    [12, 4],
                    [13, 4],
                    [14, 4],
                    [15, 4],
                ]  # for all tiles that have grass on top
                for i in grass_road_tile_reverse_positions:
                    screen.blit(
                        grass_road_tile_reverse,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_road_tile_turning_upright_positions = [
                    [1, 1],
                    [10, 4],
                ]  # for all tiles that turn to the right going upwards
                for i in grass_road_tile_turning_upright_positions:
                    screen.blit(
                        grass_road_tile_turning_upright,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_road_tile_turning_downright_positions = [
                    [1, 7],
                ]  # for all tiles that turn to the right going down
                for i in grass_road_tile_turning_downright_positions:
                    screen.blit(
                        grass_road_tile_turning_downright,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_tile_mechanic_tower_positions = [
                    [3, 0],
                ]  # for all grass tiles with mechanic symbol
                for i in grass_tile_mechanic_tower_positions:
                    screen.blit(
                        grass_tile_mechanic_tower,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_tile_circle_tower_positions = [
                    [6, 0],
                ]  # for all grass tiles with circle symbol
                for i in grass_tile_circle_tower_positions:
                    screen.blit(
                        grass_tile_circle_tower,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                grass_tile_cross_tower_positions = [
                    [7, 0],
                ]  # for all grass tiles with mechanic symbol
                for i in grass_tile_cross_tower_positions:
                    screen.blit(
                        grass_tile_cross_tower,
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_bottom_positions = [
                    [13, 6, 0],
                ]  # for all tiles that mountain on bottom
                for i in mountain_on_bottom_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_bottom, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_bottom_and_side_positions = [
                    [12, 7, 0],
                    [5, 8, 270],
                    [10, 8, 0],
                ]
                for i in mountain_on_bottom_and_side_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_bottom_and_side, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_corner_positions = [
                    [12, 3, 0],
                ]  # for all tiles that mountain on bottom and side
                for i in mountain_on_corner_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_corner, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_bottom_and_side_22_positions = [
                    [14, 6, 0],
                ]  # for all tiles that mountain on bottom and side
                for i in mountain_on_bottom_and_side_22_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_bottom_and_side_22, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_bottom_and_side_3_positions = [
                    [14, 2, 0],
                ]  # for all tiles that mountain on bottom and side
                for i in mountain_on_bottom_and_side_3_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_bottom_and_side_3, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )
                mountain_on_side_22_positions = [
                    [14, 1, 0],
                ]  # for all tiles that mountain on side
                for i in mountain_on_side_22_positions:
                    screen.blit(
                        pg.transform.rotate(mountain_on_side_22, i[2]),
                        (
                            i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                            i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                        ),
                    )

                # weapons bar
                mountain_road_bottom_positions = [
                    [5, 7],
                    [6, 7],
                    [7, 7],
                    [8, 7],
                    [9, 7],
                    [10, 7],
                ]
                for i in mountain_road_bottom_positions:
                    screen.blit(
                        mountain_road_bottom,
                        (
                            i[0] * TILE_SIZE,
                            i[1] * TILE_SIZE,
                        ),
                    )

                mountain_positions = [
                    [6, 8],
                    [6, 8],
                    [7, 8],
                    [8, 8],
                    [9, 8],
                ]
                for i in mountain_positions:
                    screen.blit(
                        mountain,
                        (
                            i[0] * TILE_SIZE,
                            i[1] * TILE_SIZE,
                        ),
                    )
                screen.blit(soldier1, (6 * TILE_SIZE, 8 * TILE_SIZE))
                screen.blit(soldier2, (7 * TILE_SIZE, 8 * TILE_SIZE))
                screen.blit(missile_launcher, (8 * TILE_SIZE, 8 * TILE_SIZE))
                screen.blit(turret, (9 * TILE_SIZE, 8 * TILE_SIZE))

                # entities
                for entity in self.entities:
                    screen.blit(entity.entity, entity.rect)

                for entity in self.entities:
                    if (
                        entity.rect.x > TILE_SIZE * 10.5
                        and entity.rect.y == TILE_SIZE * 4.5
                    ):
                        entity.rect.x -= VELOCITY
                        entity.rotate(90)
                    elif (
                        entity.rect.y < TILE_SIZE * 6.5
                        and entity.rect.x == TILE_SIZE * 10.5
                    ):
                        entity.rect.y += VELOCITY
                        entity.rotate(180)
                    elif (
                        entity.rect.x > TILE_SIZE * 1.5
                        and entity.rect.y == TILE_SIZE * 6.5
                    ):
                        entity.rect.x -= VELOCITY
                        entity.rotate(90)
                    elif (
                        entity.rect.y > TILE_SIZE * 1.5
                        and entity.rect.x == TILE_SIZE * 1.5
                    ):
                        entity.rect.y -= VELOCITY
                        entity.rotate(0)
                    elif (
                        entity.rect.x < TILE_SIZE * 4.5
                        and entity.rect.y == TILE_SIZE * 1.5
                    ):
                        entity.rect.x += VELOCITY
                        entity.rotate(-90)
                    elif (
                        entity.rect.y > -TILE_SIZE and entity.rect.x == TILE_SIZE * 4.5
                    ):
                        entity.rect.y -= VELOCITY
                        entity.rotate(0)
                    else:
                        self.entities.remove(entity)
                        self.player_hp -= entity.entity_hp
                        self.entities.append(Entity(loris_entity_og))

                    # display HP Text
                    hp_text = title_font.render(
                        f"{self.player_hp} HP", True, (255, 255, 255)
                    )
                    hp_text_rect = hp_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
                    screen.blit(hp_text, hp_text_rect)

            # display swedish flag
            screen.blit(swedish_flag, swedish_flag_rect)

            pg.display.flip()

            clock.tick(24)  # limits FPS to 24

        pg.quit()

    def reset(self, option: int):
        """
        Method to reset background and game variables
        Option 1 resets everything (background and variables)
        Option 2 only resets background
        """
        # reset background
        for i in range(TILED_WIDTH):
            for j in range(TILED_HEIGHT):
                screen.blit(
                    grass_tile,
                    (
                        i * (SCREEN_WIDTH / TILED_WIDTH),
                        j * (SCREEN_HEIGHT / TILED_HEIGHT),
                    ),
                )

        if option == 1:
            # reset game variables
            self.player_hp = 1000


class Entity:
    """Creates loris entity and stores its variables."""

    og_image: pg.Surface

    def __init__(self, image: pg.Surface):
        self.og_image = image
        self.entity = pg.transform.rotate(
            pg.transform.scale(self.og_image, (TILE_SIZE, TILE_SIZE)), 90
        )
        self.rect = self.entity.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = round(4.5 * TILE_SIZE)

    def rotate(self, angle: int):
        """Rotates the Entity according to angle parameter"""
        self.entity = pg.transform.rotate(
            pg.transform.scale(self.og_image, (TILE_SIZE, TILE_SIZE)), angle
        )

    entity_hp = 100


game = Game()
