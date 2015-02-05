
# Chapter 3


# user-defined function
def foo(x,y):
    return x+y

print foo.__doc__
print foo.__globals__

bar = lambda x,y: x+y
print foo(1,2)
print bar(2,3)

# method

class Foo(object):

#   instance methods
    def instance_method(self, arg):
        statements
#   class methods
    def class_method(cls, arg):
        statements
#   static methods
    def static_method(arg):
        statements

""" built-in functions such as len(), __self__ is set to None , indicating
that the function isn't bound to any specific object . For built-in methods
such as x.append, where x is a list object, __self__ is set to x. """

# Object behaviour and special methods

# Object comparison
__bool__(self)
__hash__(self)

# Type checking
__instancecheck__(cls, object)  # isinstance(object, cls)
__subclasscheck__(cls, sub)     # issubclass(sub, cls)

# Iteration implementation
obj.__iter__()
iter.next() # raise StopIteration to signal the end of iteration

"""
iter = s.__iter__()
while 1:
    try:
        x = _iter.next() # _iter.__next__() in python 3
    except StopIteration:
        break
    # Do statements in body of for loop
"""

