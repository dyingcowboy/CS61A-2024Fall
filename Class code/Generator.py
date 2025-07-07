# def list_partition(n,m):
#     if n<0 or m==0:
#         return []
#     else:
#         exact_match=[]
#         if n==m:
#             exact_match=[str(m)]
#         with_m=[p+' + '+str(m) for p in list_partition(n-m,m)]
#         without_m=list_partition(n,m-1)
#         return exact_match+with_m+without_m
    

def list_partition(n,m):
    if n>0 and m>0:
        if n==m:
            yield str(m)
        for p in list_partition(n-m,m):
            yield p+' + '+str(m)
        yield from list_partition(n,m-1)

for p in list_partition(6,4):print(p) 