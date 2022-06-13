n=int(input())
l=1;nums=0
for i in range(n):
    nums+=l
    num=nums
    for o in range(l):
        print("{:3d}".format(num),end=" ")
        num-=1
    print();l+=1