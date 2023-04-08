def combinationSort(strList):
    L=[]
    L2 = strList.copy()
    n = len(strList)
    for i in range(n):
        j = i
        while(strList[j][0] < strList[j-1][0] and j>0 ):
            (strList[j],strList[j-1]) = (strList[j-1],strList[j])
            j -= 1
    L = strList
    
    for i in range(n):
        j = i
        while(L2[j][0] <= L2[j-1][0] and j>0 ):
            if(L2[j][0] == L2[j-1][0]):
                if(int(L2[j][1:]) > int(L2[j-1][1:])):
                     (L2[j],L2[j-1]) = (L2[j-1],L2[j])
                else:
                    (L2[j],L2[j-1]) = (L2[j],L2[j-1])
            else:
                (L2[j],L2[j-1]) = (L2[j-1],L2[j])
            j -= 1
    return L,L2

print(combinationSort(['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']))