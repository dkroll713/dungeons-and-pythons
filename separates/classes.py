import random
import time
import pickle

fighters = []
hit_point_values = [3,4,5]
ads_values = [1,2,3,4,5,6,7,8,9,10]
avoid_values = [.1,.2,.3,.4,.5,.6]
block_values = [.6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
names = ['Sam', 'Ridge', 'Eli', 'Jon', 'William', 'Brandon', 'Joe', 'John', 'Toohey', 'Earle', 'Drake', 'Tripp', 'X']


class Fighter:
    type = 'Fighter'
    def __init__(self, name, attack, defense, hit_points, speed, pet, status):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hit_points = hit_points
        self.speed = speed
        self.pet = pet
        self.status = status

class Opponent:
    type = 'Opponent'
    def __init__(self, name, attack, defense, hit_points, speed, pet, status):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hit_points = hit_points
        self.speed = speed
        self.pet = pet
        self.status = status

a = Fighter
b = Opponent
characterFile = a
