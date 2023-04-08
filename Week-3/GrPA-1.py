def insertion_sort(res):
    n = len(res)
    if n<=1:
        return
    for i in range(n):
        j=n
        while(j<n and res[j][i]>res[j-1][i]):
            res[j][i] = res[j-1][i]
            j-=1

def DishPrepareOrder(order_list):
    count = dict()
    res = []
    for order in order_list:
        if order in count:
            count[order]+=1
        else:
            count[order] = 1
    for id in sorted(count.keys()):
        res.append((id,count[id]))
    insertion_sort(res)
    ans = []
    for i in res:
        ans.append(i[0])
    return ans
nums = eval(input())
print(DishPrepareOrder(nums))