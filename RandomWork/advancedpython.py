# try and except -- exception handling
a = 2
x = 2
while (x >-2):
    try:
        a/x
        
    except ZeroDivisionError:
        print("This is inside the exception")
        print("{0},{1} - 0 division error".format(a,x))
    finally :
        print("this is executed always")
        print("{0},{1} - 0 - always executes".format(a,x))
    x = x-1
    
# enumerate the key and value in collections
"""
collections:
1. sequences : List and Tuple
2.sets : set 
3.mappings: Dictionary
""" 
lis = [1,25,6,8889,77,"agg"]
dic = {}
for i,value in enumerate(lis):
    a,b = i,value # where i and value are in tuple(unpacking the tuple here)
    a = "key"+str(i)
    dic[a] = value
print(dic)


# class and objects, operator/method overloading
class ComputePower:
    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu
    def isEnough(self):
        if self.ram > 8 and self.cpu > 2:
            return "yes, it can handle!!"
        else:
            return "Rebuild the system!!"
    # operator/method overloading
    def __str__(self):
        return "computing power : {0},{1}".format(self.ram,self.cpu)
    def __repr__(self):
        return "ComputePower({0},{1})".format(self.ram,self.cpu)
    def __gt__(self,other):
        if (self.ram > other.ram):
            return "{0} is better than the {1}".format(self,other)
        else:
            return  "{1} is better than the {0}".format(self,other)
    

obj = ComputePower(1,8)
obj.isEnough()
str(obj) # this will execute __str__()
obj # this will execute the __repr__() -- representation 
dir(obj)
Asus = ComputePower(1,4)
HP = ComputePower(8,2)
print(Asus>HP) 
 
 # memory management 
var1 = 10
var2 = var1
print("address of var1 = {0}\n address of var2 = {1}".format(id(var1),id(var2))) 
print(var1 is var2) # check the address and return boolean
print(var1 == var2)# check the value and return true if equal


"""
Mutable objects or structures : List, Sets ,Dict
Immputable objects or structures : Int, Float, Bool,Tuple, String

"""
# Immutable objects and shared references
text = "Data is big."
data = text
def check_sharedref():
    print("address of text = {0}\n address of data = {1}".format(id(text),id(data)))
    if text is data:
        print("shared reference")
    else:
        return "No shared reference"
check_sharedref()
data = text + "but can be interpreted wasily with the help of anlytical tools!!!"
check_sharedref()

# List is mutable and no shared reference when same values assigned to different variable names/identifier
li = [1,3,11]
li_dup = [1,3,11]
print("address of text = {0}\n address of data = {1}".format(id(li),id(li_dup)))

li = [1,1]
li_dup = li
print("address of text = {0}\n address of data = {1}".format(id(li),id(li_dup)))
li_dup.append(10) # this will effect both li and li_dup as they are sharing reference to the same memory location where the list object is stored
print(li,li_dup)

# Tuple is immutable sequence but sometimes elements of tuple are mutable

tu = (1,1)
tu[0] = 10 #integers are immutable, it should throw an error

tu = ([1,1],'a')
tu[0].append(20) # first element is list and it can be mutable
print(tu) # 

# function use shared reference while passing a parameter
import sys
import ctypes
def concat(string):
    print('reference count of string - sys',sys.getrefcount(string))
    print('reference count of string - ctype',ctypes.c_long.from_address(id(string)))
    new = string + "hello"
    print("address of string = {0}\n address of new = {1}".format(id(string),id(new)))
    print(new)
    return
s = "hey!"
concat(s) # id(string) is copied and passed to the function's local variable string.
"""
module space:    s --->hey(address = 111)
function space:  string -----hey(address = 111)
                 new = 'hey! hello' ---->(address = 115)
"""

a = "abcd"
b = a # and b have shared references
sys.getrefcount(a)-1
b = a+ "abcds" # pointing to a new memory location 
sys.getrefcount(a)-1
a = None
print(sys.getrefcount(a)-1 and a is None) # true


""" Sorted is a built in function which takes iterable and returns list in sorted order -->Ascending
"""
#custom sorting
def order_(a:str):
    """accept the string and assign some order to it"""
    if a == 'a':
        a = 100
    elif a == 'b':
        a = 99
    elif a == 'z':
        a = 0
    return a
l = ['a','b','a','z']

sorted(l, key = lambda a: order_(a))

# randomized sorting using the random module

import random
lis = [2,1,4,785,445,56,4,56,885,44,588,6631,4475,4477888955547]
file = open(r"C:\Users\Naren\Desktop\random_sort.txt",'w+')
for i in range(10000):
    file.write(str(sorted(lis,key = lambda a:random.random())) + '\n')
file.close()


# customized sorting using the function
lis = [1,2,3,4]
def sort_(a):
    for i in range(len(lis)):
        if a >= 3:
            a = 0
        return a

sorted(lis,key = sort_)