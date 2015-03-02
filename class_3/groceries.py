# Imports don't worry about these
import sys

def part1():
    # GOAL: Write a grocery list app that records grocery items input by the user,
    #       and prints out the NEWEST item if asked nicely.
    #
    # ##################### Example Usage ####################
    #
    # Enter a grocery, or type "newest" to see the most recently added grocery, or type "quit" to quit
    # >>> bananas
    #
    # Enter a grocery, or type "newest" to see the most recently added grocery
    # >>> apples
    #
    # Enter a grocery, or type "newest" to see the most recently added grocery
    # >>> newest
    #
    # You most recently added: apples
    # Enter a grocery, or type "newest" to see the most recently added grocery
    # >>> quit
    pass


def part2():
    # GOAL: Write a grocery list app that records grocery items input by the user,
    #       and prints out the OLDEST item if asked nicely.
    #
    # ##################### Example Usage ####################
    #
    # Enter a grocery, or type "oldest" to see the most recently added grocery, or type "quit" to quit
    # >>> bananas
    #
    # Enter a grocery, or type "oldest" to see the most recently added grocery
    # >>> apples
    #
    # Enter a grocery, or type "oldest" to see the most recently added grocery
    # >>> oldest
    #
    # Your oldest item is: bananas
    # Enter a grocery, or type "oldest" to see the most recently added grocery
    # >>> quit
    pass

def part3():
    # GOAL: Write a grocery list app that records grocery items input by the user,
    #       and prints out the NEWEST (n) items if asked nicely.
    #
    # ##################### Example Usage ####################
    #
    # Enter a grocery, or "newest N" (where N is a number) to see the most recently added groceries, or "quit" to quit
    # >>> bananas
    #
    # Enter a grocery, or "newest N" (where N is a number) to see the most recently added groceries, or "quit" to quit
    # >>> apples
    #
    # Enter a grocery, or "newest N" (where N is a number) to see the most recently added groceries, or "quit" to quit
    # >>> oreos
    #
    # Enter a grocery, or "newest N" (where N is a number) to see the most recently added groceries, or "quit" to quit
    # >>> newest 2
    #
    # Your newest 2 items are: apples, oreos
    # Enter a grocery, or "newest N" (where N is a number) to see the most recently added groceries, or "quit" to quit
    # >>> quit
    pass



########################################################
########################################################
########################################################

def main():
    """
    The main function will run your code
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    DO NOT CHANGE THIS CODE
    """
    sec = sys.argv[-1]
    if sec not in ['1', '2', '3']:
        print "Your command line arguments dont make sense"
        print "Usage: python conditionals.py <number>"
        return

    print "Lets check your solutions!\n"
    print "This is part {}\n".format(sec)
    if sec == '1':
        part1()
    elif sec == '2':
        part2()
    elif sec == '3':
        part3()
    else:
        print "Uh Oh something went wrong"

main()
