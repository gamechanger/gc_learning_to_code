

def main():
	"""
	YOU CAN RUN THIS PROGRAM BY TYPING:

		python rabbits.py

	ON THE COMMAND LINE IN THE SAME DIRECTORY THAT THIS FILE IS IN.

	You discover a pair of Rabbits inside the Board Room. Assume they breed as follows:

		1. Each year, each rabbit mates with exactly one other rabbit, with each pair of rabbits producing a litter of 4 bunnies.
		2. Each year after the bunnies are born, 10% (rounded down) of the previously-existing colony are adopted and moved out of the Board Room. All bunnies stay their first year.

	Based on these numbers, write a program to show how the Board Room rabbit population will change over the next 20 years. Your program should output the rabbit population every year for 20 years. You can format the output any way you like, but it should include some introductory text that explains what the program is doing, and it should clearly present the output data.
	To help you check your program, the population in 2015 is 6 rabbits (2 rabbits from 2014 plus 4 bunnies, with no adoptions), the population in 2016 is 18 rabbits (6 from 2015 plus 12 bunnies, with no adoptions), the population in 2017 is 53 (18 rabbits from the previous year, 36 bunnies from the 9 rabbit pairs, and 1 adoption), and the population in 2018 is 152 (53 rabbits from the previous year, 104 bunnies from the 26 full rabbit pairs, and 5 adoptions).

	Steps to follow:
		1. Write a loop that can print out the years and some fixed number of bunnies per year for 20 years.
		2. Add logic to increase the size of the bunny population each year and print out the total bunnies.
		3. Add logic for decreasing the bunny population by 10 percent each year.
	"""

	# BTW that long tripple quoted section is called a Doc String.
	# They are commonly used to explain what a program or function is supposed to do.

	# Hint 1: Use variables to save the current state of the rabbit colony
	#		  i.e. store the current population, number of first year rabbits (etc.)
	# Hint 2: Use a while loop to make sure you calculate population changes
	#   	  for 20 years!
	print 'There are 4 bunnies in 2014'






# DO NOT REMOVE THIS LINE
main()
