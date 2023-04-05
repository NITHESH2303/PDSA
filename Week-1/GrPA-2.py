def isPrime(n,i):
    if n<=2:
        return True if n==2 else False
    if n%i==0:
        return False
    if i*i>n:
        return True
    return isPrime(n,i+1)
    
def Goldbach(n):
    res = []
    for i in range(n//2+1):
        if isPrime(i,2):
            if isPrime(n-i,2):
                res.append((i,n-i))
    return res
n=int(input())
print(sorted(Goldbach(n)))