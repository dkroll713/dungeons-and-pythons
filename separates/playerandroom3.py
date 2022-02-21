import random
from classes import Fighter
from classes import Opponent
# from functions import fight
import time

a = Fighter("David",10,10,100,10,False,True)
a.posX = 1
a.posY = 1
# now have a fighter with positon (posX,posY)

difficulty = input("Type easy or hard: ")

map_width = 60
map_height = 60
max_room_width = 25
min_room_width = 5
max_room_height = 25
min_room_height = 5
min_rooms = 5
max_rooms = 10
total_rooms = random.choice(range(min_rooms,max_rooms))
map = {}
rooms = {}
monsters = {}
min_monsters = 1
max_monsters = 4
min_room_monsters = 0
max_room_monsters = 6
total_room_monsters = random.randrange(min_room_monsters,max_room_monsters)
total_monsters = random.randrange(min_monsters,max_monsters)
monster_names = ['Bulbous Goblin']
monster_attack = [1,2,3,4,5]
monster_defense = [2,3,4]
hit_point_values = [3,4,5]
ads_values = [1,2,3,4,5,6,7,8,9,10]
avoid_values = [.1,.2,.3,.4,.5,.6]
block_values = [.6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
# room creation stats & dicts

class Monster:
    def __init__(self):
        self.monster_id = len(monsters)+1
        self.monster_name = monster_names[0]
        self.monster_attack = random.choice(monster_attack)
        self.monster_defense = random.choice(monster_defense)
        self.monster_hit_points = (self.monster_defense*random.choice(monster_defense))
        self.monster_speed = random.choice(monster_attack)
        self.monster_status = 'alive'
        monsters[self.monster_id] = {
            "monster_id" : self.monster_id,
            "monster_name" : self.monster_name,
            "monster_attack" : self.monster_attack,
            "monster_defense" : self.monster_defense,
            "monster_hit_points" : self.monster_hit_points,
            "monster_speed" : self.monster_speed,
            "monster_status" : self.monster_status
        }

b = Monster()

class Room():
    def __init__(self):
        print("Creating room")
        self.room_id = len(rooms)+1
        self.width = random.choice(range(min_room_width,max_room_width))
        self.height = random.choice(range(min_room_height,max_room_height))
        self.x = random.choice(range(0,map_width-self.width))
        self.y = random.choice(range(0,map_height-self.height))
        self.coords = (self.x,self.y)
        self.room_corners = {}
        self.top_left_corner = self.coords
        self.room_corners['top_left_corner'] = self.top_left_corner
        self.top_right_corner = (self.x+self.width,self.y)
        self.room_corners['top_right_corner'] = self.top_right_corner
        self.bottom_left_corner = (self.x,self.y+self.height)
        self.room_corners['bottom_left_corner'] = self.bottom_left_corner
        self.bottom_right_corner = (self.x+self.width,self.y+self.height)
        self.room_corners['bottom right corner'] = self.bottom_right_corner
        self.room_map = {}
        for sy in range(self.height):
            for sx in range(self.width):
                if sy == 0:
                    self.room_map[sx,sy]= ' # '
                elif sx == 0:
                    self.room_map[sx,sy] = ' # '
                elif sy == self.height-1:
                    self.room_map[sx,sy] = ' # '
                elif sx == self.width-1:
                    self.room_map[sx,sy] = ' # '
                else:
                    self.room_map[sx,sy] = "   "
        self.room_size = self.width*self.height
        self.door = []
        self.monster_list = []
        rooms[self.room_id] = {
            "room_id" : self.room_id,
            "room_x" : self.x,
            "room_y" : self.y,
            "room_height" : self.height,
            "room_width" : self.width,
            "room_size" : self.room_size,
            "room_corners" : self.room_corners,
            "room_map" : self.room_map,
            "door" : self.door,
            "coords" : (self.y,self.x),
            "monster_list" : self.monster_list
            }

    def print_room(self):
        print("Room created at",self.coords,"with",self.room_size,"size.",\
        self.height,"cells high and",self.width,"cells wide.")

    def add_to_map(self):
        # print("Mapping room")
        for y in range(self.y,self.y+self.height):
            for x in range(self.x,self.x+self.width):
                coords = (x,y)
                map[coords] = "#"
                # print(coords)

    def print_room_map(self):
        printed_room_map = list(self.room_map.values())
        chunks = [printed_room_map[i:i+self.width] for i in range(0, len(printed_room_map), self.width)]
        for chunk in chunks:
            print(''.join(chunk))

    def add_door(self):
        randomWallSpot = list(random.choice(list(rooms[self.room_id]['room_map'].items())))
        spot_coords = randomWallSpot[0]
        while randomWallSpot[0] == (0,0) or randomWallSpot[0] == (self.width-1,0)\
        or randomWallSpot[0] == (0,self.height-1) or randomWallSpot[0] == (self.width-1,self.height-1)\
        or randomWallSpot[1] != " # ":
            # print(randomWallSpot)
            randomWallSpot = list(random.choice(list(rooms[self.room_id]['room_map'].items())))
            spot_coords = randomWallSpot[0]
        else:
            # print("adding door at",spot_coords)
            self.room_map[spot_coords] = " _ "
            self.door = spot_coords

def multiply(x,y):
    return x*y

r = 1
# r declared here so that it can be used by room generators
def generate_rooms():
    for r in range(total_rooms):
        room = Room()
        room.print_room()
        room.add_to_map()
        room.add_door()
        room.print_room_map()
        generate_monsters(room)
        rooms[room.room_id] = {
            "room_id" : room.room_id,
            "room_x" : room.x,
            "room_y" : room.y,
            "room_height" : room.height,
            "room_width" : room.width,
            "room_size" : room.room_size,
            "room_corners" : room.room_corners,
            "room_map" : room.room_map,
            "door" : room.door,
            "coords" : (room.y,room.x),
            "monster_list" : room.monster_list
            }
    place_player()
    place_monster()
    print("\n\nTotal rooms:",total_rooms)
    print("\n\nTotal monsters:",len(monsters))



def generate_monsters(room):
    for r in range(total_monsters):
        monster = Monster()
        monster.posX = random.randrange(1,room.width-1)
        monster.posY = random.randrange(1,room.height-1)
        monsters[monster.monster_id]['monster_posX'] = monster.posX
        monsters[monster.monster_id]['monster_posY'] = monster.posY
        room.monster_list.append({
            "monster_id" : monster.monster_id,
            "monster_name" : monster.monster_name,
            "monster_attack" : monster.monster_attack,
            "monster_defense" : monster.monster_defense,
            "monster_hit_points" : monster.monster_hit_points,
            "monster_speed" : monster.monster_speed,
            "monster_status" : monster.monster_status,
            "monster_posX" : monster.posX,
            "monster_posY" : monster.posY
            })

def print_room_map(room,r):
    printed_room_map = list(rooms[r]['room_map'].values())
    chunks = [printed_room_map[i:i+rooms[r]['room_width']] for i in range(0, len(printed_room_map), rooms[r]['room_width'])]
    for chunk in chunks:
        print(''.join(chunk))

def place_player():
    for r in rooms:
        print("\nAdding player position at",(a.posX,a.posY))
        current_room = rooms[r]
        current_room_width = current_room['room_width']
        current_room_height = current_room['room_height']
        current_room_map = current_room['room_map']
        a.posX = random.randrange(1,current_room_width-1)
        a.posY = random.randrange(1,current_room_height-1)
        # print(current_room)
        # print((a.posX,a.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[a.posX,a.posY] = " @ "
                rooms[r]['room_map'] = current_room_map
                rooms[r]['posX'] = a.posX
                rooms[r]['posY'] = a.posY
        # print(current_room)
        print_room_map(current_room,r)

def place_monster():
    for r in rooms:
        print("\nAdding monsters to dungeon",r," . . .")
        current_room = rooms[r]
        current_room_width = current_room['room_width']
        current_room_height = current_room['room_height']
        current_room_map = current_room['room_map']
        current_monster_list = current_room['monster_list']
        mo = 0
        for monster in current_monster_list:
            current_monster = current_room['monster_list'][mo]
            current_mon_posX = current_monster['monster_posX']
            current_mon_posY = current_monster['monster_posY']
            # print(current_monster)
            mo = mo+1

            for sy in range(current_room_height):
                for sx in range(current_room_width):
                    if not current_room_map[current_mon_posX,current_mon_posY] == " @ ":
                        current_room_map[current_mon_posX,current_mon_posY] = " * "
                    else:
                        current_mon_posX = random.randrange(1,current_room_width-1)
                        current_mon_posY = random.randrange(1,current_room_height-1)
        print_room_map(current_room_map,r)

def printOpponent():
    print("\n")
    print("Your opponent: "+str(b.name))
    time.sleep(.5)
    print("Attack stat: "+str(b.attack))
    time.sleep(.5)
    print("Defense stat: "+str(b.defense))
    time.sleep(.5)
    print("Speed stat: "+str(b.speed))
    time.sleep(.5)
    print("Hit points: "+str(b.hit_points))
    time.sleep(.5)
    if b.pet is True:
        print("Has a pet")
    else:
        pass

def printSelf():
    print(vars(a))
    print("\n")
    print("Your fighter: "+str(a.name))
    time.sleep(.5)
    print("Attack stat: "+str(a.attack))
    time.sleep(.5)
    print("Defense stat: "+str(a.defense))
    time.sleep(.5)
    print("Speed stat: "+str(a.speed))
    time.sleep(.5)
    print("Hit points: "+str(a.hit_points))
    time.sleep(.5)
    if a.pet is True:
        print("Has a pet")
    else:
        pass

def move_up(current_room,r):

    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    a.posX = rooms[r]['posX']
    a.posY = rooms[r]['posY']
    if current_room_map[a.posX,a.posY-1] == " # ":
        print("You can't move that way")
    else:
        print("move up")
        a.posY = a.posY-1
        print((a.posX,a.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[a.posX,a.posY] = " @ "
                current_room_map[a.posX,a.posY+1] = "   "
                current_room['posX'] = a.posX
                current_room['posY'] = a.posY
                rooms[r]['room_map'] = current_room_map
        print(r)

def move_down(current_room,r):

    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    a.posX = rooms[r]['posX']
    a.posY = rooms[r]['posY']
    if current_room_map[a.posX,a.posY+1] == " # ":
        print("You can't move that way")
    else:
        print("move down")
        a.posY = a.posY+1
        print((a.posX,a.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[a.posX,a.posY] = " @ "
                current_room_map[a.posX,a.posY-1] = "   "
                current_room['posX'] = a.posX
                current_room['posY'] = a.posY
                rooms[r]['room_map'] = current_room_map
        print(r)

def move_left(current_room,r):

    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    a.posX = rooms[r]['posX']
    a.posY = rooms[r]['posY']
    if current_room_map[a.posX-1,a.posY] == " # ":
        print("You can't move that way - left")
    else:
        print("move left")
        a.posX = a.posX-1
        print((a.posX,a.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[a.posX,a.posY] = " @ "
                current_room_map[a.posX+1,a.posY] = "   "
                current_room['posX'] = a.posX
                current_room['posY'] = a.posY
                rooms[r]['room_map'] = current_room_map
        print(r)

def move_right(current_room,r):

    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    a.posX = rooms[r]['posX']
    a.posY = rooms[r]['posY']
    if current_room_map[a.posX+1,a.posY] == " # ":
        print("You can't move that way - right")
    else:
        print("move right")
        a.posX = a.posX+1
        print((a.posX,a.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[a.posX,a.posY] = " @ "
                current_room_map[a.posX-1,a.posY] = "   "
                current_room['posX'] = a.posX
                current_room['posY'] = a.posY
                rooms[r]['room_map'] = current_room_map
        print(r)

def reroll():
    dice_move = [1,2,3,4]
    roll_move = random.choice(dice_move)
    return roll_move

def monster_move(current_room,r):
    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    mo = 0

    for monster in current_room['monster_list']:
        time.sleep(.5)
        dice_move = [1,2,3,4,5,6,7,8,9]
        current_monster = current_room['monster_list'][mo]
        current_mon_posX = current_monster['monster_posX']
        current_mon_posY = current_monster['monster_posY']
        roll_move = random.choice(dice_move)
        moveYet = False

        if difficulty == "easy":

            while moveYet == False:
                time.sleep(1)
                print(roll_move)
                if roll_move == 1:
                    # dice roll - moving up
                    print("Monster",current_monster['monster_id'],"is moving aimlessly")
                    # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX,current_mon_posY-1]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posY = current_mon_posY-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX,current_mon_posY+1] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                    else:
                        reroll()
                        return roll_move

                if roll_move == 2:
                    print("Monster",current_monster['monster_id'],"is moving aimlessly")
                    # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX,current_mon_posY+1]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posY = current_mon_posY+1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX,current_mon_posY-1] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                    else:
                        reroll()
                        return roll_move

                if roll_move == 3:
                    print("Monster",current_monster['monster_id'],"is moving aimlessly")
                    # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX-1,current_mon_posY]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posX = current_mon_posX-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX+1,current_mon_posY] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                    else:
                        reroll()
                        return roll_move

                if roll_move == 4:
                    print("Monster",current_monster['monster_id'],"is moving aimlessly")
                    # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX+1,current_mon_posY]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posX = current_mon_posX+1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX-1,current_mon_posY] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                    else:
                        reroll()
                        return roll_move

                if roll_move == 5:
                    print("The monster stares menacingly . . .")
                    moveYet = True
                    pass
                if roll_move == 6 or roll_move == 7 or roll_move == 8\
                or roll_move == 9:

                    xdif = a.posX - current_mon_posX
                    ydif = a.posY - current_mon_posY

                    if xdif > ydif or ydif == 0:
                        if xdif >= 0:

                            print("Monster",current_monster['monster_id'],"is moving towards you")
                            # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                            newCoords = current_room_map[current_mon_posX+1,current_mon_posY]

                            if not newCoords == " # " or newCoords == " @ ":
                                current_mon_posX = current_mon_posX+1

                                for sy in range(current_room_height):
                                    for sx in range(current_room_width):
                                        current_room_map[current_mon_posX,current_mon_posY] = " * "
                                        current_room_map[current_mon_posX-1,current_mon_posY] = "   "
                                        current_monster['monster_posX'] = current_mon_posX
                                        current_monster['monster_posY'] = current_mon_posY
                                moveYet = True
                        elif xdif < 0:

                            print("Monster",current_monster['monster_id'],"is moving towards you")
                            # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                            newCoords = current_room_map[current_mon_posX-1,current_mon_posY]

                            if not newCoords == " # " or newCoords == " @ ":
                                current_mon_posX = current_mon_posX-1

                                for sy in range(current_room_height):
                                    for sx in range(current_room_width):
                                        current_room_map[current_mon_posX,current_mon_posY] = " * "
                                        current_room_map[current_mon_posX+1,current_mon_posY] = "   "
                                        current_monster['monster_posX'] = current_mon_posX
                                        current_monster['monster_posY'] = current_mon_posY
                                moveYet = True
                    elif xdif < ydif or xdif == 0:
                        if ydif >= 0:

                            print("Monster",current_monster['monster_id'],"is moving towards you")
                            # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                            newCoords = current_room_map[current_mon_posX,current_mon_posY+1]

                            if not newCoords == " # " or newCoords == " @ ":
                                current_mon_posY = current_mon_posY+1
                                for sy in range(current_room_height):
                                    for sx in range(current_room_width):
                                        current_room_map[current_mon_posX,current_mon_posY] = " * "
                                        current_room_map[current_mon_posX,current_mon_posY-1] = "   "
                                        current_monster['monster_posX'] = current_mon_posX
                                        current_monster['monster_posY'] = current_mon_posY
                                moveYet = True
                        elif ydif < 0:
                            print("Monster",current_monster['monster_id'],"is moving towards you")
                            # print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                            newCoords = current_room_map[current_mon_posX,current_mon_posY-1]
                            if not newCoords == " # " or newCoords == " @ ":
                                current_mon_posY = current_mon_posY-1
                                for sy in range(current_room_height):
                                    for sx in range(current_room_width):
                                        current_room_map[current_mon_posX,current_mon_posY] = " * "
                                        current_room_map[current_mon_posX,current_mon_posY+1] = "   "
                                        current_monster['monster_posX'] = current_mon_posX
                                        current_monster['monster_posY'] = current_mon_posY
                                moveYet = True
        if difficulty == "hard":
            xdif = a.posX - current_mon_posX
            ydif = a.posY - current_mon_posY
            # print("\nPlayer coordinates:",(a.posX,a.posY))
            # print("\nMonster",mo,"coordinates:",(current_mon_posX,current_mon_posY))
            # print("If xcoord result is positive, monster is to the left; if negative, monster is to the right")
            # print("xdif = ",a.posX - current_mon_posX)
            # print("If ycoord result is positive, monster is above; if negative, monster is below")
            # print("ydif", a.posY - current_mon_posY)
            if xdif > ydif: # or ydif == 0:
                # if left-right distance is greater than up-down difference, or is in same row
                if xdif > 0:
                    # if player is to the right or in the same row
                    print("xdif > ydif & xdif >= 0")
                    print("Monster",current_monster['monster_id'],"is moving right")
                    print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX+1,current_mon_posY]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posX = current_mon_posX+1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX-1,current_mon_posY] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                elif xdif < 0:
                    # else if player is to the left
                    print("xdif > ydif & xdif < 0")
                    print("Monster",current_monster['monster_id'],"is moving left")
                    print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX-1,current_mon_posY]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posX = current_mon_posX-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX+1,current_mon_posY] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                elif xdif == 0:
                    newCoords = current_room_map[current_mon_posX,current_mon_posY-1]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posY = current_mon_posY-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX,current_mon_posY+1] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
            elif xdif <= ydif: # or xdif == 0:
                # otherwise if up-down distance is greater than left-right distance, or player in same column
                if ydif > 0:
                    # if player is up or in the same column
                    print("xdif <= ydif & ydif > 0")
                    print("Monster",current_monster['monster_id'],"is moving down")
                    print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX,current_mon_posY+1]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posY = current_mon_posY+1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX,current_mon_posY-1] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                elif ydif < 0:
                    # else if player is below
                    print("xdif < ydif & ydif < 0")
                    print("Monster",current_monster['monster_id'],"is moving up")
                    print("Current monster coordinates:",(current_mon_posX,current_mon_posY))
                    newCoords = current_room_map[current_mon_posX,current_mon_posY-1]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posY = current_mon_posY-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX,current_mon_posY+1] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
                elif ydif == 0:
                    newCoords = current_room_map[current_mon_posX-1,current_mon_posY]
                    if not newCoords == " # " or newCoords == " @ ":
                        current_mon_posX = current_mon_posX-1
                        for sy in range(current_room_height):
                            for sx in range(current_room_width):
                                current_room_map[current_mon_posX,current_mon_posY] = " * "
                                current_room_map[current_mon_posX+1,current_mon_posY] = "   "
                                current_monster['monster_posX'] = current_mon_posX
                                current_monster['monster_posY'] = current_mon_posY
                        moveYet = True
        # print(current_monster,(current_mon_posX,current_mon_posY))
        mo = mo+1

def print_room(current_room):
    print("\nRoom created at",current_room['coords'],"with",current_room['room_size'],"size.",\
    current_room['room_height'],"cells high and",current_room['room_width'],"cells wide.")

def fight():
    time.sleep(2)
    printSelf()
    time.sleep(2)
    printOpponent()
    time.sleep(2)
    print("\n FIGHT")
    fight = True
    round = 1
    while fight is True:
        if a.speed > b.speed:
            # Turn based combat
            # User speed advantage
            # User attack

            print("\n -----Round ", round, "-----")
            time.sleep(2)
            print("\n You struck first!")
            a_dmg = multiply(a.attack,random.choice(range(0,6)))
            b_avoid = (b.defense + b.speed)*random.choice(avoid_values)
            # time.sleep(2)
            # print("\nYour damage points: "+str(a_dmg))
            # time.sleep(2)
            # print("Opponent's hit points: "+str(b.hit_points))
            time.sleep(3)


            if b_avoid > a.speed:
                a_dmg = 0
                print("\n         The attack missed.")
            elif(a_dmg == 0):
                print("\n         "+b.name+" successfully blocked your attack.")
            else:
                block_amount = b.defense*random.choice(block_values)
                if block_amount >= a_dmg:
                    block_amount = a_dmg
                    print("\n         The attack may be blocked")
                else:
                    pass
                b.hit_points = b.hit_points + block_amount - a_dmg
                print("\n         You hit "+b.name+" for "+str(a_dmg)+", but they blocked "+str(block_amount))


            time.sleep(2)


            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break
            time.sleep(2)


            print("\n Your opponent attacks.")
            b_dmg = multiply(b.attack,random.choice(range(0,6)))
            a_avoid = (a.defense + a.speed)*random.choice(avoid_values)
            # time.sleep(2)
            # print("\nOpponent damage points: "+str(b_dmg))
            # time.sleep(2)
            # print("Your hit points: "+str(a.hit_points))
            time.sleep(3)


            if a_avoid > b.speed:
                b_dmg = 0
                print("\n         The attack missed.")
            elif(b_dmg == 0):
                print("\n         You successfully blocked "+b.name+"'s' attack.")
            else:
                block_amount = a.defense*random.choice(block_values)
                if block_amount >= b_dmg:
                    block_amount = b_dmg
                    print("\n         The attack may be blocked")
                else:
                    pass
                a.hit_points = a.hit_points + block_amount - b_dmg
                print("\n         You were hit for "+str(b_dmg)+", but blocked "+str(block_amount))


            time.sleep(2)
            time.sleep(2)
            round = round+1
            print("\nEnd of round!")
            a.speed = random.choice(ads_values)
            b.speed = random.choice(ads_values)
            time.sleep(1.5)
            printSelf()
            print("\n Loading . . .")
            time.sleep(4)
            printOpponent()
            print("\n Loading . . .")
            time.sleep(4)


            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break
            input("\nPress enter to advance to the next round")


        else:

            print("\n -----Round ", round,"-----")
            time.sleep(2)
            print("\n Your opponent is faster..")
            b_dmg = multiply(b.attack,random.choice(range(0,6)))
            a_avoid = (a.defense + a.speed)*random.choice(avoid_values)
            # time.sleep(2)
            # print("\nOpponent damage points: "+str(b_dmg))
            # time.sleep(2)
            # print("Your hit points: "+str(a.hit_points))
            time.sleep(3)


            if a_avoid > b.speed:
                b_dmg = 0
                print("\n         The attack missed.")
            elif(b_dmg == 0):
                print("\n         You successfully blocked "+b.name+"'s' attack.")
            else:
                block_amount = a.defense*random.choice(block_values)
                if block_amount >= b_dmg:
                    block_amount = b_dmg
                    print("\n         The attack may be blocked")
                else:
                    pass
                a.hit_points = a.hit_points + block_amount - b_dmg
                print("\n         You were hit for "+str(b_dmg)+", but blocked "+str(block_amount))
            time.sleep(2)


            if b.hit_points <=0:
                print("\n~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n~~~~~You lose:(~~~~~")
                break
            time.sleep(2)


            print("\n ..but you won't go down without a fight!")
            a_dmg = multiply(a.attack,random.choice(range(0,6)))
            b_avoid = (b.defense + b.speed)*random.choice(avoid_values)
            # time.sleep(2)
            # print("\nYour damage points: "+str(a_dmg))
            # time.sleep(2)
            # print("Opponent's hit points: "+str(b.hit_points))
            time.sleep(3)


            if b_avoid > a.speed:
                a_dmg = 0
                print("\n         The attack missed.")
            elif(a_dmg == 0):
                print("\n         "+b.name+" successfully blocked your attack.")
            else:
                block_amount = b.defense*random.choice(block_values)
                if block_amount >= a_dmg:
                    block_amount = a_dmg
                    print("\n         The attack may be blocked")
                else:
                    pass
                b.hit_points = b.hit_points + block_amount - a_dmg
                print("\n         You hit "+b.name+" for "+str(a_dmg)+", but they blocked "+str(block_amount))


            time.sleep(2)
            round = round+1
            print("\nEnd of round!")
            a.speed = random.choice(ads_values)
            b.speed = random.choice(ads_values)
            time.sleep(1.5)
            printSelf()
            print("\n Loading . . .")
            time.sleep(4)
            printOpponent()
            print("\n Loading . . .")
            time.sleep(2.5)


            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break
            input("\nPress enter to advance to the next round")

def dungeon_run():
    for r in rooms:
        complete = False
        current_room = rooms[r]
        print("\nInitializing room . . .")
        print_room(current_room)
        current_room_width = current_room['room_width']
        current_room_height = current_room['room_height']
        current_room_map = current_room['room_map']
        current_room_door = current_room['door']
        a.posX = rooms[r]['posX']
        a.posY = rooms[r]['posY']

        current_monster_list = current_room['monster_list']


        while complete == False:
            print()
            print_room_map(current_room,r)
            k = input("\nWhat would you like to do? ")
            print("\nPlayer at",(a.posX,a.posY))
            print("\ndoor at",current_room_door)

            mo = 0
            if current_room['monster_list']:
                current_monster = current_room['monster_list'][mo]
                current_mon_posX = current_monster['monster_posX']
                current_mon_posY = current_monster['monster_posY']

            if (a.posX,a.posY) == (current_mon_posX,current_mon_posY):
                print("You are under attack!")
                b.name = current_monster['monster_name']
                b.attack = current_monster['monster_attack']
                b.defense = current_monster['monster_defense']
                b.hit_points = current_monster['monster_hit_points']
                b.speed = current_monster['monster_speed']
                b.pet = False
                fight()
                if a.hit_points <= 0:
                    print("The monster got you!")
                    break
                else:
                    print("You successfuly killed the monster.")
                    current_room_map[current_mon_posX,current_mon_posY] = "   "
                    current_mon_posX = ""
                    current_mon_posY = ""
                    current_room_map[a.posX,a.posY] = " @ "
                    del current_room['monster_list'][mo]
                    print(current_room['monster_list'])
                mo = mo+1

            if (a.posX,a.posY) == current_room_door:
                print("\nCongrats! You escaped room",str(r)+"!")
                complete == True
                r = r+1
                break
            else:
                if k == "w" or 'up' in k:
                    move_up(current_room,r)
                    if (a.posX,a.posY) == current_room_door:
                        print("\nCongrats! You escaped room",str(r)+"!")
                        complete == True
                        r = r+1
                        break
                elif k == "s" or 'down' in k:
                    move_down(current_room,r)
                    if (a.posX,a.posY) == current_room_door:
                        print("\nCongrats! You escaped room",str(r)+"!")
                        complete == True
                        r = r+1
                        break
                elif k == "a" or 'left' in k:
                    move_left(current_room,r)
                    if (a.posX,a.posY) == current_room_door:
                        print("\nCongrats! You escaped room",str(r)+"!")
                        complete == True
                        r = r+1
                        break
                elif k == "d" or 'right' in k:
                    move_right(current_room,r)
                    if (a.posX,a.posY) == current_room_door:
                        print("\nCongrats! You escaped room",str(r)+"!")
                        complete == True
                        r = r+1
                        break
                else:
                    print(k)
            # print_room_map(current_room,r)

            if current_room['monster_list']:
                monster_move(current_room,r)
            if (a.posX,a.posY) == (current_mon_posX,current_mon_posY):
                print("You are under attack!")
                b.name = current_monster['monster_name']
                b.attack = current_monster['monster_attack']
                b.defense = current_monster['monster_defense']
                b.hit_points = current_monster['monster_hit_points']
                b.speed = current_monster['monster_speed']
                b.pet = False
                fight()
                if a.hit_points <= 0:
                    print("The monster got you!")
                    break
                else:
                    print("You successfuly killed the monster.")
                    current_room_map[current_mon_posX,current_mon_posY] = "   "
                    current_mon_posX = ""
                    current_mon_posY = ""
                    current_room_map[a.posX,a.posY] = " @ "
                    del current_room['monster_list'][mo]
                    print(current_room['monster_list'])
                mo = mo+1
    print("You escaped the dungeon!")

generate_rooms()

dungeon_run()
