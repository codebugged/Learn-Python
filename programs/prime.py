# Naive approach 
# time complexity O(n)


def divisor_count(p):
    x=0
    for i in range(1,p+1):
        if(p%i==0):
            x=x+1 
    return x
    
n=int(input())
if(divisor_count(n)==2):
    print("YES")
else:
    print("NO")
    
   
#----------------------------------------------------------

# Optimised approach
# time complexity O(sqrt(n))

import math
def divisor_count(p):
    x=0
    for i in range(2,sqrt(p)+1):
        if(p%i==0):
            x=x+1 
    return x
    
n=int(input())
if(divisor_count(n)==0):
    print("YES")
else:
    print("NO")
    
# ----------------------------------------------------------

Solution can be further optimised using sieve method for large number of queries
    
    
