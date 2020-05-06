# try and except -- exception handling
a = 2
x = 2
while a > -2:
    try:
        a/x
    except ZeroDivisionError:
        print("{0},{1} - 0 division error".format(a,x))
    finally :
        print("{0},{1} - 0 - always executes".format(a,x))
    a -= 1
    x -= 1
    
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

obj = ComputePower(10,8)
obj.isEnough()
str(obj) # this will execute __str__()
obj # this will execute the __repr__() -- representation 
 
 
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

