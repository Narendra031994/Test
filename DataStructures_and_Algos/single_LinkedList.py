"""
single linked list implementation.
Author:Narendra.b.sinappa
Date : 01052020 DDMMYYYY

Time complexity analysis:
1) Append operation will take O(n) to insert node at the end of the list.
2) get operation will take O(n) : iterate over the nodes to find the element at specified index
3) length operation will take O(n)
4)Display will take  O(n)
Asymptotically, The time complexity of the linkedList = O(n)
"""
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
            
    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def len_(self):
        cur = self.head
        count = 0
        while cur.next!=None:
            count +=1
            cur = cur.next
        return count
    
    def display(self):
        data = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            data.append(cur.data)
        return data
    def get(self,index):
        if (index > self.len_()):
            return "Index is out of range"
        idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if idx == index:
                return cur.data
            idx+=1    
    def remove(self,index):
        if (index > self.len_()):
            return "Index is out of range"
        idx = 0
        cur = self.head
        while True:
            last = cur
            cur = cur.next
            if idx == index:
                last.next = cur.next
                return
            idx += 1
        
obj = LinkedList()
obj.append(155)
print(obj.display())
print(obj.get(3))
obj.remove(1)

