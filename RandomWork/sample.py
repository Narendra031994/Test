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

