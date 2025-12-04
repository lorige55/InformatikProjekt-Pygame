"""The main file of our game"""

from __future__ import annotations
import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()
TILED_WIDTH: int = 16
TILED_HEIGHT: int = 9
TILE_SIZE: int = 80
SCREEN_WIDTH: int = TILED_WIDTH * TILE_SIZE
SCREEN_HEIGHT: int = TILED_HEIGHT * TILE_SIZE
VELOCITY: int = 20
SCREEN: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pg.time.Clock = pg.time.Clock()
title_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Blocks.ttf", 36)
subtitle_font: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Future.ttf", 18)

TILES: dict = {
    "grass": {
        "path": "./assets/tiles/towerDefense_tile231.png",
    },
    "grass_road_up": {
        "path": "./assets/tiles/towerDefense_tile047.png",
    },
    "grass_road_down": {"path": "./assets/tiles/towerDefense_tile001.png"},
    "grass_road_left": {"path": "./assets/tiles/towerDefense_tile025.png"},
    "grass_road_right": {"path": "./assets/tiles/towerDefense_tile023.png"},
    "grass_road_turning_upleft": {"path": "./assets/tiles/towerDefense_tile004.png"},
    "grass_road_turning_upright": {"path": "./assets/tiles/towerDefense_tile003.png"},
    "grass_road_turning_downleft": {"path": "./assets/tiles/towerDefense_tile027.png"},
    "grass_road_turning_downright": {"path": "./assets/tiles/towerDefense_tile026.png"},
    "grass_road_bigturning_downleft": {
        "path": "./assets/tiles/towerDefense_tile048.png"
    },
    "grass_freePositon": {"path": "./assets/tiles/towerDefense_tile042.png"},
    "grass_mechanic": {"path": "./assets/tiles/towerDefense_tile043.png"},
    "grass_cross": {"path": "./assets/tiles/towerDefense_tile044.png"},
    "grass_circle": {"path": "./assets/tiles/towerDefense_tile045.png"},
    "mountain": {"path": "./assets/tiles/towerDefense_tile034.png"},
    "mountain_bottom": {"path": "./assets/photoshopped/mountain_bottom.png"},
    "mountain_corner_upleft": {
        "path": "./assets/photoshopped/mountain_corner_upleft.png"
    },
    "mountain_corner_downleft": {
        "path": "./assets/photoshopped/mountain_corner_downleft.png"
    },
    "mountain_corner_downright": {
        "path": "./assets/photoshopped/mountain_corner_downright.png"
    },
    "mountain_bigturning_downright": {
        "path": "./assets/photoshopped/mountain_bigturning_downright.png"
    },
    "mountain_freePosition": {"path": "./assets/tiles/towerDefense_tile088.png"},
    "mountain_mechanic": {"path": "./assets/tiles/towerDefense_tile089.png"},
    "mountain_cross": {"path": "./assets/tiles/towerDefense_tile090.png"},
    "mountain_circle": {"path": "./assets/tiles/towerDefense_tile091.png"},
    "mountain_road_down": {"path": "./assets/tiles/towerDefense_tile011.png"},
}

