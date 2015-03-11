"""
Problem 2.1

Let's do a problem with default parameters.  
Let's say that you work at McDonald's.  Most people order fries with their order, 
and McDonald's wants a system that is as fast as possible for ordering.  
Write a function that allows the cashier to add fries onto an order by default, 
but allow the cashier to change that if the customer doesn't want fries.

"""

def mcdonalds_order( # What are the parameters? ):
	
	return withFries

assert mcdonalds_order(['chicken_tenders', 'bacon_burger']) == True
assert mcdonalds_order(['garden_salad', 'apple_slices'], False) == False