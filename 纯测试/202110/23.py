mylist = []
mynum2 = mynum = eval(input('输入一个数字'))
while mynum>0:
    if mynum % 2 == 0:
        mylist.append(0)
    else:
        mylist.append(1)
    mynum //= 2
mylist.reverse()
print(mynum2,'=',end="",sep='')
for i in mylist:
    print(i,end="",sep='')
print('(B)')