myfriend = ['彭家龙','托乐克','刘俊','李立恒','许海骏','吴展鹏','托乐克','托乐克','托乐克','刘俊','李立恒','托乐克','刘俊','许海骏','彭家龙','许海骏']
a = input('请输入要删除的联系人：')
if a in myfriend:
    b = myfriend.count(a)
    if b >0:
        for s in range(0,b):
            myfriend.remove(a)
    print('删除{}后的联系人名单：{}'.format(a,myfriend))
myfriend.sort()
for i in myfriend[:]:
    if myfriend.count(i) >1:
        myfriend.remove(i)
print('去重后的联系人名单：',myfriend)