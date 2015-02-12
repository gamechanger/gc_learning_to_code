def main():
    ex1()
    print "\n~~ !!STOP AND WAIT FOR THE NEXT EXERCISE!! ~~"
    print "~~ !!Parada y espera para el proximo ejercicio!! ~~\n"
    ex2()
    print "\n~~ !!STOP AND WAIT FOR THE NEXT EXERCISE!! ~~"
    print "~~ !!Parada y espera para el proximo ejercicio!! ~~\n"
    ex3()
    print "\n~~ !!STOP AND WAIT FOR THE NEXT EXERCISE!! ~~"
    print "~~ !!Parada y espera para el proximo ejercicio!! ~~\n"
    ex4()
    print "\n~~ YOU DID IT!! GREAT JOB!! ~~"
    print "~~ Trabajo bien!! ~~\n\n"

def ex1():
    # EXERCISE 1 - True False for boolean expressions
    question = 0
    ans_1 = 'tftff'
    print "EXERCISE 1\n"
    while question < 5:
        ans = raw_input("Question {} (t or f): ".format(question+1)).strip().lower()
        if ans == 't' or ans == 'f':
            if ans == ans_1[question]:
                print "CORRECT"
            else:
                print "INCORRECT"
            question += 1

def ex2():
    # EXERCISE 2 - true false for longer boolean expressions
    question = 0
    ans_1 = 'fttft'
    print "EXERCISE 2\n"
    while question < 5:
        ans = raw_input("Question {} (t or f): ".format(question+1)).strip().lower()
        if ans == 't' or ans == 'f':
            if ans == ans_1[question]:
                print "CORRECT"
            else:
                print "INCORRECT"
            question += 1

def ex3():
    # EXERCISE 3 - true of false for bool exp with complex comparators
    question = 0
    ans_1 = 'tffft'
    print "EXERCISE 3\n"
    while question < 5:
        ans = raw_input("Question {} (t or f): ".format(question+1)).strip().lower()
        if ans == 't' or ans == 'f':
            if ans == ans_1[question]:
                print "CORRECT"
            else:
                print "INCORRECT"
            question += 1

def ex4():
    #EXERCISE 4 - Expressions for boolean operators
    question = 0
    ans_2 = [True, False, True, True, False]
    print "EXERCISE 4\n"
    while question < 5:
        ans = raw_input("Question {} Enter an expression: ".format(question+1))
        if eval(ans) == ans_2[question]:
            print "CORRECT"
            question += 1
        else:
            print "INCORRECT...try again"

main()
