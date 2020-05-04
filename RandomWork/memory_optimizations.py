# integer optimization/integer interning
"""
the integers between -5 and 256 are applicable to the shared reference concept
a = 10
b = 10
where a and b are referenced to the same memory location where as:
a  = 300
b = 300
In the above; a and b are in different memory locations.
This optimization strategy is well suited for the image processing techniques(pixel value ranges between 0 to 256).
"""
inta = 10
intb = 10
print("address of inta = {0} \n address of intb = {1}".format(id(inta),id(intb)))
print(inta is intb)

inta = 3000
intb = 3000
print("address of inta = {0} \n address of intb = {1}".format(id(inta),id(intb)))
print(inta is intb)

# string optimization
"""
String optimization is the most useful one when we dealing with the harware eating processes like text parsing and text visualization or text analytics..etc.
String interning is automatic when the string is similar to the identifier.
ex:
a = "hello" b = "hello"  # and b are pointing to the same location
or a = "_hello_machine_learning" b = "_hello_machine_learning"

String interning can also be done using sys module manually.
a = "hello ML" # this is not similar to the identifier

using sys:
a = sys.intern("hello ML")
b = sys.intern("hello ML")
both a and b are pointing to the same location.
benifit of interning : string comparision will take O(1)(asymptotically) instead of O(n)
"""
str1 = "python_optimizer"
str2 = "python_optimizer"
print(str1 is str2) # True if shared reference

import sys
a = sys.intern("python optimizer")
b = sys.intern("python optimizer")
print(str1 is str2) # True if shared reference
#string compare using intern
def comparestring_intern(str1,str2):
    if str1 is str2:
        return "similar"
    else:
        return "not same"
import time
start = time.perf_counter()
print(comparestring_intern(str1,str2))
end = time.perf_counter()
time_intern = end-start
print("time :",end-start)

# traditional string compare
def compareStrings(str1,str2):
    for i,j in zip(str1,str2):
        if i==j:
            continue
        else:
            return "Not same"
    return "similar"
str1 = "python_optimizer"
str2 = "python_optimizer"
import time
start = time.perf_counter()
print(compareStrings(str1,str2))
end = time.perf_counter()
time_traditional  = end-start
print("time :",end-start)


#check the performance of the traditional and optimized string compare
if time_intern < time_traditional:
    print("optimized")
else:
    print("not good")
 
 
#optimization in compile time

"""
1. constant expressions are evaluated during compile time :
example:  25 * 30
2. Sequence calculations less than 20 elements are calculated during the compile time
ex : (20,10)*5

"""
def testExpression():
    b = 20*8888
    c = 'aBV'*2
    d = ('a','b')*20
    return
testExpression.__code__.co_consts # this will show the pre-calculated expressions in tuple