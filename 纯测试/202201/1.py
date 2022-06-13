n=int(input())
l=1;nums=0
for i in range(n):
    nums+=l
    num=nums
    for o in range(l):
        print("{:<4d}".format(num),end="")
        num-=1
    l+=1
    if i<n-1:
        print()