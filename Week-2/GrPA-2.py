def findLargest(L):
    n=len(L)
    if n<=1:
        return L[0]
    start = 0
    end = n-1
    mid =0
    while start<=end:
        mid = start+ (end-start)//2
        if mid<end and L[mid]>L[mid+1]:
            return L[mid]
        if mid>start and L[mid]<L[mid-1]:
            return L[mid-1]
        if L[mid]<=L[start]:
            end = mid-1
        else:
            start = mid+1
    return L[-1]

print (findLargest([2, 4, 5, 7, 9]))