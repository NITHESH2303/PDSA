def find_Min_Difference(L,P):
    L.sort()
    n = len(L)
    min_diff = max(L)-min(L)
    for i in range(n-P+1):
        min_diff=min(min_diff,L[i+P-1]-L[i])
    return min_diff
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))