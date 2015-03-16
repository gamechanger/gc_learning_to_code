"""
Problem 4

Python comes with a bunch of built-in functions and methods that we can use very easily. 
For example, let's say you have a string:

my_string = "The quick brown fox"

Here are some neat methods that live on every string in Python:


string.split(separator) : Splits the string at each instance of separator and returns the result as a list

my_string.split(" ") => ["The", "quick", "brown", "fox"]


string.upper() : Returns the string in all caps

my_string.upper() => "THE QUICK BROWN FOX"


string.join(list_of_strings) : Combine a list of strings, placing the initial string between each member of the list

" ".join(["The", "quick", "brown", "fox"]) => "The quick brown fox"

", hooray! ".join(["Python", "Bears"]) => "Python, hooray! Bears, hooray! "


Given all these fun new methods, write a function that takes a parameter `my_string`
and returns the same string but with the names of all i* Apple products capitalized.
"""

APPLE_PRODUCTS = ['ipod', 'iphone', 'ipad', 'imac', 'iwatch']

def simulate_cs_spelling(my_string):
    # Write your implementation here
    # You can reference APPLE_PRODUCTS from in here and Python will know what you mean, you don't need to pass it as a parameter
    pass # You can delete this line once you write your implementation
    
customer_1 = "hello, yes, i believe there is a problem with my IPAD"
customer_2 = "i really wish there was an xbox version but i guess i can watch it on my IWATCH"
customer_3 = "why can i not follow teams on my IPHONE IMAC entertainment device"
assert simulate_cs_spelling(customer_1.lower()) == customer_1
assert simulate_cs_spelling(customer_2.lower()) == customer_2
assert simulate_cs_spelling(customer_3.lower()) == customer_3
print "Problem 4 is finished!"