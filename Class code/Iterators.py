def palindrome(s):
    return all(a==b for a,b in list(zip(s,reversed(s))))

print(palindrome([1,2,3,2,1]))
print(palindrome(['seveneves']))