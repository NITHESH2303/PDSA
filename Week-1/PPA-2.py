class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Is_valid(self):
        if (self.c < self.a + self.b) and (self.a + self.c >self.b) and (self.b + self.c > self.a):
            return "Valid"
        return "Invalid"   
    def Side_Classification(self):
        if self.Is_valid()=="Valid":
            if self.a==self.b==self.c:
                return "Equilateral"
            if self.a==self.b or self.b==self.c or self.a==self.c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Invalid"
    def Angle_Classification(self):
        if self.Is_valid()=="Valid":
            l = [self.a**2, self.b**2, self.c**2]
            l.sort()
            if l[0] + l[1] > l[2]:
                return "Acute"
            elif l[0] + l[1] == l[2]:
                return "Right"
            elif l[0] + l[1] < l[2]:
                return "Obtuse"
        else:
            return "Invalid"
    def Area(self):
        if self.Is_valid()=="Valid":
            s = (self.a + self.b + self.c)/2
            return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        else:
            return "Invalid"
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())