import time

def login():
    print('\n\n\n————————————————————————————————————————————\n欢迎使用简单购物系统！\n\n/guest：顾客模式\n/admin：管理员模式\n/exit：退出系统\n————————————————————————————————————————————\n\n\n')
    while True:
        msg = input('<用户> ')
        if msg == '/guest':
            guest();return 0
        elif msg == '/admin':
            if adminlogin() != 0:
                return 0
        elif msg == '/exit':
            print('正在退出......\n');time.sleep(1)
            return 0
        elif msg == '/help':
            print('\n\n\n————————————————————————————————————————————\n<指令帮助>\n\n/guest：顾客模式\n/admin：管理员模式\n/exit：退出系统\n————————————————————————————————————————————\n\n\n')
        elif msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        else:
            print('[错误] 未知的指令，使用 /help 指令来查看帮助。\n')
        time.sleep(0.2)

def adminlogin():
    password=input('请输入管理员密码：\n\n<用户> ')
    if password.isnumeric:
        try:
            if eval(password) == (eval(password)%37)+eval(password[0:2])*377*(eval(password)%37)+eval(password[2:])*4+258*eval(password[3:4]):
                print('密码正确！')
                return 1
            else:
                print('[系统] 密码错误，即将返回菜单！\n')
                time.sleep(2)
                print('使用 /help 指令来查看帮助。\n')
                return 0
        except:
            print('[系统] 密码错误，即将返回菜单！\n')
            print('使用 /help 指令来查看帮助。\n')
            time.sleep(2)
            return 0

def is_kazu(num): #一个自制函数
    if type(num) is not str:
        raise ValueError('parameter must be a string.')
    if num.isnumeric():
        return True
    else:
        return False

def guest():
    print('\n\n\n——————————————————————————————————————————————————————————\n欢迎来到简单购物商店！\n/list - 查看商品列表')
    print('/buy [Item ID] - 单独购买指定物品\n/addtocart [Item ID] - 添加一个指定物品到购物车')
    print('/mycart - 查看购物车\n/check - 结账\n/help - 查看更多指令帮助\n/exit - 退出系统\n——————————————————————————————————————————————————————————\n')
    while True:
        msg = input('<Guest> ')
        if len(msg) >= 6:
            if msg[0:6]=='/help ':
                if msg[6] == '1':
                    guesthelp1()
                elif msg[6] == '2':
                    guesthelp2()
                else:
                    print('[错误] 请输入正确的页数！')
            elif msg[0:6]=='/list ':
                if is_kazu(msg[6:]):
                    global selectidpage
                    selectidpage = int(msg[6:])
                    idlistpage()
                else:
                    print('[错误] 请输入正确的页数！')
        elif msg == '/help':
            guesthelp1()
        elif msg == '/list':
            tidlist()
        elif msg == '/exit':
            print('正在退出......\n');time.sleep(1)
            return 0
        elif msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        else:
            print('[错误] 未知的指令，使用 /help 指令来查看帮助。\n')
        time.sleep(0.2)


def guesthelp1():
    print('\n\n\n\n——————————————————————————————————————————————————————————\n指令帮助 <第1页 / 共2页>\n/list - 查看商品列表')
    print('/list [Page] - 查看商品列表的指定页数')
    print('/buy [Item ID] - 单独购买指定物品\n/addtocart [Item ID] - 添加一个指定物品到购物车')
    print('/addtocart [Item ID] [Amount] - 添加多个指定物品到购物车\n/help [Page] - 查看帮助')
    print('——————————————————————————————————————————————————————————\n')

def guesthelp2():
    print('\n\n\n——————————————————————————————————————————————————————————\n指令帮助 <第2页 / 共2页>')
    print('/mycart - 查看购物车\n/mycart [Page] - 查看购物车的指定页数\n/check - 结账\n/coupon [Coupon Code] - 使用优惠券\n/exit - 退出系统\n——————————————————————————————————————————————————————————\n')

def tidlist():
    if count <=5:
        print('\n\n————————————————————————————————————————————\n商品列表 ',end='')
        print('<第1页 / 共1页>\n————————————————————————————————————————————')
        print('编号          商品名称              价格    \n————————————————————————————————————————————')
        for i in range(count):
            print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————————————————————————\n')
    if count >5:
        print('\n\n————————————————————————————————————————————\n商品列表 ',end='')
        print('<第1页 / 共{}页>\n————————————————————————————————————————————'.format(idpage))
        print('编号          商品名称              价格    \n————————————————————————————————————————————')
        for i in range(5):
            print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————————————————————————\n')

def idlistpage():
    if idpage < selectidpage or selectidpage < 1:
        print('[错误] 请输入正确的页数！')
        return 0
    else:
        print('\n\n————————————————————————————————————————————\n商品列表 ',end='')
        print('<第{}页 / 共{}页>\n————————————————————————————————————————————'.format(selectidpage,idpage))
        print('编号          商品名称              价格    \n————————————————————————————————————————————')
        if selectidpage == idpage:
            for i in range(5*selectidpage-5,5*selectidpage+idsolo-5):
                print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        else:
            for i in range(5*selectidpage-5,5*selectidpage):
                print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————————————————————————\n')



def main():
    idlistfile = open('idlist.txt','a',encoding='utf-8')
    idlistfile.close()
    idlistfile = open('idlist.txt','r+',encoding='utf-8')
    idlist = idlistfile.readlines()
    if idlist == []:
        print('\n————————————————————————————————————————————\n[简单购物] 请在商品列表idlist.txt中添加商品！\n\n格式：商品名|商品价格\n————————————————————————————————————————————\n')
        idlistfile.write('泡面|4\n小泡芙|5\n酒|10\n新游戏光盘|198\n篮球|95\n电脑屏幕|1000\n扑克牌（十七张）|5\n周淑怡定制早安音频|3000\n《哲学：深邃达克幻想》|68\n木吉重工业区门票|220\n夹心棉花糖|10\n一撮毛|1998\n《创价学会全彩收藏集》|78\n《带篮子名言》|-250')
        idlistfile.close()
        input('\n按任意键退出。\n')
    else:
        idlistfile.close()
        global getid,count,idpage,idsolo
        getid = idlist
        count = len(getid)
        idpage = count//5 + 1
        idsolo = count%5
        newidlist = []
        for i in range(count-1):
            getid[i] = getid[i][:-1]
        for i in getid[:]:
            newidlist.extend(i.split('|'))
        getid = []
        for i in range(count):
            getid.append([i+1,newidlist[0+2*i],eval(newidlist[1+2*i])])
        login()


main()