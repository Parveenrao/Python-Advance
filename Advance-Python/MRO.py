"""MRO (Method Resolution Order) is the order in which Python looks for a method/attribute when it is called on an object.

It is especially important in multiple inheritance, because a class can inherit from multiple parents, 
and we need a consistent way to decide which parent’s method runs first.


Avoids ambiguity in multiple inheritance.

Ensures all parents get initialized exactly once (important in diamond problem).

Works with super() to make cooperative multiple inheritance possible.

"""