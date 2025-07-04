# def search(f):
#     x=0
#     while True:
#         if f(x):
#             return x
#         x+=1

def search(f):
    x=0
    while not f(x):
        x+=1
    return x

def inverse(f):
    """Return g(y) such that g(f(x))-> x"""
    return lambda y:search(lambda x:f(x)==y)
def square(x):
    return x*x
sqrt=inverse(square)
sqrt(9)

def is_three(x):
    return x==3 
    