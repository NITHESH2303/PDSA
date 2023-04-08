def mergeInPlace(A,B):
    m = len(A)
    n = len(B)
    if m<1 or n<1:
        return
    for i in range(m):
        if A[i] > B[0]:
            A.swap(i,B,0)
        j=0
        while j<n-1 and B[j]>B[j+1]:
            B.swap(j,B,j+1)
            j+=1