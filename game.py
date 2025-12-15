"""The main file of our game"""

# Franco looks like a maulwurf who just went to chong colong
# Hayk is such a pookie - Gabriel (ily Hayk <3 ) (Philipp doesn't agree)
# Mark 99.-

from __future__ import annotations
import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()
pg.display.set_caption("Tower Defense - by Gabriel, Fillipe and Loris")
pg.display.set_icon(pg.image.load("./assets/custom/icon.png"))
TILED_WIDTH: int = 16
TILED_HEIGHT: int = 9
TILE_SIZE: int = 80
SCREEN_WIDTH: int = TILED_WIDTH * TILE_SIZE
SCREEN_HEIGHT: int = TILED_HEIGHT * TILE_SIZE
SCREEN: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pg.time.Clock = pg.time.Clock()
TITLE_FONT: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Blocks.ttf", 36)
SUBTITLE_FONT: pg.font.Font = pg.font.Font("./assets/fonts/Kenney Future.ttf", 18)
WEAPONS_RANGE = 4 * TILE_SIZE

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
    "free_position": {"path": "./assets/tiles/towerDefense_tile015.png"},
    "mechanic": {"path": "./assets/tiles/towerDefense_tile016.png"},
    "cross": {"path": "./assets/tiles/towerDefense_tile017.png"},
    "circle": {"path": "./assets/tiles/towerDefense_tile018.png"},
    "mountain": {"path": "./assets/tiles/towerDefense_tile034.png"},
    "mountain_road_down": {"path": "./assets/tiles/towerDefense_tile011.png"},
    "soldier1": {"path": "./assets/tiles/towerDefense_tile245.png"},
    "soldier2": {"path": "./assets/tiles/towerDefense_tile246.png"},
    "missile_launcher": {"path": "./assets/tiles/towerDefense_tile205.png"},
    "turret": {"path": "./assets/tiles/towerDefense_tile250.png"},
    "mountain_done": {"path": "./assets/photoshopped/Mountain_on_bottom_done.png"},
    "mountain_bns1": {
        "path": "./assets/photoshopped/Mountain_on_bottom_and_side_done.png"
    },
    "mountain_bns2": {
        "path": "./assets/photoshopped/Mountain_on_bottom_and_side_done_1.png"
    },
    "mountain_blc": {
        "path": "./assets/photoshopped/Mountain_on_bottom_left_corner.png"
    },
    "mountain_brc": {
        "path": "./assets/photoshopped/Mountain_on_bottom_right_corner_1.png"
    },
    "mountain_trc": {"path": "./assets/photoshopped/Mountain_on_top_right_corner.png"},
    "mountain_left": {"path": "./assets/photoshopped/Mountain_on_left.png"},
    "mountain_right": {"path": "./assets/photoshopped/Mountain_on_right.png"},
    "mountain_top": {"path": "./assets/photoshopped/Mountain_on_top.png"},
    "mountain_tlc": {"path": "./assets/photoshopped/Mountain_on_top_left_corner.png"},
    "mountain_tns2": {
        "path": "./assets/photoshopped/Mountain_on_top_and_side_done1.png"
    },
    "mountain_tns1": {
        "path": "./assets/photoshopped/Mountain_on_top_and_side_done.png"
    },
    "mountain_tc": {"path": "./assets/photoshopped/Mountain_on_top_corners.png"},
}

