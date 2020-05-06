"""
iterables in python : 
String,List,Tuple,Dictionary,Set
All these iterables support unpacking.

"""

l = [1,2,3,4]
# unpacking a list
a,*b = l
print(a,b)
print(id(a),id(b),id(l),id(l[0]),id(l[1]),id(b[0]))

# unpacking a tuple
tu = (1,2,3,4)
a,*b = tu
print(a,b)
print(id(a),id(b),id(l),id(l[0]),id(l[1]),id(b[0]))

# merging a list 
l1 = [1,2,3,4]
l2 = [5,8,9,7]
list_ = [*l1,*l2]
tuple_ = (*l1,*l2)
set_ = {*l1,*l2}
print(list_,tuple_,set_)

# unpacking a set
s = {1,2,4,55,5,5,5}
A,*B =s
print(A,B) 

# unpacking a dictionary
d = {'key1':12,'key2':10}
a,b = d.values()
print(a,b)
a,b = d.keys()
print(a,b)

# Merge the dictionary
d1 = {'a':10,'b':210}
d2 = {'a':1000}
d3 = {**d1,**d2} # Update the lates values of keys and merge the dicts

# *args
def max_avg(*args:'collects all the arguments and pack into tuple')->"returns max and avg value from the tuple":
    """
    input : *args (can be any positional arguments)
    output: max and avg(of type integer)
    """
    print(args) # This is the tuple with all the elements from the function call
    count = len(args)
    avg = sum(args)/count
    return {'avg' : avg,'max':max(args)}
max_avg(1,4,15,4)

# documentation of a function
help(max_avg)
max_avg.__annotations__ # this will print all the meta data given during parameter creation
