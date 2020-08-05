"""
builtin scopes : this is where all the builtin methods are stored.
global scope :module namespace 
local scope : function namespace

"""
c = 100 #this is the global variable
a = 10 #this is the global variable
def method_(a,b):
    return a,b,c
"""
local namespace is detected while compiling the function.
global namespace is referenced during the runtime if the variable is not in the local namespace.
"""
method_(1,0) #this will print the local variables and global variable if it is not found in the local namespace


def method2(a,b):
    c = 0.33 # this is the local variable and this is identified during the compilation time.
    return a,b,c
method2(4,6)  # this will return the c in local namespace

def method3(a,b):
    global c
    return a,b,c

method3(10,20) # this will return tuple containing local a and b and global c


"""
it is not necessary to create a global variable before using it in the local namespace with the global keyword.
all the local variable references are removed from the local namespace after the execution of the function.

"""

def method4(a,b):
    global z
    z = 2000
    return a,b,z

method4(10,50)
print(z) #this will return the value of z

 
