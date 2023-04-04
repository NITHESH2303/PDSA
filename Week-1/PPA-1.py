def isPrime(a,i):
    if a%i==0:
        return False
    if a<=2:
        return True if a==2 else False
    if i*i>a:
        return True
    return isPrime(a,i+1)
def Twin_Primes(n,m):
    res=[]
    for i in range(n,m-1):
        if isPrime(i,2):
            if isPrime(i+2,2):
                res.append((i,i+2))
    return res
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))