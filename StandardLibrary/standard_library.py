# standard_library.py
"""Python Essentials: The Standard Library.
<Alexandra Wold>
<MTH 420>
<4/28>
"""


# Problem 1
def prob1(L):
    return(min(L),max(L),sum(L)/len(L))


           
           
my_list=[1, 2, 3]
print(prob1(my_list))



# Problem 2
def prob2():
    int1 = 4
    int2 = int1
if int1 == int2:
    print("this is mutable")
else:
    print("this is immutable")
#list
college = ("oregon","state","university")
OSU = college
if college == OSU:
    print("this is mutable")
else:
    print("this is immuatble")
#str
Str1 = "Hello"
Str2 = Str1 
if Str1 == Str2:
    print("this is mutable")
else:
    print("this is immutable")
#tuple
tuple1 = (1,2,3)
tuple2 = tuple1
if tuple1 == tuple2:
    print("this is mutable")
else:
    print("this is immutable")
#set
set1= {1,2,3}
set2 = set1
if set1 == set2:
    print("this is mutable")
else:
    print("this is immutable")




# Problem 3
def hypot(a, b):
    import calculator
    sumofsquares=calculator.product(a,a)+calculator.product(b,b)
    c=calculator.sqrt(sumofsquares)
    return c
    


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
