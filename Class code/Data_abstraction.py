from math import gcd

#constructors and selectors

def rational(n,d):
    """Construct a rational number that represents N/D"""
    g=gcd(n,d)
    return [n//g,d//g]

# def rational(n,d):
#     """Construct a rational number that represents N/D"""
#     def select(name):
#         if name=='n':
#             return n
#         if name=='d':
#             return d
#         else:
#             return select
#     return select

def numer(x):
    """Return the numerator of the rational number x"""
    return x[0]

def denom(x):
    """Return the denominator of the rationa number x"""
    return x[1]

# rational arithemetic

def add_rational(x,y):
    """Add rational number x and y"""
    nx,ny=numer(x),numer(y)
    dx,dy=denom(x),denom(y)
    return rational(nx*dy+ny*dx,dx*dy)

def mul_rational(x,y):
    """Multipy rational number x and y"""
    nx,ny=numer(x),numer(y)
    dx,dy=denom(x),denom(y)
    return rational(nx*ny,dx*dy)

def rationals_are_equal(x,y):
    """Return whether rational number x and y are equal"""
    nx,ny=numer(x),numer(y)
    dx,dy=denom(x),denom(y)
    return nx*dy==ny*dx

def print_rational(x):
    print(numer(x),"/",denom(x))