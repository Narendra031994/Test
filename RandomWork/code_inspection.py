"""
def func(a,b,c,u = 20,kw1,kw2 = 222):
    print(a,b,c,u,kw1,kw2)
"""
def func(a,b,c,u = 20,*,kw1,kw2 = 222):
    print(a,b,c,u,kw1,kw2)
# print the default positional values/arguments -->returns tuple
print(func.__defaults__)
# Default keyword arguments/values -- > returns dict
print(func.__kwdefaults__)
# name of a function
print(func.__name__)

# get the parameters and local varibles of a function
func.__code__.co_varnames
# get the argument/parameter count of some function using the __code__ attribute
func.__code__.co_argcount

#method -- > instance of a class or some function

def func__():
    def inst_func__():
        print("Iam bound to the function func__, I am the method")
    print("I am the master, I am the function")    
instance = func__()
# generator function
import random as e
def gen_rand():
    yield e.random()


import inspect
inspect.isfunction(func)
inspect.ismethod(func)

inspect.ismethod(instance.inst_func__)

inspect.isgeneratorfunction(func)
inspect.isgeneratorfunction(gen_rand)
