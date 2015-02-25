import random

switch = False
boats = 0
goats = 0
runs = 1000000

for run in range(runs):
    doors = ['goat', 'goat', 'boat']

    random.shuffle(doors)

    choice = random.randint(0, 2)

    selection_door = doors.pop(choice)

    if selection_door == 'boat':
        # we got a boat!
        # doors = ['goat', goat']
        goat_door = doors.pop(random.randint(0, 1))
    elif selection_door == 'goat':
        # we got a goat
        # doors = ['goat', 'boat']
        # doors = ['boat', goat']
        goat_door = doors.remove('goat')

    remaining_door = doors[0]

    if switch:
        selection_door, remaining_door = remaining_door, selection_door
    if selection_door == 'goat':
        goats += 1
    elif selection_door == 'boat':
        boats += 1

print 'boats: {}%, goats: {}%'.format(
    100*boats/float(runs), 100*goats/float(runs))
