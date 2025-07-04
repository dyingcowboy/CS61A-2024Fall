def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum

print_sum(1)(2)(3)

def split(n):
    """Split the postive n into all but its last digit and ints last digit"""
    return n//10,n%10
def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return sum_digits(all_but_last)+last

def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
fact(3)

def luhn_sum(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return luhn_sum_double(all_but_last)+last
    
def luhn_sum_double(n):
    all_but_last,last=split(n)
    luhn_digit=sum_digits(last*2)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last)+luhn_digit
    
def cascade(n):
    print(n)
    if n>=10:
        cascade(n//10)
        print(n)

# beautifui example for recursion
def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n:f_then_g(grow,print,n//10)
shrink =lambda n:f_then_g(print,shrink,n//10)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

# Tree recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
    
# Counting Partition
def count_partition(n,m):
    if n==0:
        return 1
    if n<0:
        return 0
    if m==0:
        return 0
    return count_partition(n-m,m)+count_partition(n,m-1)