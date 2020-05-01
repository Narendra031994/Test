"""
Queue implementation using the circular array method.
Each operation in queue takes O(1) time complexity, it is constant time operation.

""" 
class queue:
    def __init__(self,size):
        self.size = size
        self.r = 0   # pointer to the next availabe cell in the array
        self.f = 0   # pointer to the next deque element
        self.qu = list(map(lambda x:None,range(self.size)))
        
    def enque(self,data):
        if ((self.size-self.f+self.r)%self.size == self.size):
            return "full"
        else:
            self.qu[self.r] = data
            self.r = (self.r+1)%self.size
            if (self.qu[self.r]!=None):
                return "there is no space"
            print(self.qu)
            
    def deque(self):
        if (self.f == self.r == 0):
            return "queue is empty."
        else:
            temp = self.qu.pop(self.f)
            self.qu.insert(self.f,None)
            self.f = (self.f+1)%self.size
            print(self.qu)
            return temp
        

ob = queue(3) 
print(len(ob.qu))
ob.enque(0)
ob.deque()


                      
