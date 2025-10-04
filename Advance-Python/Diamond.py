# Here we are discussing diamond problem 
# Diamond Problem is a python multiple inheritance ambiguity problem 


# suppose all classes define a method called who 

class A:
    def who(self):
        print("A")
 
class B(A):
    def who(self):
        print("B")

class C(A):
    def who(self):
        print("C") 
        
class D(B ,C):
    pass


d = D() 

d.who()                      


# Should D use B.who() (since B is listed first)?

# Or should it use C.who() (since C also defines it)?

# Without Rules is is ambiguos  


#------------------------------------------------------------------------------

# Python MRO(Method Resolution Operator ) with c3 linearization alogorithm 

print(D.mro())