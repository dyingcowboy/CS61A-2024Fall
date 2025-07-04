def sum_list(s):
    if len(s)==0:
        return 0
    else:
        return s[0]+sum_list(s[1:])
# print(sum_list([1,2]))
    
def large(s,n):
    """Return the sublist of postive numbers s with the largest sum that is less than or equal to n"""

    if s==[]:
        return []
    elif s[0]>n:
        return large(s[1:],n)
    else:
        with_s=[s[0]]+large(s[1:],n-s[0])
        without_s=large(s[1:],n)
        if sum_list(with_s)>sum_list(without_s):
            return with_s
        else:
            return without_s
print(large([4,2,5,6,7],3))