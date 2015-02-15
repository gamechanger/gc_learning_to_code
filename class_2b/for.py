# Imports don't worry about these
import sys

def part1():
    # GOAL: Figure out if a number is prime
    #
    # Get a number from a user and then use for loop to figure
    # out if the number is prime
    # What does it mean to be prime?

    # TODO - print out True or False depending on if the number is prime
    print True


def part2():
    # Goal: Figure out x * y
    #
    # Ask the user for two numbers
    # Use a for loop to calculate what x * y is

    # TODO print out x * y
    print 0

def part3():
    # Goal: Make a letter counter
    #
    # Ask the user for two things: a phrase and the letter they want a count of
    # Use a for loop to loop over the string to get the number of times that letter occurs

    # TODO print out number of times letter occurs
    print 0


def part4():
    # GOAL: Convert an expression to Leet Speak
    #
    # Ask the user to enter an expression
    # get the users expression
    # Use a for loop to interate over the characters in the expression
    # Convert the right characters:
    #   e/E -> 3
    #   l/L -> 1
    #   s/S -> 5

    # TODO: DELETE THE LINE BELOW
    print "YOU HAVEN'T STARTED PART 1 YET!"

    # TODO: Ask the user to enter an expression
    # TODO: Get the users answer
    # TODO: Use a for loop to change their expression to Leet Speak!
    # TODO: Print out the new super cool expression!
    #       W0W, V3RY 133T, 5UCH C0D3!


def part5():
    # GOAL: Print out the following awesome pattern!
    #
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
    #
    # This problem will require 2 nested for loops (one for counting up, the other for counting down)
    # Use nested for loops to print the pattern above
    #      Hint: to print something on the same line end the print statement with a ,
    #      Hint: To print an empty new line just use print

    # TODO: DELETE THE 2 LINES BELOW
    print "YOU HAVEN'T STARTED PART 2 YET!"

    # TODO: Keep track of how many stars to print
    #       Hint: use a counter!
    # TODO: Make a for loop to run code for each line we want to print
    #       Hint: Use range()
    # TODO: In that loop make a loop to print the stars
    #       Hint: Use print with a , to keep the stars on the same line!
    # TODO: Rinse and Repeat for counting down!
    #
    # Hint: Do this incrementally, get the first nested loop to work then try the other!


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
    if sec not in ['1', '2', '3', '4', '5']:
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
    elif sec == '4':
        part4()
    elif sec == '5':
        part5()
    else:
        print "Uh Oh something went wrong"

main()
