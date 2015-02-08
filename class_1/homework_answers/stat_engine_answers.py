
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

# ANSWER: calculate field_goal_made (the sum of two point made shots and three point made shots)
field_goal_made = two_point_made + three_point_made

# ANSWER: calculate field_goal_attempts (the sum of two point shot attempts and three point shot attempts)
field_goal_attempts = two_point_attempts + three_point_attempts

# ANSWER: calculate field_goal_percentage (field goal made shots over field goal attempts multiplied by 100)
field_goal_percentage = float(field_goal_made) / field_goal_attempts * 100
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate free_throw_percentage (made free throws over free throw attempts multiplied by 100)
free_throw_percentage = float(free_throw_made) / free_throw_attempts * 100
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate two_point_percentage (two point made shots over two point attempts multiplied by 100)
two_point_percentage = float(two_point_made) / two_point_attempts * 100
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate three_point_percentage (three point made shots over three point attempts multiplied by 100)
three_point_percentage = float(three_point_made) / three_point_attempts * 100
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate the total points
points = two_point_made * 2 + three_point_made * 3 + free_throw_made

# ANSWER: calculate true_shooting_attempts (FGA + (FTA * 044))
true_shooting_attempts = field_goal_attempts + free_throw_attempts * 0.44

# ANSWER: calculate true_shooting_percentage (PTS / (2 * TSA) * 100)
true_shooting_percentage = points / (2 * true_shooting_attempts)  * 100
# *No float conversion needed because true_shooting_attempts is already a decimal number

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

# ANSWER: calculate hits (the sum of singles, doubles, triples and home runs)
hits = singles + doubles + triples + home_runs

# ANSWER: calculate average (hits over at bats)
average = float(hits) / at_bats
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate total_bases (total number of bases reached (singles * 1) + (doubles * 2) + ... )
total_bases = singles * 1 + doubles * 2 + triples * 3 + home_runs * 4

# ANSWER: calculate extra_base_hits (the sum of doubles, triples and home runs)
extra_base_hits = doubles + triples + home_runs

# ANSWER: calculate slugging_percentage (total bases over at bats multiplied by 100)
slugging_percentage = float(total_bases) / at_bats * 100
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate innings_pitched (number of outs over 3)
innings_pitched = outs / 3.0

# ANSWER: calculate earned_run_average ((earned runs * number of innings) / innings pitched))
earned_run_average = earned_runs * 9.0 / innings_pitched

# ANSWER: calculate base_on_balls_per_inning (walks over number of innings)
base_on_balls_per_inning = walks / 9.0

# ANSWER: calculate opponent_batting_average (opponent number of hits over opponent average)
opponent_batting_average = float(opponent_hits) / opponent_at_bats
# *Float conversion needed because the result of the division is decimal

# ANSWER: calculate whip (hits plus walks over innings pitched)
whip = float(hits + walks) / innings_pitched
# *Float conversion needed because the result of the division is decimal

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
