def count(f):
    def counted(n):
        count.call_count += 1
        return f(n)
    count.call_count =0
    return counted

@count
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(30))
print(count.call_count)
