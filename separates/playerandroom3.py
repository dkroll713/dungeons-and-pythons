import random
from classes import Fighter

f = Fighter("David",10,10,100,10,False,True)
f.posX = 1
f.posY = 1
# now have a fighter with positon (posX,posY)

map_width = 60
map_height = 60
max_room_width = 7
min_room_width = 5
max_room_height = 7
min_room_height = 5
min_rooms = 3
max_rooms = 5
total_rooms = random.choice(range(min_rooms,max_rooms))
map = {}
rooms = {}
# room creation stats & dicts

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
            "coords" : (self.y,self.x)
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

r = 1
# r declared here so that it can be used by room generators
def generate_rooms():
    for r in range(total_rooms):
        room = Room()
        room.print_room()
        room.add_to_map()
        room.add_door()
        room.print_room_map()
        # print(room.door)
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
            "coords" : (room.y,room.x)
            }
        # print(rooms[r+1])
    place_player()

def print_room_map(room,r):
    printed_room_map = list(rooms[r]['room_map'].values())
    chunks = [printed_room_map[i:i+rooms[r]['room_width']] for i in range(0, len(printed_room_map), rooms[r]['room_width'])]
    for chunk in chunks:
        print(''.join(chunk))

def place_player():
    for r in rooms:
        print("\nAdding player position at",(f.posX,f.posY))
        current_room = rooms[r]
        current_room_width = current_room['room_width']
        current_room_height = current_room['room_height']
        current_room_map = current_room['room_map']
        f.posX = random.randrange(1,current_room_width-1)
        f.posY = random.randrange(1,current_room_height-1)
        # print(current_room)
        # print((f.posX,f.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[f.posX,f.posY] = " @ "
                rooms[r]['room_map'] = current_room_map
                rooms[r]['posX'] = f.posX
                rooms[r]['posY'] = f.posY
        # print(current_room)
        print_room_map(current_room,r)

def move_up(current_room,r):
    # current_room = rooms[r]
    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    f.posX = rooms[r]['posX']
    f.posY = rooms[r]['posY']
    # print_room_map(current_room,r)
    if current_room_map[f.posX,f.posY-1] == " # ":
        print("You can't move that way")
    else:
        print("move up")
        f.posY = f.posY-1
        print((f.posX,f.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[f.posX,f.posY] = " @ "
                current_room_map[f.posX,f.posY+1] = "   "
                current_room['posX'] = f.posX
                current_room['posY'] = f.posY
                rooms[r]['room_map'] = current_room_map
        # print_room_map(current_room,r)
        # print(current_room)
        print(r)

def move_down(current_room,r):
    # current_room = rooms[r]
    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    f.posX = rooms[r]['posX']
    f.posY = rooms[r]['posY']
    if current_room_map[f.posX,f.posY+1] == " # ":
        print("You can't move that way")
    else:
        print("move down")
        f.posY = f.posY+1
        print((f.posX,f.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[f.posX,f.posY] = " @ "
                current_room_map[f.posX,f.posY-1] = "   "
                current_room['posX'] = f.posX
                current_room['posY'] = f.posY
                rooms[r]['room_map'] = current_room_map
        # print_room_map(current_room,r)
        # print(current_room)
        print(r)

def move_left(current_room,r):
    # current_room = rooms[r]
    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    f.posX = rooms[r]['posX']
    f.posY = rooms[r]['posY']
    if current_room_map[f.posX-1,f.posY] == " # ":
        print("You can't move that way - left")
    else:
        print("move left")
        f.posX = f.posX-1
        print((f.posX,f.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[f.posX,f.posY] = " @ "
                current_room_map[f.posX+1,f.posY] = "   "
                current_room['posX'] = f.posX
                current_room['posY'] = f.posY
                rooms[r]['room_map'] = current_room_map
        # print_room_map(current_room,r)
        # print(current_room)
        print(r)

def move_right(current_room,r):
    current_room = rooms[r]
    current_room_width = current_room['room_width']
    current_room_height = current_room['room_height']
    current_room_map = current_room['room_map']
    f.posX = rooms[r]['posX']
    f.posY = rooms[r]['posY']
    if current_room_map[f.posX+1,f.posY] == " # ":
        print("You can't move that way - right")
    else:
        print("move right")
        f.posX = f.posX+1
        print((f.posX,f.posY))
        for sy in range(current_room_height):
            for sx in range(current_room_width):
                current_room_map[f.posX,f.posY] = " @ "
                current_room_map[f.posX-1,f.posY] = "   "
                current_room['posX'] = f.posX
                current_room['posY'] = f.posY
                rooms[r]['room_map'] = current_room_map
        # print_room_map(current_room,r)
        # print(current_room)
        print(r)

def print_room(current_room):
    print("\nRoom created at",current_room['coords'],"with",current_room['room_size'],"size.",\
    current_room['room_height'],"cells high and",current_room['room_width'],"cells wide.")

def dungeon_run():
    for r in rooms:
        complete = False
        current_room = rooms[r]
        print("Initializing room . . .")
        print_room(current_room)
        current_room_width = current_room['room_width']
        current_room_height = current_room['room_height']
        current_room_map = current_room['room_map']
        current_room_door = current_room['door']
        f.posX = rooms[r]['posX']
        f.posY = rooms[r]['posY']
        while complete == False:
            print()
            print_room_map(current_room,r)
            k = input("\nWhat would you like to do? ")
            print("Player at",(f.posX,f.posY))
            print("door at",current_room_door)


            if (f.posX,f.posY) == current_room_door:
                print("Congrats! You escaped room",str(r)+"!")
                complete == True
                r = r+1
                break
            else:
                if k == "w" or k == "up":
                    move_up(current_room,r)
                elif k == "s":
                    move_down(current_room,r)
                elif k == "a":
                    move_left(current_room,r)
                elif k == "d":
                    move_right(current_room,r)
                else:
                    print(k)



generate_rooms()
dungeon_run()
