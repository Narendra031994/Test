#Array implementation of the stack
"""
Array implementation has some limitations, The ultimate size of the array is limited.
Each operation in the stack is going to take constant time operation.
i.e  O(1)

Author : Narendra.b.sinappa
Date : 30042020

"""
class Stack:
    def __init__(self,size):
        self.size = size
        self.top = 0
        self.Stk = []
    
    def push(self,value):
        if (self.top == self.size):
            return "your poor stack is full"
        else:
            self.Stk.insert(self.top,value)
            self.top += 1
            print(self.Stk)
    def pop(self):
        if (self.top == 0 and self.Stk[0] == None):
            return " arey!! add some values and pop again!!"
        else:
            self.Stk.pop(self.top)
            self.top -= 1
            
ob = Stack(3)
ob.push(20)
            