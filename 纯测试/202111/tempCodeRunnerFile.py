x=int(input())
a=1 if x%2==0 else 0
b=1 if 4<x<=12 else 0

t=[]
t.append(a and b)
t.append(a or b)
t.append(not(a and b) and (a or b))
t.append(not(a or b))

t=[1 if i==True else 0 for i in t]
print(t[0],t[1],t[2],t[3])