for key in TILES:
    tile_og = pg.image.load(TILES[key]["path"])
    TILES[key]["object"] = pg.transform.scale(
        tile_og,
        (SCREEN_WIDTH // TILED_WIDTH, SCREEN_HEIGHT // TILED_HEIGHT),
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

    entities: list[Entity] = []

    def __init__(self) -> None:
        running: bool = True

        self.entities.append(Entity(loris_entity_og))

        pg.mixer.music.load("./assets/sound/intro.mp3")
        pg.mixer.music.play(loops=0)
        pg.mixer.music.queue("./assets/sound/afterintro.mp3")

        while running:
            for event in pg.event.get():
                if event.type == pg.constants.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and self.state == "start":
                        self.state = "game"
                        self.reset(1)
                        pg.mixer.music.stop()
                        pg.mixer.music.load("./assets/sound/coconut_mall.mp3")
                        pg.mixer.music.play(loops=-1)

            # start SCREEN if:
            if self.state == "start":
                self.reset(2)
                # title:
                welcome_title = title_font.render(
                    "Welcome to Tower Defense!", True, (187, 127, 68)
                )
                welcome_title_rect = welcome_title.get_rect(center=(640, 340))
                SCREEN.blit(welcome_title, welcome_title_rect)
                # subtitle:
                welcome_subtitle = subtitle_font.render(
                    "Press Space to start Game.", True, (187, 127, 68)
                )
                welcome_subtitle_rect = welcome_subtitle.get_rect(center=(640, 380))
                SCREEN.blit(welcome_subtitle, welcome_subtitle_rect)

            elif self.state == "game":
                # Check hp
                if self.player_hp <= 0:
                    self.state = "game_over"
                    # play sound
                    pg.mixer.music.stop()
                    pg.mixer.music.load("./assets/sound/mimimi.mp3")
                    pg.mixer.music.play()

                # rerender background
                self.reset(2)

                # Render grass_road_up tiles
                self.renderTiles(
                    "grass_road_up",
                    [
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
                    ],
                )

                # Render grass_road_down tiles
                self.renderTiles(
                    "grass_road_down",
                    [
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
                    ],
                )

                # Render grass_road_left tiles
                self.renderTiles(
                    "grass_road_left",
                    [
                        [1, 2],
                        [1, 3],
                        [1, 4],
                        [1, 5],
                        [1, 6],
                        [4, 0],
                        [10, 5],
                    ],
                )

                # Render grass_road_right tiles
                self.renderTiles(
                    "grass_road_right",
                    [
                        [5, 0],
                        [5, 1],
                        [2, 3],
                        [2, 4],
                        [2, 5],
                        [11, 6],
                    ],
                )

                # Render grass_road_turning_upleft tiles

                # Render grass_road_turning_upright tiles
                self.renderTiles(
                    "grass_road_turning_upright",
                    [
                        [1, 1],
                        [10, 4],
                    ],
                )

                # Render grass_road_turning_downleft tiles
                self.renderTiles(
                    "grass_road_turning_downleft",
                    [[5, 2], [11, 7]],
                )

                # Render grass_road_turning_downright tiles
                self.renderTiles("grass_road_turning_downright", [[1, 7]])

                # Render grass_road_bigturning_downleft tiles
                self.renderTiles(
                    "grass_road_bigturning_downleft",
                    [
                        [4, 1, 0],
                        [2, 2, 180],
                        [2, 6, 270],
                        [10, 6, 0],
                        [11, 5, 180],
                    ],
                )

                # Render grass_freePosition tiles

                # Render grass_mechanic tiles
                self.renderTiles(
                    "grass_mechanic",
                    [
                        [3, 0],
                    ],
                )

                # Render grass_cross tiles
                self.renderTiles(
                    "grass_cross",
                    [
                        [7, 0],
                    ],
                )

                # Render grass_circle tiles
                self.renderTiles(
                    "grass_circle",
                    [
                        [6, 0],
                    ],
                )

                # Render mountain tiles
                self.renderTiles(
                    "mountain",
                    [
                        [6, 8],
                        [6, 8],
                        [7, 8],
                        [8, 8],
                        [9, 8],
                    ],
                )

                # Render mountain_bottom tiles
                self.renderTiles(
                    "mountain_bottom",
                    [
                        [13, 6, 0],
                    ],
                )

                # Render mountain_corner_upleft tiles
                self.renderTiles(
                    "mountain_corner_upleft",
                    [
                        [12, 7, 0],
                        [5, 8, 270],
                        [10, 8, 0],
                    ],
                )

                # Render mountain_corner_downleft tiles

                # Render mountain_corner_downright tiles
                self.renderTiles(
                    "mountain_corner_downright",
                    [
                        [12, 3, 0],
                        [14, 1, 0],
                        [14, 6, 0],
                    ],
                )

                # Render mountain_bigturning_downright
                self.renderTiles(
                    "mountain_bigturning_downright",
                    [
                        [14, 2, 0],
                    ],
                )

                # Render mountain_freePosition tiles

                # Render mountain_mechanic tiles

                # Render mountain_cross tiles

                # Render mountain_circle tiles

                # Render mountain_road_down tiles
                self.renderTiles(
                    "mountain_road_down",
                    [
                        [5, 7],
                        [6, 7],
                        [7, 7],
                        [8, 7],
                        [9, 7],
                        [10, 7],
                    ],
                )

                # OLD:

                # weapons bar
                SCREEN.blit(soldier1, (6 * TILE_SIZE, 8 * TILE_SIZE))
                SCREEN.blit(soldier2, (7 * TILE_SIZE, 8 * TILE_SIZE))
                SCREEN.blit(missile_launcher, (8 * TILE_SIZE, 8 * TILE_SIZE))
                SCREEN.blit(turret, (9 * TILE_SIZE, 8 * TILE_SIZE))

                # entities
                for entity in self.entities:
                    SCREEN.blit(entity.entity, entity.rect)

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
                    SCREEN.blit(hp_text, hp_text_rect)
            elif self.state == "game_over":
                pass

            # display swedish flag
            SCREEN.blit(swedish_flag, swedish_flag_rect)

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
                SCREEN.blit(
                    TILES["grass"]["object"],
                    (
                        i * (SCREEN_WIDTH / TILED_WIDTH),
                        j * (SCREEN_HEIGHT / TILED_HEIGHT),
                    ),
                )

        if option == 1:
            # reset game variables
            self.player_hp = 1000

    def renderTiles(self, tile: str, positions: list):
        """
        Renders Tiles

        Args:
            tile (str): Key of Tile accoring to TILES constant
            positions (list): X and Y corrdinates of tiles (and angle a)
        """

        for i in positions:
            try:
                SCREEN.blit(
                    pg.transform.rotate(TILES[tile]["object"], i[2]),
                    (
                        i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                        i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                    ),
                )
            except IndexError:
                SCREEN.blit(
                    TILES[tile]["object"],
                    (
                        i[0] * (SCREEN_WIDTH / TILED_WIDTH),
                        i[1] * (SCREEN_HEIGHT / TILED_HEIGHT),
                    ),
                )


class Entity:
    """Creates entity and stores its variables."""

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
