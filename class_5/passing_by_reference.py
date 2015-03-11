"""
Problem 3

If we pass a list as an argument to a function, it is passed by reference. This
means that any changes we make to the list inside the function will also be visible
outside the function in other places where the list is used.

Write a function that takes `input_list` and `padding`. This function should add
0 to the end of the list until the list is at least `padding` elements long. This
function doesn't need to return anything and you should still be able to see the
changes to your list outside the function.
"""

my_list = [1, 2, 3]

def list_padder(input_list, padding):
    # Write your implementation here
    pass # You can delete this line once you write your implementation
    
assert list_padder(my_list, 2) is None # It doesn't return anything
assert my_list == [1, 2, 3] # There's no work to do since the list is already longer than 2 elements
assert list_padder(my_list, 5) is None # Still returns nothing
assert my_list == [1, 2, 3, 0, 0] # But our original list was changed inside that last list_padder call
print "Problem 3 is finished!"