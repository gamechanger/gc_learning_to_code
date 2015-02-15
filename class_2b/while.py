# Imports don't worry about these
import sys
import random

def part0():
    # GOAL: Fix this code!

    num = 1
    while num < 11:
        print num**2


def part1():
    # GOAL: Sanitize some input with a while loop!
    #
    # Ask the user a yes or no question
    # get the users answer
    # If the answer is not yes/no or y/n ask the question again


    # TODO: Ask the user a yes or no question!
    answer = raw_input("Do you like Computers? ")

    while answer != "Yes" and answer != "No":
	    answer = raw_input("Do you like computers? ")






    #       acceptable answers: Yes, yes, Y, y, No, no, N, n
    #       Hint: you may not need to check for every single one of these!
    # TODO: Print out a response to the users answer to your question
    #       The response should be different depending on the answer!


def part2():
    # GOAL: Make a Lucky numbers game
    #
    # make a while loop that runs 3 times
    # each time, get a random number (theres an example below)
    # if any of the random numbers is 5 break out of the loop
    # if non of the numbers are 5 you win! if one of them was you lose!

    # GETTING A RANDOM NUMBER BETWEEN 1-6
    num = random.randint(1, 6)

    # This will print when you start the game
    print "Lucky Numbers! 3 numbers will be generated."
    print "If one of them is a '5', you lose!"

    # TODO: Make a while loop that will run 3 times
    #       Hint: use a counter!
    turns = 0
    while turns < 3:
	    num = random.randint(1, 6)
	    print "You number is {}".format(num)

            if num == 5:
		    print "YOU LOSE"
		    break

	    turns += 1





    # TODO: generate a random number and print it out
    # TODO: Check if that number is a 5
    # TODO: if it is break out of the loop
    # TODO: check if the user won or lost!
    #       Hint: remember that counter?

def part3():
    # GOAL: Write integer division and % logic
    #
    # Get two different numbers from the user
    # In your while loop you will need to subtract y from x
    # How long should you keep looping?
    # Keep track of the how many times you subtract y from x
    # Keep track of the remainder

    # TODO - print out x / y and x % y using a while loop
    print 'Use the force'

def part4():
    # GOAL: Figure out if a number is prime
    #
    # Get a number from a user and then use while loop to figure
    # out if the number is prime
    # What does it mean to be prime?

    # TODO - print out True or False depending on if the number is prime
    print True


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
    if sec not in ['0', '1', '2', '3', '4']:
        print "Your command line arguments dont make sense"
        print "Usage: python conditionals.py <number>"
        return

    print "Lets check your solutions!\n"
    print "This is part {}\n".format(sec)
    if sec == '0':
        part0()
    elif sec == '1':
        part1()
    elif sec == '2':
        part2()
    elif sec == '3':
        part3()
    elif sec == '4':
        part4()
    else:
        print "Uh Oh something went wrong"

main()
