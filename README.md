# dungeons-and-pythons

![image](https://user-images.githubusercontent.com/41023883/156897896-12bd6668-0b16-4423-994e-dfb31b00d855.png)

@ = player

\* = monster

Dungeons and Pythons is a silly text-based rpg based loosely on dungeon-crawlers like Diablo 2, text-based games like Zork, and tabletop rpg's like D&D. The goal isn't to make an awesome game (though hopefully that happens); the goal is to demonstrate knowledge & proficiency with different elements of the Python programming language.

## How to play:

1. Clone the repository
2. If you want to do single fights or extended tournament fights, run /fight.py
3. If you want to see & interact with the dungeon runner, run /separates/playerandroom3.py

## Important modules & their functions

* fight.py - original module containing battle code
* subclasses.py - creates functional dictionaries containing places & rooms
* /separates/ - folder containing simplified modules for elegance
* /separates/rooms2.py - test module where room concept was first proven
* /separates/playerandroom3.py - fully functional dungeon-running module. Dynamically generates dungeon rooms & lets player run to end of each; contains monsters

# Wishlist:
(crossed out items have been achieved)
* character classes (barbarian, wizard, ranger, cyborg)
  * ~~character saves & load saved characters~~
  * add equipable items e.g. "big sword", "scavenged shield/armor", "BFG", that boost attack or defense, or are single-use instant kills etc.
  * add pets that provide similar boosts e.g. "goldendoodle" boosts speed, "narwahl" boosts attack
* items (weapons, potions, gold, tools)
  * adds depth to each game mode
* text-based navigation (typing 'go north', 'open door', or 'search chest')
  * add fighting to dungeon-running module
  * then add dungeon-running to standalone "select game mode" module
* dynamically generated dungeons (start at point x, navigate to the end)
  * ~~self-generating instances~~
  * add fighting to dungeon-running module
  * add item_spawner in dungeon-running module to spawn equipable items, searchable items, & lore items
  * ~~easy~~, medium, ~~hard~~, insane modes
  * add stores between dungeons to spend gold in
  * add health potions to refill, strong weapons, pets to boost stats
* a story/campaign
  * demonstrates ability to write proficiently & craft an easily digestible narrative


# Most recent updates:

## 2/16/22

* added a "generate_monster" method to the "generate_rooms" method - now when rooms are generated, a dynamic number of monsters are generated & saved with each room as "room.monster_list".
* added a "place_monster" method that iterates over map grid & places monsters down at specified coordinates
* added a "monster_move" method that runs after "player_move" in the dungeon runner - based on easy or hard mode, monsters will either move wander/pursue player, or pursue the player

## 2/15/22
* successfully completed dungeon-runner module; generates rooms, lets player navigate through dungeons, & move on to the next room

## 2/9/22
* added a "tournament" mode; takes input from player to determine how many rounds will be fought
