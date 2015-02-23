import random

SWITCH = True
goats = 0
boats = 0
runs = 1000000

for _ in range(runs):
    doors = ['boat', 'goat', 'goat']

    random.shuffle(doors)

    selection = doors.pop(random.randint(0, 2))

    if selection == 'boat':
        door_to_show = doors.pop(random.randint(0, 1))
    elif selection == 'goat':
        door_to_show = doors.remove('goat')

    remaining_door = doors[0]

    if SWITCH:
        selection, remaining_door = remaining_door, selection

    if selection == 'boat':
        boats += 1
    elif selection == 'goat':
        goats += 1

print 'boats: {}%, goats: {}%'.format(
    100*boats/float(runs), 100*goats/float(runs))
