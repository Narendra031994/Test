"""
Single inheritance : class A
                        |
                        |
                     class B(A)
                        
Multi-level inheritance:    class A
                              |
                              |
                           class B(A)
                              |
                              |
                          class C(B)
                    
Multiple inheritance : class A   class B
                          \        / 
                           \      /
                            \    /
                          class C(A,B)     
"""
class Parent_A:
    def __init__(self,):
        print("parent_a class")
    
    def meth1(self,):
        print("this is meth1 of parent class A")

class Parent_B:
    def __init__(self):
        print("parent_b class")
    
    def meth1(self,):
        print("this is meth1 in parent class B")
        
    def meth2(self):
        print("meth2 of parent_b")
        
        
        
class sub_C(Parent_A,Parent_B):
    def __init__(self):
        super().meth1()
        super().meth2()
        print("this is sub_c class")
"""
Method resolution order : 
                        1) when there are methods with the same name in the parent classes then the MRO is used to set the preference for execution of the method
                        2)Only the method of leftmost class will be executed.
                        3) Mro is applicable only for the Mupltiple inheritance.
"""

ob_c = sub_C()
        



        