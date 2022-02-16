# dungeons-and-pythons

Dungeons and Pythons is a silly text-based rpg based loosely on dungeon-crawlers like Diablo 2, text-based games like Zork, and tabletop rpg's like D&D.

The goal isn't to make an awesome game (though hopefully that happens); the goal is to demonstrate knowledge & proficiency with different elements of the Python programming language.

* fight.py - original module containing battle code
* /separates/ - folder containing simplified modules for elegance
* subclasses.py - creates functional dictionaries containing places & rooms
* rooms2.py - test module where room concept was first proven
* playerandroom3.py - fully functional dungeon-running module. Dynamically generates dungeon rooms & lets player run to end of each; contains monsters

Wishlist (crossed out items have been achieved):
* character classes (barbarian, wizard, ranger, cyborg)
  * improves replayability
* items (weapons, potions, gold, tools)
  * adds depth to each game mode
* text-based navigation (typing 'go north', 'open door', or 'search chest')
  * game logic, demonstrates ability to write & understand complex code
  * add fighting to dungeon-running module
  * then add dungeon-running to standalone "select game mode" module
* ~~dynamically generated dungeons (start at point x, navigate to the end)~~
  * ~~self-generating instances~~
  * ~~easy~~, medium, hard, insane modes
  * stores between dungeons to spend gold in
   * health potions to refill, strong weapons, pets to boost stats
* a story/campaign
  * demonstrates ability to write proficiently & craft an easily digestible narrative


Most recent update:
2/16/22
* added a "generate_monster" method to the "generate_rooms" method - now when rooms are generated, a dynamic number of monsters are generated & saved with each room as "room.monster_list".
* added a "place_monster" method that iterates over map grid & places monsters down at specified coordinates
* added a "monster_move" method that runs after "player_move" in the dungeon runner - based on easy or hard mode, monsters will either move wander/pursue player, or pursue the player
