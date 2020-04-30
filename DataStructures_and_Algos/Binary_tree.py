class Node:
    def __init__(self,value):
        self.val = value
        self.l = None
        self.r = None
root = Node(10)
root.l = Node(11)
root.r = Node(20)
root.l.l = Node(101)
root.l.r = Node(20)

"""
                         10
                        /  \
                       11  20
                       /\
                    101  20
"""

        