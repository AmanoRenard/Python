class Test:
    '这是一个测试'
    allnum = 0

    def __init__(self,a,b):
        self.a=a
        self.b=b
        Test.allnum += 1

    def say(self):
        print('有%d个实例' % Test.allnum)

ass = Test(1,1)
ass.say()
bss = Test(2,2)
ass.say()
bss.say()
print(ass.__doc__)