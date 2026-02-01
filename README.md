# Informatik Project of Gabirel, Filipe and Loris

## Goal
Stop enemies from reaching the end of the path.  
You start with **1000 HP** and **100 coins**. If enemies reach the end, their remaining HP is subtracted from your HP. If your HP hits **0**, you lose.

You win after clearing **Wave 8** (includes the boss **Vielgut**).

---

## Starting the Game
1. Launch the game.
2. On the start screen, press **SPACE** to begin.

---

## What You See In-Game
- **Wave counter** (top-left): `Wave X`
- **HP** (top-right): your remaining base health
- **Coins** (top-right, below HP): your money for buying towers
- **Shop bar** (bottom row of tiles): click icons to select what to place

---

## Enemies & Path
- Enemies spawn on the **right side** and follow the road to the exit.
- Killing enemies gives coins:
  - **Loris**: +6 coins  
  - **Gabriel**: +10 coins  
  - **Phillip**: +16 coins  
  - **Vielgut (Boss)**: +120 coins

Tip: If you see enemies turning semi-transparent, they are below **50% HP**.

---

## Placing Towers
1. **Click a tower icon** in the bottom shop bar:
   - Soldier 1 (**$50**)
   - Soldier 2 (**$100**)
   - Missile Launcher (**$250**)
   - Turret (**$500**)
   - Money Tree (**starts at $50**, doubles each time you buy one)
2. Move your mouse onto the map:
   - A **preview** appears where you can place.
   - For weapons (not Money Tree), a **white circle** shows the attack range.
3. **Click to place** on a valid tile (not on the shop bar tiles nor on other preoccupied tiles).

Notes:
- Towers automatically target enemies **within range**.
- Weapons rotate to face their target.
- You must have enough coins, otherwise placement won’t happen.

---

## Deleting / Cancelling
There is a **cross tile** on the left side that toggles delete mode.

- If you are not placing anything, it shows **“Delete”**.
- If you are placing or deleting, it shows **“Cancel”**.

### Delete a tower / money tree
1. Click the **cross tile** to enable delete mode.
2. Click a placed **tower** or **money tree** to remove it.
3. You get **50% of its cost back**.

### Cancel placement
- Click the **cross tile** while you’re holding a tower preview to cancel.

---

## Money Trees
- Money Trees do not attack.
- Every **5 seconds**, each Money Tree gives **+5 coins**.
- Cost starts at **$50** and **doubles** after every purchase.

---

## Waves & Difficulty
- The game runs through **8 waves**.
- Enemy spawn rate scales with the game’s internal speed (velocity increases over time).
- Special behavior:
  - **Wave 6 enemies** have extra HP.
  - **Wave 8** includes the boss **Vielgut** and triggers boss music.

---

## Winning & Losing
- **Lose**: your HP reaches 0 → Game Over screen
- **Win**: Wave 8 cleared and no enemies remain → Win screen

---

## Strategy Tips
- Start with **cheap Soldiers** to build early coin income from kills.
- Add **Money Trees** early if you can safely survive the next waves.
- Missile Launchers are strong but slow — pair them with faster towers.
- Keep towers near corners/long road segments to maximize time in range.

---

## Credits:
* Pygame Basic Setup from [Pygame Docs](https://www.pygame.org/docs/)
* Game Tiles and Fonts from [kenney.nl](https://kenney.nl)
* ChatGPT for this ReadMe
