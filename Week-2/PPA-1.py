def binarySearchIndexAndComparisons(L,k):
        start=0
        end=len(L)-1
        count=0
        if end<1:
            return (False,0)
        while(start<=end):
            mid = start + (end-start)//2
            count+=1
            if k==L[mid]:
                return (True, count)
            elif k>=L[mid]:
                start = mid + 1
            else:
                 end = mid - 1
        return (False, count)
                    

L = [int(item) for item in input().split(", ")]
k = int(input())
found, comparisions = binarySearchIndexAndComparisons(L,k)
print (found, comparisions)