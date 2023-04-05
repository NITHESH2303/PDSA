import time

def sortInRange(L,r):
    cdict = dict.fromkeys(range(r),0)
    idx=0
    for i in L:
        cdict[i]+=1
    for key in cdict:
        for i in range(cdict[key]):
            L[idx]=key
            idx+=1

def sortInRangeIdeal(L, r):
# Create a dictionary with r keys for each integer in range r, initialize every value to 0
    countDict = [0 for i in range(r)]
# Iterate over the array and count each integer in the list
    for num in L:
        countDict[num] += 1
    index=0
    for key in range(r):
        for i in range(countDict[key]):
            L[index] = key
            index += 1
L = [int(item) for item in input().split()]
r = int(input())
L1=L.copy()
t1 = time.process_time()
sortInRange(L, r)
elapsedStudent = time.process_time() - t1
t1 = time.process_time()
sortInRangeIdeal(L1, r)
elapsedIdeal = time.process_time() - t1
timeout = elapsedIdeal*1.75
if (elapsedStudent > timeout):
    print("Timed Out. Elapsed: " + str(elapsedStudent))
else:
    print(*L)