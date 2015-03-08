# Imports don't worry about these
import sys


def part1():
    # GOAL: Create a copy of a one level dict
    #
    # Turn output (defined below) into a copy of input.
    #
    # - The output will contain the same keys and values where each key -> value
    #
    # ...but...
    #
    # - The output list will be a DIFFERENT list.
    #   If, after creating the output copy, I alter the input in some way (like adding a new key value pair),
    #   the output shouldn't change.
    #   What won't work:
    #       output = input
    #
    #
    input = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
             'september': 30, 'october': 31, 'november': 30, 'december': 31}
    output = {}


    print output



def part2():
    # GOAL: Replicate the keys() functionality
    #
    # Turn output (defined below) into a list of the keys of input
    #
    # Example:
    #     input  = {'dog': True, 'cat': True, 'bird': False}
    #     output = ['dog', 'cat', 'bird']
    #
    #
    input = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
             'september': 30, 'october': 31, 'november': 30, 'december': 31}
    output = []


    print output



def part3():
    # GOAL: Replicate the values() functionality
    #
    # Turn output (defined below) into a list of the values of input
    #
    # Example:
    #     input  = {'dog': True, 'cat': True, 'bird': False}
    #     output = [True, True, False]
    #
    #
    input = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
             'september': 30, 'october': 31, 'november': 30, 'december': 31}
    output = []


    print output

def part4():
    # GOAL: Replicate the del functionality
    #
    # Ask for input from the user.  Make output a new dictionary minus the key from the user
    # If they key does not exist in the dictionary, output should be the same as input
    #
    # Example:
    #     input  = {'dog': True, 'cat': True, 'bird': False}
    #     users_key = 'cat'
    #     output = {'dog': True, 'bird': False}
    #
    #
    input = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
             'september': 30, 'october': 31, 'november': 30, 'december': 31}
    output = {}


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
    if sec not in ['1', '2', '3', '4']:
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
    elif sec == '4':
        part4()
    else:
        print "Uh Oh something went wrong"

main()
