import random
import time
import pickle

def multiply(x,y):
    return x*y

fighters = []
hit_point_values = [3,4,5]
ads_values = [1,2,3,4,5,6,7,8,9,10]
avoid_values = [.1,.2,.3,.4,.5,.6]
block_values = [.6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
names = ['Dad', 'Mom', 'Joe', 'John', 'Toohey', 'Earle', 'Drake', 'Tripp', 'X']

def printSelf():
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

    def save(self):
        with open("save.pkl", "wb") as fp:
            pickle.dump(characterFile, fp, pickle.HIGHEST_PROTOCOL)

def load():
    with open("save.pkl", "rb") as fp:
        return pickle.load(fp)

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

def start():
    print("\nWelcome to DUNGEONS AND PYTHONS")
    x = False
    start = input("\nWould you like to create a new character or load a save? \nType \"create\" or \"load\": ")
    while x == False:
        if start.lower() == "create":
            create()
            x = True
        elif start.lower() == "load":
            print(load().__dict__)
            a = load().__dict__
            x = True
        else:
            start = input("Type \"create\" to make a new character or \"load\" to load a saved character: ")

def create():
    print("\nChoose your character:")
    a.name = input("\nName: ")
    a.attack = int(input("\nChoose your attack stat, 1-10: "))
    a.defense = int(input("\nChoose your defense stat, 1-10: "))
    a.hit_points =multiply(multiply(a.defense,random.choice(hit_point_values)),5)
    a.speed = random.choice(ads_values)
    a.pet = False
    a.status = True

    printSelf()
    x = False
    sv = input("\nWould you like to save this character?\nType \"yes\" or \"no\": ")
    while x == False:
        if sv.lower() == "yes":
            characterFile.save(characterFile)
            x = True
            pass
        elif sv.lower() == "no":
            x = True
            pass
        else:
            sv = input("\nType \"yes\" or \"no\": ")

def create_opponents():
    b.name = random.choice(names)
    b.attack = random.choice(ads_values)
    b.defense = random.choice(ads_values)
    b.hit_points = multiply(multiply(b.defense,random.choice(hit_point_values)),5)
    b.speed = random.choice(ads_values)
    b.pet = False
    b.status = True
    if b.status is True:
        print("\n\nPrepare to battle")
    # print(b.name,b.attack,b.defense,b.hit_points)

def create_tournament_fighters():
    x = int(input("How many fighters are you willing to face? "))+1
    y = 0
    for i in range(1,x):
        fighters.append(Fighter(random.choice(names)+str(i),random.choice(ads_values), random.choice(ads_values), multiply(random.choice(range(1,11)),random.choice(hit_point_values)),
            random.choice(ads_values), False, True))
    for i in range(1,x):
        print(vars(fighters[y]))
        y = y+1

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
                print("\nThe attack missed.")
            elif(a_dmg == 0):
                print("\nThey successfully blocked your attack.")
            else:
                block_amount = b.defense*random.choice(block_values)
                b.hit_points = b.hit_points + (block_amount) - a_dmg
                print("\nYou hit "+b.name+" for "+str(a_dmg)+", but they blocked "+str(block_amount))


            time.sleep(2)


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
            # time.sleep(2)
            # print("\nOpponent damage points: "+str(b_dmg))
            # time.sleep(2)
            # print("Your hit points: "+str(a.hit_points))
            time.sleep(3)


            if a_avoid > b.speed:
                b_dmg = 0
                print("\nThe attack missed.")
            elif(b_dmg == 0):
                print("\nYou successfully blocked their attack.")
            else:
                block_amount = a.defense*random.choice(block_values)
                a.hit_points = a.hit_points + (block_amount) - b_dmg
                print("\nYou  were hit  for "+str(b_dmg)+", but blocked "+str(block_amount))


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
                print("\nThe attack missed.")
            elif(b_dmg == 0):
                print("\nYou successfully blocked their attack.")
            else:
                block_amount = a.defense*random.choice(block_values)
                a.hit_points = a.hit_points + (a.defense*random.choice(avoid_values)) - b_dmg
                print("\nYou were hit for "+str(b_dmg)+", but blocked "+str(block_amount))
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
                print("\nThe attack missed.")
            elif(a_dmg == 0):
                print("\nThey successfully blocked your attack.")
            else:
                block_amount = b.defense*random.choice(block_values)
                b.hit_points = b.hit_points + (block_amount) - a_dmg
                print("\nYou hit "+b.name+" for "+str(a_dmg)+", but they blocked "+str(block_amount))


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

start()
create_opponents()
# create_tournament_fighters()
# print(load().__dict__)
# fight()
