import random

failed = False

for run in range(10000):
    n_marbles = random.randint(1, 1000)
    scoop_size = random.randint(1, n_marbles)

    red_tank = ['r']*n_marbles
    blue_tank = ['b']*n_marbles

    scoop = blue_tank[0:scoop_size]
    blue_tank = blue_tank[scoop_size:]

    red_tank = red_tank + scoop

    random.shuffle(red_tank)

    scoop = red_tank[0:scoop_size]
    red_tank = red_tank[scoop_size:]

    blue_tank = blue_tank + scoop

    blue_in_red = 0
    red_in_blue = 0

    for marble in red_tank:
        if marble == 'b':
            blue_in_red += 1

    for marble in blue_tank:
        if marble == 'r':
            red_in_blue += 1

    if blue_in_red != red_in_blue:
        print 'the experiment failed!'
        failed = True
        break
if not failed:
    print 'yippy!'
