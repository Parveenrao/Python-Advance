"""terators are objects that allow you to traverse (iterate) through elements of a collection
(like lists, tuples, sets, etc.) one item at a time, without needing to know the underlying structure."""

"""mylist = [1 , 2, 3]

iterator = iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))"""

#-----------------------------------------------------------------------------------------------------------------

# Custom Iterator Example 

class CountDown:
    def __init__(self , start):
        self.num = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=0:
            raise StopIteration
        
        current = self.num
        
        self.num -=1
        
        return current
    


for i in  CountDown(4):
    print(i)        