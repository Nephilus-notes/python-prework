# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. The first line of the code has been defined below.


def hello_name(user_name):
    """A print statement to take in the argument, uppercase it, and greet."""
    print("hello_" + user_name.upper() + '!')    


# Question 2 
# Please write a python function, first_odds that prints the odd numbers from 
# 1-100 and returns nothing

def first_odds():
    """If the number is divisible by 2, continue, otherwise print it."""
    for num in range(100):
        if num % 2 == 1:
            print(num)
        else:
            continue

# Question 3
# Please write a python function, max_num_in_list to return the max number of a 
# given list. The first line of code has been defined as below.

def max_num_in_list(a_list):
    """Returning the highest number in the list"""
    return(max(a_list))


# Question 4
# Write a function to return if a given years is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be a boolean Type (True/False).

def is_leap_year(a_year):
    '''Comparing first to 400, then combining divisibility by 4 
    with excepting divisibility by 100.'''
    if int(a_year) % 400 == 0:
        return(True)
    elif int(a_year) % 4 == 0 and int(a_year) % 100 != 0:
        return(True)
    else:
        return(False)

# Question 5
# Write a function to see if all numbers in a list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
# consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Using a counter to compare against the next """
    consecutive_counter= a_list[0]
    for num in a_list:
        if num != consecutive_counter:
            return False
            break
        elif num == consecutive_counter:
            consecutive_counter += 1
            continue
    if True:
        return True