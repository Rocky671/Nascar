#####################################
##|                               |##
##|                               |##
##|         Rocky Vargas          |##
##|                               |##
##|                               |##
#####################################





from random import randint

#Car Generator
name = ["Jasper", "Ethyn", "Rocky", "Steve", "James", "Chris", "Cooley", "Storm", "Richard", "Sarah", "Kevin", "Karen", "Tyler", "Marcos", "Jimenez", "Rhoda", "Justin", "Patrick", "Jairo", "Madonna"]
sponsor = ["Bethesda", "Chic fil a", "UAT", "Panda Express", "Nvidia", "AMC", "Fox", "ArenaNet", "Mcdonalds", "Rockstar", "Monster", "Red Bull", "Walmart", "Target", "Pringles", "Taco Bell", "Wendys", "Mobil", "EA", "Gamestop"]

car = []

class Car():

    #Initializing at 0 
    def __init__(self, name, sponsor):
        self.name = name
        self.sponsor = sponsor
        self.miles = 0
        self.speed = 0
        self.avg = 0
        self.lap = 0

    def __str__(self):
        output = '''\n\tDriver Name:\t{}\n\tSponsor:\t{}\n\tMiles:\t{:.2f}\n\tSpeed:\t{:.2f}\n\n'''.format(self.name, \
                    self.sponsor,self.miles,self.speed)
        return output

    #Average speed
    def update(self):
        mph = randint(1,120)
        self.speed = mph
        self.miles += self.speed/60

#Showing car and sponsor
for x in range(len(name)):
    car.append(Car(name[x], sponsor[x]))
    print(car[x])

#Updating car attributes
while car[0].miles < 500:
    for y in range(len(car)):
        car[y].update()
    car.sort(key = lambda x: x.miles, reverse = True)

for x in range(len(car)):
    print(car[x])

print("----------------------------------------\n\n")
#Display Winner
print("Coming in 1st place is: %s\n And in 2nd place: %s\n Finally, in 3rd place: %s"%(car[0], car[1], car[2]))
print("----------------------------------------")
