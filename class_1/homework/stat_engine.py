# Instructions: The point of this file is to get you to apply the concepts covered in class to a practical example. In this case you will be making a simplified version of stat engine. This file contains a list of variables that we have assigned. You're job is to calculate derived stats using those variables. The 'TODO' comments  indicate the places where you need to modify the code. Remember to assign the calculated stats to the provided variables, so they get printed in the results section.


### 1. HOOPS STAT ENGINE:

print "---------------------------------------------------"
print "Hoops Stat Engine"
print "---------------------------------------------------\n"

### Variables:

two_point_made = 12
three_point_made = 7
two_point_attempts = 17
three_point_attempts = 11
free_throw_made = 4
free_throw_attempts = 6

field_goal_made = None
field_goal_attempts = None
field_goal_percentage = None
free_throw_percentage = None
two_point_percentage = None
three_point_percentage = None
points = None
true_shooting_attempts = None
true_shooting_percentage = None

### Calculations:

# TODO: calculate field_goal_made (the sum of two point made shots and three point made shots)


# TODO: calculate field_goal_attempts (the sum of two point shot attempts and three point shot attempts)


# TODO: calculate field_goal_percentage (field goal made shots over field goal attempts multiplied by 100)


# TODO: calculate free_throw_percentage (made free throws over free throw attempts multiplied by 100)


# TODO: calculate two_point_percentage (two point made shots over two point attempts multiplied by 100)


# TODO: calculate three_point_percentage (three point made shots over three point attempts multiplied by 100)


# TODO: calculate the total points


# TODO: calculate true_shooting_attempts (FGA + (FTA * 044)) 


# TODO: calculate true_shooting_percentage (PTS / (2 * TSA) * 100)


### Results: 

print "Field goal made: {}".format(field_goal_made)
print "Field goal attempts: {}".format(field_goal_attempts)
print "Field goal percentage: {}%".format(field_goal_percentage)
print "Free throw percentage: {}%".format(free_throw_percentage)
print "Two point percentage: {}%".format(two_point_percentage)
print "Three point percentage: {}%".format(three_point_percentage)
print "Total points: {}".format(points)
print "True shooting attempts: {}".format(true_shooting_attempts)
print "True shooting percentage: {}%".format(true_shooting_percentage)





### 2. BATS STAT ENGINE:

print "\n\n---------------------------------------------------"
print "Bats Stat Engine"
print "---------------------------------------------------\n"

### Variables:

# Batting:
singles = 4
doubles = 3
triples = 1
home_runs = 2
at_bats = 14
strike_outs = 6

hits = None
average = None
total_bases = None
extra_base_hits = None
slugging_percentage = None

# Pitching: 

outs = 11
earned_runs = 4
walks = 5
opponent_hits = 6
opponent_at_bats = 12

innings_pitched = None
earned_run_average = None
base_on_balls_per_inning = None
opponent_batting_average = None
whip = None

### Calculations:

# TODO: calculate hits (the sum of singles, doubles, triples and home runs)


# TODO: calculate average (hits over at bats)


# TODO: calculate total_bases (total number of bases reached (singles * 1) + (doubles * 2) + ... )


# TODO: calculate extra_base_hits (the sum of doubles, triples and home runs)


# TODO: calculate slugging_percentage (total bases over at bats multiplied by 100)


# TODO: calculate innings_pitched (number of outs over 3)


# TODO: calculate earned_run_average ((earned runs * number of innings) / innings pitched))


# TODO: calculate base_on_balls_per_inning (walks over number of innings)


# TODO: calculate opponent_batting_average (opponent number of hits over opponent average)


# TODO: calculate whip (hits plus walks over innings pitched)


### Results: 

print "* Batting stats:"
print "Hits: {}".format(hits)
print "Batting average: {}".format(average)
print "Total bases: {}".format(total_bases)
print "Extra base hits: {}".format(extra_base_hits)
print "Slugging percentage: {}%".format(slugging_percentage)
print "\n* Pitching stats:"
print "Innings pitched: {}".format(innings_pitched)
print "Earned runs average: {}".format(earned_run_average)
print "Base on balls per inning: {}".format(base_on_balls_per_inning)
print "Opponent batting average: {}".format(opponent_batting_average)
print "Whip: {}".format(whip)
