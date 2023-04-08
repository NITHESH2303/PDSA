# class create_stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack += [value]
#     def pop(self):
#         ele = self.stack[-1]
#         self.stack = self.stack[:-1]
#         return ele

def operation(a,b,e):
    if e=="+":
        return a+b
    elif e=="-":
        return a-b
    elif e=="*":
        return a*b
    elif e=="/":
        return a/b
    else:
        return a**b

def EvaluateExpression(exp):
    new_Exp = exp.split(" ")
    st = []
    for e in new_Exp:
        if e.isnumeric():
            st.append(e)
        else:
            a2 = int(st.pop())
            a1 = int(st.pop())
            st.append(operation(a1,a2,e))
    return st[0]

print(float(EvaluateExpression(input())))