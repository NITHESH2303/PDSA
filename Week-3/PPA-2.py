class Hashing:
    def __init__(self,c1,c2,m):
        self.hashtable = []
        for i in range(m):
            self.hashtable.append(None)     
        self.c1 = c1
        self.c2 = c2
        self.m = m
    def hashfun(self,data):
        i=0
        hash = (data%self.m + self.c1*i + self.c2*i**2)%m
        while self.hashtable[hash]!=None and i<self.m:
            hash = (data%self.m + self.c1*i + self.c2*i**2)%m
            i+=1
        return hash
    def store_data(self,data):
        if self.hashtable.count(None)!=0:
            hash = self.hashfun(data)
            self.hashtable[hash] = data
        else:
             print("Hash table is full")
    def display_hashtable(self):
         return self.hashtable
c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
	A.store_data(i)
print(A.display_hashtable())