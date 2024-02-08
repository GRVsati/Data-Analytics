# print row of pascal triangle
 
def ncr(n,r):
    res = 1
    for i in range(0,r):
        res *= (n-i)
        res //= (i+1)
    return res

def ncrow(n):
    l=[]
    for i in range(0,n):
        l.append(ncr(n-1,i))
    return l

ans = ncrow(5)
print(ans)