for key, value in TILES.items():
    tile_og = pg.image.load(value["path"])
    value["object"] = pg.transform.scale(
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
vielgut_entity_og = pg.image.load("./assets/custom/vielgut_entity.png").convert_alpha()

# load weapons
soldier1_og = pg.image.load("./assets/tiles/towerDefense_tile245.png")
soldier1 = pg.transform.scale(
    soldier1_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
soldier1_rect = soldier1.get_rect(topleft=(6 * TILE_SIZE, 8 * TILE_SIZE))

soldier2_og = pg.image.load("./assets/tiles/towerDefense_tile246.png")
soldier2 = pg.transform.scale(
    soldier2_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
soldier2_rect = soldier2.get_rect(topleft=(7 * TILE_SIZE, 8 * TILE_SIZE))

missile_launcher_og = pg.image.load("./assets/tiles/towerDefense_tile205.png")
missile_launcher = pg.transform.scale(
    missile_launcher_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
missile_launcher_rect = missile_launcher.get_rect(
    topleft=(8 * TILE_SIZE, 8 * TILE_SIZE)
)

turret_og = pg.image.load("./assets/tiles/towerDefense_tile250.png")
turret = pg.transform.scale(
    turret_og,
    (SCREEN_WIDTH / TILED_WIDTH, SCREEN_HEIGHT / TILED_HEIGHT),
)
turret_rect = turret.get_rect(topleft=(9 * TILE_SIZE, 8 * TILE_SIZE))


class Game:
    """Stores Variables and methods needed to control the game."""

    state: str = "start"

    velocity: int = 2

    player_hp: float = 1000

    player_coins: int = 100

    active_weapon_placing: list = [False, ""]

    entities: pg.sprite.Group = pg.sprite.Group()

    weapons: pg.sprite.Group = pg.sprite.Group()

    placement_free_zone: list = [[6, 8], [7, 8], [8, 8], [9, 8]]

    current_wave: int = 1

    waves: dict = {
        1: {loris_entity_og: 10},
        2: {loris_entity_og: 5, gabriel_entity_og: 5, phillippe_entity_og: 5},
        3: {
            loris_entity_og: 10,
            gabriel_entity_og: 10,
            phillippe_entity_og: 10,
        },
        4: {
            loris_entity_og: 20,
            gabriel_entity_og: 20,
            phillippe_entity_og: 20,
            vielgut_entity_og: 1,
        },
    }

    last_entity_spawn_time: int = 0

    next_wave_time: int = 0

    def __init__(self) -> None:
        running: bool = True

        pg.mixer.music.load("./assets/sound/intro.mp3")
        pg.mixer.music.play(loops=0)
        pg.mixer.music.queue("./assets/sound/afterintro.mp3")

        while running:
            for event in pg.event.get():
                if event.type == pg.constants.QUIT:
                    running = False
                elif event.type == pg.constants.KEYDOWN:
                    if event.key == pg.constants.K_SPACE and self.state == "start":
                        self.state = "game"
                        self.reset(1)
                        pg.mixer.music.stop()
                        pg.mixer.music.load("./assets/sound/coconut_mall.mp3")
                        pg.mixer.music.play(loops=-1)
                elif event.type == pg.constants.MOUSEBUTTONDOWN:
                    x, y = convert_coordinates(event.pos)
                    if soldier1_rect.collidepoint(event.pos):
                        self.active_weapon_placing = [True, "soldier1"]
                    elif soldier2_rect.collidepoint(event.pos):
                        self.active_weapon_placing = [True, "soldier2"]
                    elif missile_launcher_rect.collidepoint(event.pos):
                        self.active_weapon_placing = [True, "missile_launcher"]
                    elif turret_rect.collidepoint(event.pos):
                        self.active_weapon_placing = [True, "turret"]
                    elif (
                        self.active_weapon_placing[0] is True
                        and [x, y] not in self.placement_free_zone
                    ):
                        if (
                            (
                                self.active_weapon_placing[1] == "soldier1"
                                and self.player_coins >= 50
                            )
                            or (
                                self.active_weapon_placing[1] == "soldier2"
                                and self.player_coins >= 100
                            )
                            or (
                                self.active_weapon_placing[1] == "missile_launcher"
                                and self.player_coins >= 250
                            )
                            or (
                                self.active_weapon_placing[1] == "turret"
                                and self.player_coins >= 500
                            )
                        ):
                            self.weapons.add(
                                Weapon(
                                    self.active_weapon_placing[1],
                                    [x, y],
                                    self,
                                )
                            )
                            self.active_weapon_placing = [False, ""]
                            self.placement_free_zone.append([x, y])

            # start SCREEN if:
            if self.state == "start":
                self.reset(2)
                # title:
                welcome_title = TITLE_FONT.render(
                    "Welcome to Tower Defense!", True, (187, 127, 68)
                )
                welcome_title_rect = welcome_title.get_rect(center=(640, 340))
                SCREEN.blit(welcome_title, welcome_title_rect)
                # subtitle:
                welcome_subtitle = SUBTITLE_FONT.render(
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
                self.render_tiles(
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
                self.render_tiles(
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
                self.render_tiles(
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
                self.render_tiles(
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
                self.render_tiles(
                    "grass_road_turning_upright",
                    [
                        [1, 1],
                        [10, 4],
                    ],
                )

                # Render grass_road_turning_downleft tiles
                self.render_tiles(
                    "grass_road_turning_downleft",
                    [[5, 2], [11, 7]],
                )

                # Render grass_road_turning_downright tiles
                self.render_tiles("grass_road_turning_downright", [[1, 7]])

                # Render grass_road_bigturning_downleft tiles
                self.render_tiles(
                    "grass_road_bigturning_downleft",
                    [
                        [4, 1, 0],
                        [2, 2, 180],
                        [2, 6, 270],
                        [10, 6, 0],
                        [11, 5, 180],
                    ],
                )

                # Render free_position tiles

                # Render mechanic tiles

                # Render cross tiles
                self.render_tiles(
                    "cross",
                    [
                        [0, 4],
                    ],
                )

                # Render circle tiles

                # Render mountain tiles
                self.render_tiles(
                    "mountain",
                    [
                        [6, 8],
                        [6, 8],
                        [7, 8],
                        [8, 8],
                        [9, 8],
                        [7, 3],
                        [7, 4],
                        [6, 4],
                        [5, 4],
                        [8, 3],
                        [7, 2],
                        [7, 1],
                        [8, 2],
                        [8, 1],
                        [9, 3],
                        [9, 2],
                        [9, 1],
                        [9, 0],
                        [8, 0],
                        [10, 0],
                        [15, 8],
                        [15, 7],
                        [14, 8],
                        [13, 8],
                        [14, 7],
                        [15, 0],
                        [14, 0],
                        [15, 1],
                        [15, 2],
                        [14, 1],
                    ],
                )

                # Render mountain_road_down tiles
                self.render_tiles(
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
                self.render_tiles(
                    "mountain_done",
                    [
                        [4, 3],
                        [5, 3],
                        [15, 6],
                        [14, 6],
                    ],
                )
                self.render_tiles(
                    "mountain_bns1",
                    [
                        [7, 0],
                        [6, 3],
                        [12, 8],
                        [13, 7],
                    ],
                )
                self.render_tiles(
                    "mountain_bns2",
                    [
                        [0, 8],
                    ],
                )
                self.render_tiles(
                    "mountain_trc",
                    [
                        [4, 5],
                        [14, 3],
                        [13, 2],
                    ],
                )
                self.render_tiles(
                    "mountain_brc",
                    [
                        [4, 3],
                        [6, 0],
                        [12, 7],
                        [13, 6],
                        [11, 8],
                    ],
                )
                self.render_tiles(
                    "mountain_blc",
                    [
                        [1, 8],
                        [0, 7],
                    ],
                )
                self.render_tiles(
                    "mountain_left",
                    [
                        [10, 2],
                        [10, 1],
                    ],
                )
                self.render_tiles(
                    "mountain_right",
                    [
                        [4, 4],
                        [6, 2],
                        [6, 1],
                        [13, 1],
                    ],
                )
                self.render_tiles(
                    "mountain_top",
                    [
                        [5, 5],
                        [6, 5],
                        [7, 5],
                        [15, 3],
                    ],
                )
                self.render_tiles(
                    "mountain_tns1",
                    [
                        [8, 4],
                        [9, 3],
                        [10, 1],
                        [11, 0],
                        [10, 8],
                    ],
                )
                self.render_tiles(
                    "mountain_tns2",
                    [
                        [5, 8],
                        [14, 2],
                        [13, 0],
                    ],
                )
                self.render_tiles(
                    "mountain_tlc",
                    [
                        [8, 5],
                        [9, 4],
                        [10, 3],
                        [11, 1],
                    ],
                )
                self.render_tiles(
                    "mountain_tc",
                    [
                        [12, 0],
                    ],
                )

                # weapons bar
                SCREEN.blit(soldier1, soldier1_rect)
                SCREEN.blit(soldier2, soldier2_rect)
                SCREEN.blit(missile_launcher, missile_launcher_rect)
                SCREEN.blit(turret, turret_rect)

                # wave management / entity spawning
                now = pg.time.get_ticks()
                if self.next_wave_time <= now and self.next_wave_time != 0:
                    self.current_wave += 1
                    self.next_wave_time = 0
                    self.velocity += 1

                for number, objects in self.waves.items():
                    total = 0
                    for _, amount in objects.items():
                        total += amount
                    if (
                        total == 0
                        and self.current_wave == number
                        and self.next_wave_time == 0
                    ):
                        self.next_wave_time = now + 50000

                for entity_og_image, amount in self.waves[self.current_wave].items():
                    if amount > 0 and now - self.last_entity_spawn_time >= (
                        12000 / (self.velocity * 2)
                    ):
                        self.entities.add(Entity(entity_og_image))
                        self.last_entity_spawn_time = now
                        self.waves[self.current_wave][entity_og_image] -= 1
                        if entity_og_image == vielgut_entity_og:
                            pg.mixer.music.load("./assets/sound/ima_boss.mp3")
                            pg.mixer.music.play(loops=0)
                            self.velocity = 2

                if self.current_wave == 4 * len(self.entities.sprites()) == 0:
                    self.state = "win"

                # entities
                if self.entities:
                    self.entities.update(self.entities, self)
                    self.weapons.update(self.entities)

                self.entities.draw(SCREEN)
                self.weapons.draw(SCREEN)

                # Active Weapon Placement
                if self.active_weapon_placing[0] is True:
                    x, y = pg.mouse.get_pos()
                    tile_x, tile_y = convert_coordinates([x, y])
                    if [tile_x, tile_y] not in self.placement_free_zone:
                        self.render_tiles("free_position", [[tile_x, tile_y]])
                        self.render_tiles(
                            self.active_weapon_placing[1], [[tile_x, tile_y]]
                        )
                        circle_x, circle_y = convert_coordinates([tile_x, tile_y])
                        circle_x += TILE_SIZE / 2
                        circle_y += TILE_SIZE / 2
                        pg.draw.circle(
                            SCREEN,
                            (255, 255, 255),
                            (circle_x, circle_y),
                            WEAPONS_RANGE,
                            width=1,
                        )
                    elif tile_x == 0 and tile_y == 4:
                        self.active_weapon_placing = [False, ""]

                # display wave
                current_wave_text = TITLE_FONT.render(
                    f"Wave {self.current_wave}", True, (255, 255, 255)
                )
                current_wave_text_rect = current_wave_text.get_rect(topleft=(10, 0))
                SCREEN.blit(current_wave_text, current_wave_text_rect)

                # display HP Text
                hp_text = TITLE_FONT.render(
                    f"{self.player_hp} HP", True, (255, 255, 255)
                )
                hp_text_rect = hp_text.get_rect(topright=(SCREEN_WIDTH - 10, 0))
                SCREEN.blit(hp_text, hp_text_rect)

                # display Coins Text
                coins_text = TITLE_FONT.render(
                    f"{self.player_coins} Coins", True, (255, 255, 255)
                )
                coins_text_rect = coins_text.get_rect(topright=(SCREEN_WIDTH - 10, 50))
                SCREEN.blit(coins_text, coins_text_rect)

            elif self.state == "game_over":
                self.reset(2)
                # title:
                gameover_title = TITLE_FONT.render("Game Over!", True, (187, 127, 68))
                gameover_title_rect = gameover_title.get_rect(center=(640, 140))
                SCREEN.blit(gameover_title, gameover_title_rect)
                # subtitle:
                gameover_subtitle = SUBTITLE_FONT.render(
                    "You Lost", True, (187, 127, 68)
                )
                gameover_subtitle_rect = gameover_subtitle.get_rect(center=(640, 180))
                SCREEN.blit(gameover_subtitle, gameover_subtitle_rect)
                # picture
                gameover_screen = pg.image.load("./assets/custom/Game_over.bg.png")
                gameover_screen_rect = gameover_screen.get_rect(center=(640, 450))
                SCREEN.blit(gameover_screen, gameover_screen_rect)
                # tip
                gameover_tip = SUBTITLE_FONT.render("Tip:", True, (187, 127, 68))
                gameover_tip_rect = gameover_tip.get_rect(topleft=(90, 300))
                SCREEN.blit(gameover_tip, gameover_tip_rect)

                gameover_tipw = SUBTITLE_FONT.render("Get better", True, (187, 127, 68))
                gameover_tipw_rect = gameover_tipw.get_rect(topleft=(90, 320))
                SCREEN.blit(gameover_tipw, gameover_tipw_rect)
            elif self.state == "win":
                self.reset(2)
                # add music
                pg.mixer.music.stop()
                pg.mixer.music.load("./assets/sound/win_music.mp3")
                pg.mixer.music.play(loops=-1)
                # add picture
                happy_win = pg.image.load("./assets/custom/happy_win.png")
                happy_win_rect = happy_win.get_rect(center=(600, 540))
                SCREEN.blit(happy_win, happy_win_rect)
                # add 3 mice on the left
                mouse1 = pg.image.load("./assets/custom/mouse_right.png")
                mouse1_rect = mouse1.get_rect(center=(340, 240))
                SCREEN.blit(mouse1, mouse1_rect)
                mouse2 = pg.image.load("./assets/custom/mouse_right.png")
                mouse2_rect = mouse2.get_rect(center=(290, 390))
                SCREEN.blit(mouse2, mouse2_rect)
                mouse3 = pg.image.load("./assets/custom/mouse_right.png")
                mouse3_rect = mouse3.get_rect(center=(240, 540))
                SCREEN.blit(mouse3, mouse3_rect)
                # add 3 mice on the right
                mouse4 = pg.image.load("./assets/custom/mouse_left.png")
                mouse4_rect = mouse4.get_rect(center=(940, 240))
                SCREEN.blit(mouse4, mouse4_rect)
                mouse5 = pg.image.load("./assets/custom/mouse_left.png")
                mouse5_rect = mouse5.get_rect(center=(990, 390))
                SCREEN.blit(mouse5, mouse5_rect)
                mouse6 = pg.image.load("./assets/custom/mouse_left.png")
                mouse6_rect = mouse6.get_rect(center=(1040, 540))
                SCREEN.blit(mouse6, mouse6_rect)

            # display swedish flag
            SCREEN.blit(swedish_flag, swedish_flag_rect)

            pg.display.flip()

            clock.tick(24)  # limits FPS to 24

        pg.quit()

    def reset(self, option: int):
        """
        Method to reset background and game variables

        Args:
            option (int): Option 1 resets background and variables, while option 2 only resets background.
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
            self.player_coins = 100

    def render_tiles(self, tile: str, positions: list):
        """
        Rotates Tile if needed and puts it onto screen.

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
            if (
                tile is not "grass"
                and tile is not "mountain"
                and tile is not "free_position"
                and tile is not "soldier1"
                and tile is not "soldier2"
                and tile is not "missile_launcher"
                and tile is not "turret"
                and [i[0], i[1]] not in self.placement_free_zone
            ):
                self.placement_free_zone.append([i[0], i[1]])


class Entity(pg.sprite.Sprite):
    """Creates entity and stores its variables."""

    og_image: pg.Surface

    entity_hp: int

    def __init__(self, image: pg.Surface):
        """
        Creates Entity Object and sets its variables.

        Args:
            image (pg.Surface): og_image of entity
        """
        super().__init__()
        self.og_image = image
        self.image = pg.transform.rotate(
            pg.transform.scale(self.og_image, (TILE_SIZE, TILE_SIZE)), 90
        )
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = round(4.5 * TILE_SIZE)
        if self.og_image == loris_entity_og:
            self.entity_hp = 100
        elif self.og_image == gabriel_entity_og or self.og_image == gabriel_entity2_og:
            self.entity_hp = 200
        elif self.og_image == phillippe_entity_og:
            self.entity_hp = 300
        elif self.og_image == vielgut_entity_og:
            self.entity_hp = 1500

        self.path: list[list[float, float]] = [
            [10.5, 4.5],
            [10.5, 6.5],
            [1.5, 6.5],
            [1.5, 1.5],
            [4.5, 1.5],
            [4.5, -1],
        ]

    def rotate(self, angle: int):
        """
        Rotates entity on screen by angle.

        Args:
            angle (int): angle in degrees (anti-clockwise)
        """
        self.image = pg.transform.rotate(
            pg.transform.scale(self.og_image, (TILE_SIZE, TILE_SIZE)), angle
        )

    def update(self, entities: pg.sprite.Group, game: Game):
        """
        Checks if entity is dead.
        If so, it removes itself and gives player coins.

        Args:
            entities (pg.sprite.Group): entities sprite group
            game (Game): game object
        """
        if len(self.path) == 0:
            game.player_hp -= self.entity_hp
            self.entity_hp = 0
        else:
            target_x: int = self.path[0][0] * TILE_SIZE
            target_y: int = self.path[0][1] * TILE_SIZE

            delta_x: int = target_x - self.rect.x
            delta_y: int = target_y - self.rect.y

            if delta_x == 0 and delta_y == 0:
                self.path.pop(0)
            elif abs(delta_x) <= game.velocity and abs(delta_y) <= game.velocity:
                self.rect.x = target_x
                self.rect.y = target_y
            else:
                step_x: int = (
                    game.velocity
                    if delta_x > 0
                    else (-game.velocity if delta_x < 0 else 0)
                )
                step_y: int = (
                    game.velocity
                    if delta_y > 0
                    else (-game.velocity if delta_y < 0 else 0)
                )

                if abs(step_x) > abs(delta_x):
                    step_x = delta_x
                if abs(step_y) > abs(delta_y):
                    step_y = delta_y

                if step_x < 0:
                    angle = 90
                elif step_x > 0:
                    angle = -90

                if step_y < 0:
                    angle = 0
                elif step_y > 0:
                    angle = 180

                self.rect.x += step_x
                self.rect.y += step_y

                self.rotate(angle)

        if self.entity_hp <= 0:
            entities.remove(self)
            if len(self.path) > 0:
                if self.og_image == loris_entity_og:
                    game.player_coins += 10
                elif self.og_image == gabriel_entity_og:
                    game.player_coins += 30
                elif self.og_image == gabriel_entity2_og:
                    game.player_coins += 50
                elif self.og_image == phillippe_entity_og:
                    game.player_coins += 80
                elif self.og_image == vielgut_entity_og:
                    game.player_coins += 150


class Weapon(pg.sprite.Sprite):
    """Creates weapon and stores its variables."""

    og_image: pg.Surface

    weapon: str

    damage: int

    last_shot_time: int = 0

    fire_rate: int

    weapon_pos: pg.Vector2

    cost: int

    def __init__(self, weapon: str, position: list, game: Game):
        """
        Creates Weapon Object and subtracts coins from player.

        Args:
            weapon (str): Type of Weapon
            position (list): Postion of Weapon in Screen Pixels
            game (Game): game Object
        """
        super().__init__()
        self.weapon = weapon
        if weapon == "soldier1":
            self.og_image = soldier1_og
            self.cost = 50
            self.damage = 25
            self.fire_rate = 5000
        elif weapon == "soldier2":
            self.og_image = soldier2_og
            self.cost = 100
            self.damage = 50
            self.fire_rate = 2500
        elif weapon == "missile_launcher":
            self.og_image = missile_launcher_og
            self.cost = 250
            self.damage = 125
            self.fire_rate = 2500
        elif weapon == "turret":
            self.og_image = turret_og
            self.cost = 500
            self.damage = 150
            self.fire_rate = 1000
        self.image = pg.transform.scale(self.og_image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = convert_coordinates(position)
        self.weapon_pos = pg.Vector2(self.rect.center)
        game.player_coins -= self.cost

    def update(self, entities: pg.sprite.Group):
        """
        Checks if Weapon is ready to shoot again.
        Then damages first entity that is within its range.

        Args:
            entities (pg.spriteGroup): entities Sprite group
        """
        now = pg.time.get_ticks()
        if now - self.last_shot_time >= self.fire_rate and len(entities.sprites()) > 0:
            for entity in entities.sprites():
                target_pos = pg.Vector2(entity.rect.center)
                distance = self.weapon_pos.distance_to(target_pos)
                if distance <= WEAPONS_RANGE:
                    entity.entity_hp -= self.damage
                    self.last_shot_time = now
                else:
                    break


def convert_coordinates(coordinates: list):
    """
    Converts coordinates between screen-pixels and tiled system.
    Returns converted x and y value.

    Args:
        coordinates (list): X, Y position (screen pixels or tiled)
    """
    x, y = coordinates
    if x > TILED_WIDTH and y > TILED_WIDTH:
        tile_x: int
        tile_y: int
        for i in range(0, (TILED_WIDTH + 1)):
            if i * TILE_SIZE < x:
                tile_x = i
        for i in range(0, (TILED_HEIGHT + 1)):
            if i * TILE_SIZE < y:
                tile_y = i
        return (tile_x, tile_y)
    else:
        screen_x: int = x * (SCREEN_WIDTH / TILED_WIDTH)
        screen_y: int = y * (SCREEN_HEIGHT / TILED_HEIGHT)
        return (screen_x, screen_y)


game = Game()
