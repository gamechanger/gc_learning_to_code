# Imports don't worry about these
import sys


def part1():
    # GOAL: Create a copy of a list
    #
    # Turn output (defined below) into a copy of input.
    #
    # - The output list will be the SAME length as the input list
    # - The output list will contain the SAME numbers as the input list
    # - The output list will be in the SAME order as the input list
    #
    # ...but...
    #
    # - The output list will be a DIFFERENT list.
    #   If, after creating the output copy, I alter the input list in some way (like appending a new number),
    #   the output list shouldn't change.
    #   What won't work:
    #       output = input
    #   As we talked about in the lecture, this will result in output and input actually being the SAME list.
    #   What you need to do is build up the output list from scratch.
    #
    #
    input = [11, 2, 8, 7, 7, 10, 6, 18, 12, 8, 12, 12, 15, 6, 3]
    output = []


    print output



def part2():
    # GOAL: Create a *filtered* copy of a list
    #
    # Turn output (defined below) into a copy of input, omitting any numbers less than 10.
    #
    # - The output list will be a DIFFERENT length than the input list
    # - The output list will be in the SAME order from the input list (minus the dropped numbers)
    # - The numbers remaining in the output list will all be in the input list
    #
    #
    # Example:
    #     input  = [6, 12, 7, 19, 3, 4, 20]
    #     output = [12, 19, 20]
    #
    #
    input = [11, 2, 8, 7, 7, 10, 6, 18, 12, 8, 12, 12, 15, 6, 3]
    output = []


    print output



def part3():
    # GOAL: Create a *sorted* copy of a list
    #
    # Turn output (defined below) into a sorted copy of input.
    #
    # - The output list will be the SAME length as the input list
    # - The output list will contain the SAME numbers as the input list
    # - The output list will be in a DIFFERENT order from the input list
    #    - The first number in the output list should be the smallest, followed by the next smallest...
    #
    #
    # Example:
    #     input  = [5, 1, 3, 1, 4, 2]
    #     output = [1, 1, 2, 3, 4, 5]
    #
    #
    input = [11, 2, 8, 7, 7, 10, 6, 18, 12, 8, 12, 12, 15, 6, 3]
    output = []


    print output



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
        print "Usage: python list_exercises.py <number>"
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
