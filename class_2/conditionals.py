# Imports don't worry about these
import sys


def part1():
    # GOAL: Make some If statements!
    #
    # Take some user input using raw_input (this is done for you)
    # Check that input
    
    # TODO: DELETE THE LINE BELOW
    print "YOU HAVEN'T STARTED PART 1 YET!"

    # user input
    gc = raw_input("Type GameChanger: ")
    
    # TODO: Make an if statement that checks the input
    # TODO: print "YOU DID IT" if it is!
    if gc == "GameChanger":
    	print "YOU DID IT"

def part2():
    # GOAL: Use an if/else statement
    #
    # Take some user input about the users occupation
    # If they are an engineer print something
    # if they aren't an engineer print something else

    # TODO: DELETE THE LINE BELOW
    print "YOU HAVEN'T STARTED PART 2 YET!"

    # TODO: Get the users occupation
    # TODO: print something for engineers
    # TODO: print something else for non engineers


def part3():
    # GOAL: Use an if/elif/else statement
    #
    # Get the users favorite color and their favorite number
    #   HINT: raw_input gives you a string, how can we make it an integer?
    # Use an if/elif/else to print something about their color and number choice
    # Use boolean operators in at least one conditional clause
    # Use comparators in at least one conditional clause
    # Use both comparators and boolean operators in at least one coditional clause
    # Do at least one mathematical operation on the users number

    # TODO: DELETE THE LINE BELOW
    print "YOU HAVEN'T STARTED PART 3 YET!"

    # TODO: Get the users favorite color
    # TODO: Get the users favorite number

    # TODO: Make an if statement
    # TODO: Make an elif statement
    # TODO: Make another elif statement
    # TODO: Make an else statement


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
