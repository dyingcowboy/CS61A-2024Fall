from math import pi,sqrt
from operator import add, mul

def fib(n):
    """It will return the n th number of fibonacci"""
    pre,curr=1,0
    k=0
    while k<n:
        k+=1
        pre,curr=curr,pre+curr
    return curr

def area(r,shape_constant):
    assert r>0, 'A length must be postive'
    return r**2*shape_constant
def area_square(r):
    return area(r,1)
def are_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

# def sum_naturals(n):
#     """Sum thr first N batural numbers
#     >>> sum_naturals(5)
#     15
#     """
#     total ,k=0,1
#     while k<=n:
#         total,k=total+k,k+1
#     return total
#     use the higher-order function!

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

# functions as return values

def make_adder(n):
    """Return a function that takes one argument called k and return k+n
    >>> add_three=make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k+n
    return adder
add_three=make_adder(3)
result=add_three(4)

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g
m=curry2(add)





