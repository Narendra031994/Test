name = input("enter the name : ")
_password = "abcd2011"
pcount = len(_password)
while not (len(name)>=5 and name.isalpha() and name.isprintable() and pcount > 2 and _password.isalnum):
    name = input("enter the name : ")
print(name,_password)

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
 