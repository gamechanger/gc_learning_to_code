import random

# Attributes the Trainer can set in create_pokemon()
# These are GLOBAL variables they can be used anywhere in this file

# DONT CHANGE ANY OF THESE VALUES HERE...MAKE IT HAPPEN IN CREATE_POKEMON!!

# First Trainers Pokemon
TRAINER_1 = None				# Can be anything!
NAME_1 = None					# Can be anything!
TYPE_1 = None					# Must be Fire, Water, Grass, Electric, Psychic
HEALTH_1 = 0					# Must be something RANDOM between 80-100
SPECIAL_ATTACK_1 = None			# Can be anything! 
SPECIAL_ATTACK_DAMAGE_1 = 0 	# Must be something RANDOM between 30-50
NORMAL_ATTACK_1 = None			# Can be anything!
NORMAL_ATTACK_DAMAGE_1 = 0    	# Must be something RANDOM between 0-15

# Second Trainers Pokemon
TRAINER_2 = None				# Can be anything!
NAME_2 = None					# Can be anything!
TYPE_2 = None					# Must be Fire, Water, Grass, Electric, Psychic
HEALTH_2 = 0					# Must be something RANDOM between 80-100
SPECIAL_ATTACK_2 = None			# Can be anything! 
SPECIAL_ATTACK_DAMAGE_2 = 0 	# Must be something RANDOM between 30-50
NORMAL_ATTACK_2 = None			# Can be anything!
NORMAL_ATTACK_DAMAGE_2 = 0    	# Must be something RANDOM between 0-15


# DONT CHANGE THIS VALUE HERE
TURN = 1						# Use this to keep track of whose turn it is
								#	Hint: set it to 1 or 2 for each trainer


def create_pokemon():
	# GOAL: Allow the players to create their pokemon
	#		They must follow the rules listed above!

	# TODO: Use a while loop to get all of the pokemon attributes
	#		Hint: Think about what condition to check!
	print "\nWELCOME PLAYER 1, LETS SET-UP!\n"

	# TODO: Ask the Trainer what they want each attribute to be
	# 		Make sure they follow the rules!
	#		Hint: You will need to convert health and damage to an int!

	# TODO: Set the global variable to the Trainers desired value
	#		But only if its valid!

	# TODO: Rinse and Repeat for the Second Trainers 
	print "\nWELCOME PLAYER 2, LETS SET-UP!\n"


	# DO NOT REMOVE THE LINE BELOW!
	return




def battle():
	# GOAL: create the logic for a single battle turn

	# TODO: figure out which Trainers turn it is, save that in the variable below
	#		Hint: Use the TURN variable
	current_trainer = "Ash Ketchum"

	# TODO: figure out which Pokemon is attacking, save that in a variable below
	current_pokemon = "Pikachu"

	# TODO: Ask the user which attack they want to use (special or normal)
	#		Hint: Make sure they cant enter anything other than special or normal!
	#		Don't forget to change the print statement!
	# NOTE: Special attacks and Normal attacks are different! READ BELOW!
	attack_type = None
	attack_name = None
	print "Trainer {} chose {} attack {}!".format(current_trainer, attack_type, attack_name)

	# TODO: For Normal attacks, there is a RANDOM chance to attack between 1 and 3 times!
	#		Figure out how many times the pokemon will attack, save that in a variable
	#		Don't forget to change the print statement
	normal_attacks = 1
	print "WOAH! {} attacked {} times!".format(current_pokemon, normal_attacks)
	
	# TODO: For Special attacks check if the attack was super effective!
	#		This means the Trainer automatically wins!! There should be a 5% chance
	#		of a super effective attack.
	#		Hint: use random and conditionals to get a 5% probability of a super effective attack
	#		Hint: remember the battle is over when the opponents pokemon has no more health!
	#			  End this battle when a super effective attack happens!
	#		Don't forget to change the conditional and print statement!
	if True:
		print "{}'s Special attack was SUPER EFFECTIVE!".format(current_pokemon)
	
	# TODO: Apply the damage of that attack to the defending player (for non super effective attacks)
	# 		For normal attacks, apply damage for each time the pokemon attacked!!
	# 		Don't forget to change the HEALTH variable for the defending pokemon

	# DO NOT REMOVE THE LINE BELOW!
	return




def main():
	# GOAL: Make a Pokemon Battling Game for Two Players!!
	# Don't worry some of the function calling is done for you
	
	# Make sure to fill in this function!
	create_pokemon()

	# This will randomly select who goes first!
	TURN = random.randint(1,2)

	# This loop goes forever its infinite! We dont know when the battle will end!
	# The means we need a condition inside to check inside the loop to know when to stop
	#	Hint: How do we exit an infinite loop?
	while True:

		# This is where all the battle logic goes!
		battle()

		# TODO: Change this conditional to check if the battle is over
		#	Hint: A battle is over when a pokemons HEALTH is 0 (or negative)
		#		  Don't forget to exit the while loop!!
		if True:
			# TODO: Format these prints for the winning trainer and pokemon!
			# 		Hint: You can check the TURN varaible
			winning_trainer = "Ash Ketchum"
			winning_pokemon = "Pikachu"
			print "{} won the battle!".format(winning_pokemon) 
			print "Good job Trainer {}!".format(winning_trainer)
			break

		# TODO: Change the turn variable to give the other trainer a turn!
		# 		Hint: Use conditionals!
		TURN = 0




# DO NOT REMOVE THIS LINE
main()
