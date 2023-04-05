def odd_one(L):
    d = dict()
    for i in L:
        if type(i) not in d:
            d[type(i)] = 0
        d[type(i)] += 1
    for key,value in d.items():
        if value == 1:
            return key.__name__

print(odd_one(eval(input().strip())))