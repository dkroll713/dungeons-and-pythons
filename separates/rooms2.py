# CURRENTLY TESTING - BUILD A MAP IN LIST FORMAT

import random
import cairo

map_width = 60
map_height = 60
max_room_width = 25
min_room_width = 12
max_room_height = 25
min_room_height = 12
min_rooms = 3
max_rooms = 10
total_rooms = random.choice(range(min_rooms,max_rooms))
map = {}
rooms = {}

def start_map():
    print("Printing map")
    for y in range(map_height):
        for x in range(map_width):
            map[x,y] = " "
    # print(map)

start_map()

def draw_dungeon():
    """Draws the dungeon with cairo rectangles."""

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,500,500)
    ctx = cairo.Context(surface)

    for y in range(map_height):
        for x in range(map_width):
            r = random.choice(range(1,10))
            if map[x,y] == "#":
                ctx.set_source_rgb(0.3,0.3,0.3)
            elif map[x,y] == "_":
                ctx.set_source_rgb(0.5,0.5,0.5)
            # elif map[x,y] == 2:
            #     ctx.set_source_rgb(0,0,0)
            # elif map[x,y] == 3:
            #     ctx.set_source_rgb(0,0,0)
            # elif map[x,y] == 4:
            #     ctx.set_source_rgb(255,255,255)
            # elif map[x,y] == 5:
            #     ctx.set_source_rgb(255,255,255)
            ctx.rectangle(x*10,y*10,10,10)
            ctx.fill()
    surface.write_to_png("dungeon.png")
    print("Total rooms: "+str(len(rooms)))

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
        print("Mapping room")
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
            print(randomWallSpot)
            randomWallSpot = list(random.choice(list(rooms[self.room_id]['room_map'].items())))
            spot_coords = randomWallSpot[0]
        else:
            print("adding door at",spot_coords)
            self.room_map[spot_coords] = " _ "
            self.door = spot_coords

def generate_rooms():
    for r in range(total_rooms):
        room = Room()
        room.print_room()
        room.add_to_map()
        room.add_door()
        room.print_room_map()
        print(room.door)
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
        print(rooms[r+1])

def print_dungeon_map():
    map_list = list(map.values())
    map_rows = [map_list[i:i+map_width] for i in range(0,len(map_list), map_width)]
    for row in map_rows:
        # for spot in row:
            # print(spot)
        print(row)

generate_rooms()
# print_dungeon_map()
