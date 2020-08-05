"""
first class functions are functions with the properties listed below:
1) It is an object.
2) Can be stored/assigned into the variable.
3) Can be passed as an argument to other function.
4) It can be returned from the other function.
5) Can be stored in the sequence type.

"""

# compute the max of given values 
def funcMax(a :"int",b:"int")-> "returns max value":
    """this is the docstring """
    return a if a>b else b
func(10,20)

type(funcMax)
dir(funcMax)

funcMax.__code__.co_varnames # this will return the local variables and parameter list defined in the function.
funcMax.__defaults__ #this will return default values from the parameter list.

import inspect as ins
ins.ismethod(funcMax)
ins.isfunction(funcMax)

funcMax.__doc__
funcMax.__annotations__

"""reduce functions are used to reduce the sequence iteratively or recursively using 
some mapping defined using lambda or normal def method
"""
from functools import reduce

lis = [2,45,5,14,223,0.3]
reduce(lambda a,b : min(a,b) ,lis)

#this is similar to the above code only difference is the way of computing it 
# custom reduce function using the def__
def reduce_(a,b):
    return a if (a<b) else b
reduce(reduce_,lis)


# map and filter methods 
"""map is similar to the transformation, it returns the map object"""
lis = [10,20,22,255,114,0.555777,455]
map_ = map(lambda a:a+2,lis)
dir(map_) #this is the map obj and can be converted into the list using type casting.ArithmeticError
list(map_)


""" filter function is useful when we want to filter the sequence based on some condition."""

lis = [201,11,55,1,2,4,556,774]
# lets compute the even numbers from the given sequence\
fil_ = filter(lambda a:a if (a%2 == 0) else None,lis)
list(fil_)

# map and dictionary
dic = {"a":120,"b":30}
map_ = map(lambda a:str(dic[a])+":modified",dic)
mod = list(map_)
for i,j in zip(dic,range(len(mod))):
    dic[i] = mod[j]
print(dic)

