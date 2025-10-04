# Lets learn about super in pyton with direct call or cooperactive call 

# Direct Call   -> Problem without super 

# lets suppose we have diamond inheritance again 

class A:
    def __init__(self):
        print("A init")


class B(A):
    def __init__(self):
        print("B init")
        A.__init__(self)         # direct call 
        


class C(A):
    def __init__(self):
        print("C init")
        A.__init__(self)   
        

class D(B , C):
    def __init__(self):
        print("D init")
        B.__init__(self)  
        C.__init__(self)           



d = D()    # here A is called twice duplicacy

#------------------------------------------------------------------------------

# Cooperative Way using Super

class A:
    def __init__(self):
        print("A init")


class B(A):
    def __init__(self):
        print("B init")
        super().__init__()         # direct call 
        


class C(A):
    def __init__(self):
        print("C init")
        super().__init__()   
        

class D(B , C):
    def __init__(self):
        print("D init")
        super().__init__()  
            
d = D()            
            

