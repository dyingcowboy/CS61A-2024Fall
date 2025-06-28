from math import pi,sqrt

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

