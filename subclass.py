# # superclass
# class Person():
#     def __init__(self, per_name, per_age):
#         self.name = per_name
#         self.age = per_age
#
#     def display(self):
#         print("name: ", self.name)
#         print("age: ", self.age)
#
# # subclass
# class Employee(Person):
#     def __init__(self, emp_name, emp_age, emp_salary):
#         self.salary = emp_salary
#         super().__init__(emp_name,emp_age)
#
#
#     def display2(self):
#         super().display()
#         print("salary:",self.salary)
#
# emp = Employee("John Halo", 117, 80000)
#
# emp.display2()

places = {}
class Place():
    type = 'Place'
    def __init__(self, place_counter):
        self.place_counter = place_counter
        places[place_counter] = len(places)+1

rooms = {}
class Room(Place):
    type = 'Room'
    def __init__(self, room_counter, length,width,north,east,south,west,is_dead_end):
    # def __init__(self):
        super().__init__(len(places)+1)
        self.room_counter = room_counter
        self.length = length
        self.width = width
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.is_dead_end = is_dead_end
        rooms[self.room_counter] = self.place_counter

place1 = Place(len(places)+1)
instance = place1
place2 = Place(len(places)+1)
print(vars(instance))
instance = place2
print(vars(instance))
room1 = Room(len(rooms)+1,2,4,None,None,None,None,False)
instance = room1
print(vars(instance))
print(places)
print(rooms)
