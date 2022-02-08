import random
import time

def multiply(x,y):
    return x*y

fighters = []
hit_point_values = [3,4,5]
ads_values = [1,2,3,4,5,6,7,8,9,10]
avoid_values = [.1,.2,.3,.4,.5,.6]
names = ['Dad', 'Mom', 'Joe', 'John', 'Toohey', 'Earle', 'Drake', 'Tripp', 'X']

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

def create():
    print("Choose your character:")
    a.name = input("Name: ")
    a.attack = int(input("Choose your attack stat, 1-10: "))
    a.defense = int(input("Choose your defense stat, 1-10: "))
    a.hit_points =multiply(multiply(a.defense,random.choice(hit_point_values)),5)
    a.speed = random.choice(ads_values)
    a.pet = False
    a.status = True

    print(a.name)
    print(a.attack)
    print(a.defense)
    print(a.hit_points)
    if a.status is True:
        print("It's ALIIIIIIIIIIVE")

def create_opponents():
    b.name = random.choice(names)
    b.attack = random.choice(ads_values)
    b.defense = random.choice(ads_values)
    b.hit_points = multiply(multiply(b.defense,random.choice(hit_point_values)),5)
    b.speed = random.choice(ads_values)
    b.pet = False
    b.status = True
    if b.status is True:
        print("Prepare to battle")
    print(b.name,b.attack,b.defense,b.hit_points)

def create_tournament_fighters():
    x = int(input("How many fighters are you willing to face? "))+1
    y = 0
    for i in range(1,x):
        fighters.append(Fighter(random.choice(names)+str(i),random.choice(ads_values), random.choice(ads_values), multiply(random.choice(range(1,11)),random.choice(hit_point_values)),
            random.choice(ads_values), False, True))
    for i in range(1,x):
        print(vars(fighters[y]))
        y = y+1

def printSelf():
    print("\n")
    print("Your fighter: "+str(a.name))
    print("Attack stat: "+str(a.attack))
    print("Defense stat: "+str(a.defense))
    print("Speed stat: "+str(a.speed))
    print("Hit points: "+str(a.hit_points))
    if a.pet is True:
        print("Has a pet")
    else:
        pass

def printOpponent():
    print("\n")
    print("Your opponent: "+str(b.name))
    print("Attack stat: "+str(b.attack))
    print("Defense stat: "+str(b.defense))
    print("Speed stat: "+str(b.speed))
    print("Hit points: "+str(b.hit_points))
    if b.pet is True:
        print("Has a pet")
    else:
        pass

#_dmg = damage points : attack stat * d6
#_resist = applied defense : if def > dmg then reduced damage
#_avoid = applied speed : if avoid > opponent speed, then attack is avoided

def fight():
    time.sleep(2)
    printSelf()
    time.sleep(2)
    printOpponent()
    time.sleep(2)
    print("\n FIGHT")
    fight = True
    round = 0
    while fight is True:
        if a.speed > b.speed:
            # Turn based combat
            # User speed advantage
            # User attack

            print("\n -----Round ", round, "-----")
            print("\n You struck first!")
            a_dmg = multiply(a.attack,random.choice(range(0,6)))
            b_avoid = (b.defense + b.speed)*random.choice(avoid_values)
            time.sleep(1)
            print("\nYour damage points: "+str(a_dmg)+". Your speed points: "+str(a.speed))
            time.sleep(1)
            print("Opponent's hit points: "+str(b.hit_points)+". Opponent's avoid points: "+str(b_avoid))
            if b_avoid > a.speed:
                a_dmg = 0
                print("\nThe attack missed.")
            else:
                b.hit_points = b.hit_points - a_dmg

            time.sleep(1)
            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break
            time.sleep(2)
            print("\n Your opponent managed a hit.")
            b_dmg = multiply(b.attack,random.choice(range(0,6)))
            a_avoid = (a.defense + a.speed)*random.choice(avoid_values)
            time.sleep(1)
            print("\nOpponent damage points: "+str(b_dmg)+". Opponent speed points: "+str(b.speed))
            time.sleep(1)
            print("Your hit points: "+str(a.hit_points)+". Your resist points: "+str(a_avoid))
            if a_avoid > b.speed:
                b_dmg = 0
                print("\nThe attack missed.")
            else:
                a.hit_points = a.hit_points - b_dmg
            time.sleep(1)
            time.sleep(2)
            round = round+1
            print("\nEnd of round!")
            a.speed = random.choice(ads_values)
            b.speed = random.choice(ads_values)
            time.sleep(1.5)
            printSelf()
            time.sleep(4)
            printOpponent()
            time.sleep(4)
            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break
        else:

            print("\n -----Round ", round,"-----")
            print("\n Your opponent is faster..")
            b_dmg = multiply(b.attack,random.choice(range(0,6)))
            a_avoid = (a.defense + a.speed)*random.choice(avoid_values)
            time.sleep(1)
            print("\nOpponent damage points: "+str(b_dmg)+". Opponent speed points: "+str(b.speed))
            time.sleep(1)
            print("Your hit points: "+str(a.hit_points)+". Your resist points: "+str(a_avoid))
            if a_avoid > b.speed:
                a_dmg = 0
                print("\nThe attack missed.")
            else:
                a.hit_points = a.hit_points - b_dmg

            time.sleep(1)
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
            time.sleep(1)
            print("\nYour damage points: "+str(a_dmg)+". Your speed points: "+str(a.speed))
            time.sleep(1)
            print("Opponent's hit points: "+str(b.hit_points)+". Opponent's resist points: "+str(b_avoid))
            if b_avoid > a.speed:
                a_dmg = 0
                print("\nThe attack missed.")
            else:
                b.hit_points = b.hit_points - a_dmg

            time.sleep(2)
            round = round+1
            print("\nEnd of round!")
            a.speed = random.choice(ads_values)
            b.speed = random.choice(ads_values)
            time.sleep(1.5)
            printSelf()
            time.sleep(4)
            printOpponent()
            time.sleep(4)
            if b.hit_points <=0:
                print("\n ~~~~~You win!~~~~~")
                break
            elif a.hit_points <=0:
                print("\n ~~~~~You died:(~~~~~")
                break

create()
create_opponents()
# create_tournament_fighters()
fight()
