# Chapter 4 Operators and Expressions

""" Mathematics operator
print 9.0/4  # Division
print 9.0//4 # Truncating division
print 7%4    # Modulo

quotient, remainder = divmod(9,4)
print quotient, remainder
"""

"""
# shifting and logical operators
# 5 = 101   2 = 010
print 5 & 2 # bitwise and
print 5 | 2 # bitwise or
print 5 ^ 2 # bitwise xor
print ~5    # bitwise negation
"""

"""
# pow(x, y, [, modulo])
print pow(3, 4, 7)
print round(5.0)
print round(0.5)
print round(-0.5)
"""

""" Operation on sequences
s + r
s*n, n*s
v1, v2 ... vn = s
s[i]
s[i:j]
s[i:j:stride]
x in s, x not in s
for x in s:
all(s)
any(s)
len(s)
min(s)
max(s)
sum(s, [, initial])
"""


""" String formatting
a = 42
b = 13.142783
c = "hello"
d = {'x': 13, 'y': 1.54321, 'z':'world'}
e = 5628398123741234

print "a is %d" % a
print "%10d %f" % (a, b)
print '%+010d %E' %(a, b)
print '%(x)-10d %(y)0.3g' %d # 13       1.54
print '%0.4s %s' % (c, d['z']) # hell world
print "%*.*f" % (5,3,b)
print "e = %d" % e
vars()
"""

""" Advanced string formatting
print "{0} {1} {2}".format('GooG', 100, 490.10)
stock = { 'name' : 'GOOG', 'shares' : 100, 'price' : 490.10 }

r = "{0[name]} {0[shares]} {0[price]}".format(stock)
print r
r = "{name:8} {shares:8d} {price: 8.2f}".format(name="GOOG", shares=100, price=490.10)
print r
"""

# [[fill[align]] [sign] [0] [width]] [.precision][type]
# < > ^ for left, right and centred alignment within the field

# The function call() operator
"""
def foo(x,y,z):
    return x+y+z

from functools import partial
f = partial(foo, 1, 2)
print f
print f(3)
"""

# Conversion functions
"""
ord() # single character to its integer value
chr() # an integer to character

print bin(25) # an integer to binary string
print oct(25) # an integer to octal string
"""

# Boolean Expressions
# It operates from left to right a and b (evaluate a first)

# x == y object equality
# x is y object identity

# Conditional expressions
"""
a = 5
b = 3
if a <= b:
    minvalue = a
else:
    minvalue = b

minvalue = a if a <= b else b

# List comprehension
values = [1, 100, 45, 23, 73, 37, 69]
clamped = [x if x < 50 else 50 for x in values]
print clamped

"""
