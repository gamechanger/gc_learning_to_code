# Imports don't worry about these
import sys

def part1():
    # GOAL: Write the logic to loop over a dictionary and print all keys and values
    # output should be similar too:
    # 'math' 4
    # 'science' 3
    # 'history' 1
    # 'german' 1
    # 'spelling' 2
    books_for_school = {'math': 4, 'science': 3, 'history': 1, 'german': 1, 'spelling': 2}

    # TODO remove the line below
    print books_for_school



def part2():
    # GOAL: Write the logic to loop over the dictionary and print the total number of books needed across subjects
    # output should be: 11
    books_for_school = {'math': 4, 'science': 3, 'history': 1, 'german': 1, 'spelling': 2}

    # TODO remove the line below
    print books_for_school

def part3():
    # GOAL: Write an age store. This should be an interactive app that allows you to input and store
    # someones name and age.  If you enter someone's name multiple times, the most recent age should
    # be kept. Print all name: age pairs at the end
    # ##################### Example Usage ####################
    #
    # Enter a persons name and age or "quit" to quit
    # >>> alex 15
    #
    # Enter a persons name and age or "quit" to quit
    # >>> dan 24
    #
    # Enter a persons name and age or "quit" to quit
    # >>> quit

    #TODO remove the line below
    print 'quit'


def part4():
    # GOAL: Write the logic to loop over the dictionary and print the subject with the most number of books
    # The dict below should print out:  math 4
    books_for_school = {'math': 4, 'science': 3, 'history': 1, 'german': 1, 'spelling': 2}

    # TODO remove the line below
    print books_for_school



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
    else:
        print "Uh Oh something went wrong"

main()
