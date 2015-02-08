import random

def main():
    print "================================"
    print ":: CHOOSE YOUR OWN ADVENTURE  ::"
    print "*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n"

    name = None
    print "Character Name: "
    while not name:
        name = raw_input("Enter player name: ")
    print "Welcome to your adventure {}!".format(name)

    play = True
    while play == True:
        print "You have come to a crossroads in the jungle..."
        ans = get_answer(["Go left to the Volcano", "Go right to the River"])
        if ans == 'a':
            print "{} went to the Volcano!".format(name)
            print "You climb up to the top of the volcano and see a Wizard."
            print "He asks you what he should wear today..."
            ans = get_answer(["Red Rode", "Blue Robe", "Polka Dot Robe"])
            if ans == 'a':
                print "Poor choice {}".format(name)
                print "You clearly just don't understand me! Says the wizard"
                print "The Wizard destroyed you with his magic...whomp. GOODBYE"
            elif ans == 'b':
                print "Decent choice {}".format(name)
                print "The Wizard gives you $20 you're rich! GOODBYE"
            else:
                print "Excellent choice {}!".format(name)
                print "The wizard teleports you into his vault..."
                print "You see three objects which would you take?"
                ans = get_answer(["Magic Scepter", "$1,000,000", "Yo-Yo"])
                if ans == 'a':
                    print "You take the Wizards Magic Scepter!"
                    print "without his septer he has no power! You attack him!"
                    if random.randint(0,1) > 0:
                        print "YOU MISS! The Wizard gets his spare scepter and destroys you. BOODBYE"
                    else:
                        print "YOU GOT HIM! All the Treasure is yours! GOODBYE"
                if ans == 'b':
                    print "You sneakily snag some cash..."
                    print "Your footsteps are just whispers in the wind..."
                    if random.randint(0,1) > 0:
                        print "The Wizard noticed your thievery and destroyed you!. BOODBYE"
                    else:
                        print "Congratulations you just won $1,000,000! GOODBYE"
                else:
                    print "You reach for the Yo-Yo"
                    print "Well since you picked out my robe today I will let you have my Yo-Yo says the Wizard"
                    print "{} got a Yo-Yo! GOODBYE".format(name)
        else:
            print "{} went to the River!".format(name)
            print "{} Splashed around and had a great time!".format(name)
            print "But then you were bitten by a Pirahna!"
            print "What now?"
            ans = get_answer(['Stay Calm', 'Get out of the water', 'Bite the pirahna back', 'Weep Hysterically'])
            if ans == 'a':
                print "Your calmness allows 5 other pirahnas to swarm. {} was eaten alive. GOODBYE".format(name)
            elif ans == 'b':
                print "You are just too Logical for this game! GOODBYE"
            elif ans == 'c':
                print "The pirahna thinks your crazy! It flees in terror! You keep your leg!"
                print "In an effort to stay safe {} heads home. But you found $20 on the way! GOODBYE".format(name)
            else:
                print "Futile. GOODBYE"

        print "Wanna play again {}?".format(name)
        ans = get_answer(['Yes', 'No'])
        if ans == 'b':
            play = False

    print "\nTHANKS FOR PLAYING!!\n"


def get_answer(options):
    choices = ['a', 'b', 'c', 'd']
    choice = None
    for index,opt in enumerate(options):
        print "\t[{}]\t{}".format(choices[index], opt)
    while choice not in choices[0:len(options)]:
        choice = raw_input("Choose an option: ").strip().lower()
    return choice

main()
