# Instructions: The point of this file is to get you to start working with the different types we covered today. The 'TODO' comments  indicate the places where you need to modify the code.



# Section 1: Ints

# Activity 1
print("--------------------------------------------------")
print("Activity 1")
print("--------------------------------------------------")

x = 2
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(y / x)
print(x % y)
print(y % x)
print(x ** y)
print(y ** x)


# TODO: Change the values of x and y, which cause the following statement to be true? (Feel free to use the REPL to try it out)

print "This should be True:"
print x + y == 5


# TODO: Change the values of x and y, which cause the following statement to be true? (Feel free to use the REPL to try it out)

print "This should be True:"
print x * y == 5


# TODO: Change the values of x and y, which cause the following statement to be true? (Feel free to use the REPL to try it out)

print "This should be True:"
print x % y == 5



# Activity 2
# What int values for x and y will make the following statements true?
print("--------------------------------------------------")
print("Activity 2")
print("--------------------------------------------------")

# TODO: Change the values of x and y, which cause both of the following statements to be true? (Feel free to use the REPL to try it out)

print "Both of these should be true:"
print x / y * y == x
print x / y == .5







# Section 2: floats

# Activity 3
print("--------------------------------------------------")
print("Activity 3")
print("--------------------------------------------------")

x = 2.0
y = 5.0
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(y/x)
print(x**y)
print(y**x)

# What value for x makes these statements true?
print x / y * y == x
print x / y == .5





# Section 3: bools

# Activity 4
print("--------------------------------------------------")
print("Activity 4")
print("--------------------------------------------------")

print (not False)
print (not True)
print (False or False)
print (False or True)
print (True or False)
print (True or True)
print (False and False)
print (False and True)
print (True and False)
print (True and True)

# What value do each of the following statements return?
(True and False) or (True or False)
(not False or False) and not (False and True)

# Activity 5
# What values for x and y make the following statements true?
print("--------------------------------------------------")
print("Activity 5")
print("--------------------------------------------------")

print (x and x) == True
print (x or x) == True
print (x and x) == x
print (x or x) == x
print (x and y or not x) == True





# Section 4: strings

# Activity 6
print("--------------------------------------------------")
print("Activity 6")
print("--------------------------------------------------")

x = "hello"
y = "world"
print x
print y
print x + y
print x + " " + y
print 2 * x
print x + str(5) + y
print x + 5 + y
print len(x) + len(y)
print x == "hello"
print y == "WORLD"

# Using variables x and y write a statement that will print out "Coding is easy"
x = "oding"
y = "is"

# Activity 7
print("--------------------------------------------------")
print("Activity 7")
print("--------------------------------------------------")

# Using variable x and only addition and subtraction make the following statements true
x = "Fun"
print x == "Fun, Fun, Fun, Fun, Fun, "
print x == "Fun, Fun, Fun, Fun, Fun"


# Activity 8
print("--------------------------------------------------")
print("Activity 8")
print("--------------------------------------------------")

# What values of x so that the following statements are true?
x = 1
print (len("GameChanger") / 5) * x == 100
print len("GameChanger") / x == .5
