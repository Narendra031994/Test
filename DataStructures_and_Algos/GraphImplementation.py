"""
Simple directed graph implementation using Nodes""" 

class Node():
    def __init__(self,value,next):
        self.value = value
        self.next  = next

a = Node("a",Node("b",Node("c",None)))

# Next of a is b
a.next.value
# next of b is c
a.next.next.value

# there is no node after the "c"
a.next.next.next is None


        
        