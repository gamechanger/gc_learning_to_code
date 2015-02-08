def main():
	print "WELCOME TO LECTURE 2!\n\n"
	ex1()
	print "\n~~ !!STOP AND WAIT FOR THE NEXT EXERCISE!! ~~"
	print "~~ !!Parada y espera para el proximo ejercicio!! ~~\n"
	ex2()
	print "\nYOU DID IT!! GREAT JOB!!"
	print "gran trabajo!!\n\n"

def ex1():
	# EXERCISE 1 - True False for comparators
	question = 0
	ans_1 = 'ttfftfft'
	print "EXERCISE 1\n"
	while question < 8:
		ans = raw_input("Question {} (t or f): ".format(question+1)).strip().lower()
		if ans == 't' or ans == 'f':
			if ans == ans_1[question]:
				print "CORRECT"
			else:
				print "INCORRECT"
			question += 1

def ex2():
	#EXERCISE 2 - Expressions for comparators
	question = 0
	ans_2 = [True, False, True, True, False]
	print "EXERCISE 2\n"
	while question < 5:
		ans = raw_input("Question {} Enter an expression: ".format(question+1))
		if eval(ans) == ans_2[question]:
			print "CORRECT"
			question += 1
		else:
			print "INCORRECT...try again"

main()
