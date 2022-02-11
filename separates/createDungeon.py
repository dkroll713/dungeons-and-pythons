from classes import Fighter

def create_tournament_fighters():
    x = int(input("How many fighters are you willing to face? "))+1
    y = 0
    for i in range(1,x):
        fighters.append(Fighter(random.choice(names)+str(i),random.choice(ads_values), random.choice(ads_values), multiply(random.choice(range(1,11)),random.choice(hit_point_values)),
            random.choice(ads_values), False, True))
    for i in range(1,x):
        print(vars(fighters[y]))
        y = y+1

places = {}
class Place():
    type = 'Place'
    def __init__(self, place_id):
        self.place_id = place_id
        places[place_id] = len(places)+1

    def printID(self):
        print("\nThe place place_id is:",self.place_id)

    def printPlace(self):
        print("The area length is", self.length,"units long")
        print("The area width is", self.width,"units wide")

    def lookAround(self):
        if self.north == None:
            print("The north side is empty.")
        if self.east == None:
            print("The east side is empty")
        if self.south == None:
            print("The south side is empty")
        if self.west == None:
            print("The west side is empty")

    def stuck(self):
        print("\nEnter \"search\" to look around.")
        print("\nEnter \"where\" to see where you are in the dungeon")
        print("\nEnter \"move <cardinal direction> to move either north, east, south, or west")

    def navigate(self):
        while self.active == True:
            y = input("\nWhat would you like to do? Enter \"stuck\" for suggestions. \n\n")
            if y.lower() == "stuck":
                place1.stuck()


    # def search(self):
    #     y = input("")
rooms = {}
class Room(Place):
    type = 'Room'
    def __init__(self,room_id,length,width,north,east,south,west,is_dead_end):
        super().__init__(len(places)+1)
        self.room_id = room_id
        self.length = length
        self.width = width
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.is_dead_end = is_dead_end
        rooms[self.room_id] = self.place_id

    def display(self):
        super().lookAround()


place1 = Place(1)
place2 = Place(2)
testFighter = Fighter("David",10,10,100,10,False,True)

# place1.navigate()

room1 = Room(len(rooms)+1,4,5,None,None,None,None,False)

# room1.display()
instance = places[1]
print(instance)
instance = vars(place2)
print(instance)
instance = vars(room1)
print(instance)
print(places)
print(rooms)
