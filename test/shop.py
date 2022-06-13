import time
import random
import ctypes
from math import ceil

def login(): #初始界面
    print('\n\n\n\n————————————————————————\n欢迎使用简单购物系统！\n\n【指令帮助】\n/guest：顾客模式\n/admin：管理员模式\n/exit： 退出系统\n\n· BClockraft                    - V1.011\n————————————————————————\n\n')
    while True:
        msg = (input('<用户> ')).lower()
        if msg == '/guest':
            time.sleep(0.7)
            ctypes.windll.kernel32.SetConsoleTitleW("用户： Easy-Shopping System")
            guest()
            ctypes.windll.kernel32.SetConsoleTitleW(" Easy-Shopping System")
        elif msg == '/admin':
            adminlogin()
            ctypes.windll.kernel32.SetConsoleTitleW(" Easy-Shopping System")
        elif msg == '/exit':
            print('正在退出......\n');time.sleep(1)
            return 0
        elif msg == '/help':
            print('\n\n\n————————————————————————\n<指令帮助>\n\n/guest：顾客模式\n/admin：管理员模式\n/exit：退出系统\n————————————————————————\n\n\n')
        elif msg == '' or msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        else:
            print('[错误] 未知的指令，使用 /help 指令来查看帮助。\n')
        time.sleep(0.2)

def adminlogin(): #管理员登入
    password=input('请输入管理员密码：\n\n<用户> ')
    if password.isnumeric:
        try:
            if eval(password) == (eval(password)%37)+eval(password[0:2])*377*(eval(password)%37)+eval(password[2:])*4+258*eval(password[3:4]):
                time.sleep(0.7)
                print('\n欢迎回来，Administrator。')
                time.sleep(1)
                ctypes.windll.kernel32.SetConsoleTitleW("管理员： Easy-Shopping System")
                admin()
                return 0
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

def guest(): #顾客界面
    print('\n\n\n————————————————————————\n欢迎来到简单购物商店！\n/list - 查看商品列表')
    print('/buy [Item ID] - 直接购买一个指定商品\n/addtocart [Item ID] - 添加一个指定商品到购物车')
    print('/mycart - 查看购物车\n/check - 结账\n/help - 查看更多指令帮助\n/exit - 退出顾客模式\n————————————————————————\n')
    while True:
        msg = input('<Guest> ').lower()
        lens = len(msg)
        if msg == '/addtocart':
            print('[错误] 使用方法：/addtocart [Item ID] [Amount]\n')
        elif msg == '/cartclear':
            cartclear()
        elif msg == '/check':
            check()
        elif lens >= 6:
            if msg[0:6]=='/addto' and len(msg) >= 12:
                if msg[0:11]=='/addtocart ':
                    msg=msg.split(' ')
                    if len(msg) == 2:
                        if is_kazu(msg[1]):
                            addtocart(int(msg[1])-1,1)
                        else:
                            print('[错误] 请输入正确的商品编号！\n')
                    elif len(msg) == 3:
                        if is_kazu(msg[1]):
                            if is_kazu(msg[2]):
                                addtocart(int(msg[1])-1,int(msg[2]))
                            else:
                                print('[错误] 请输入正确的数量！\n')
                        else:
                            print('[错误] 请输入正确的商品编号！\n')
                    else:
                        print('[错误] 格式错误，请检查输入。\n')
                else:
                    print('[错误] 格式错误，请检查输入。\n')
            elif msg[0:6] == '/mycar':
                if msg == '/mycart':
                    showmycart(1)
                elif len(msg) >= 8:
                    if msg[0:8] == '/mycart ':
                        msg=msg.split(' ')
                        if len(msg)==2:
                            if is_kazu(msg[1]):
                                showmycart(int(msg[1]))
                            else:
                                print('[错误] 请输入正确的页数！\n')
                        else:
                            print('[错误] 格式错误，请检查输入。\n')
                    else:
                        print('[错误] 格式错误，请检查输入。\n')
                else:
                    print('[错误] 格式错误，请检查输入。\n')
            elif msg[0:6]=='/help ':
                if msg[6] == '1':
                    guesthelp1()
                elif msg[6] == '2':
                    guesthelp2()
                else:
                    print('[错误] 请输入正确的页数！\n')
            elif msg[0:6]=='/list ':
                if is_kazu(msg[6:]):
                    global selectidpage
                    selectidpage = int(msg[6:])
                    idlistpage()
                else:
                    print('[错误] 请输入正确的页数！\n')
            elif msg[0:5]=='/buy ':
                global buyid,buynum
                msg=msg.split(' ')
                if len(msg)==2:
                    if is_kazu(msg[1]):
                        buyid = int(msg[1])-1
                        buy()
                    else:
                        print('[错误] 请输入正确的商品编号！\n')
                elif len(msg)==3:
                    if is_kazu(msg[1]):
                        buyid = int(msg[1])-1
                        if is_kazu(msg[2]):
                            buynum = int(msg[2])
                            buys()
                        else:
                            print('[错误] 请输入正确的数量！\n')
                    else:
                        print('[错误] 请输入正确的商品编号！\n')
            elif msg== '' or msg[0:1] != '/':
                print('[错误] 格式错误，请检查输入。\n')
            else:
                print('[错误] 未知的指令，使用 /help 指令来查看帮助。\n')
            buyid = ''
        elif msg == '/help':
            guesthelp1()
        elif msg == '/list':
            tidlist()
        elif msg == '/buy' or msg == '/buy ':
            print('[错误] 请输入商品编号！\n')
        elif msg == '/exit':
            print('正在退出......\n');time.sleep(1);mycart.clear()
            print('使用 /help 指令来查看帮助。\n')
            return 0
        elif msg== '' or msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        else:
            print('[错误] 未知的指令，使用 /help 指令来查看帮助。\n')
        time.sleep(0.2)


def guesthelp1(): #帮助1
    print('\n\n\n\n————————————————————————\n指令帮助 <第1页 / 共2页>\n/list - 查看商品列表')
    print('/list [Page] - 查看商品列表的指定页数')
    print('/buy [Item ID] - 直接购买一个指定商品\n/buy [Item ID] [Amount] - 直接购买多个指定商品\n/addtocart [Item ID] - 添加一个指定商品到购物车')
    print('/addtocart [Item ID] [Amount] - 添加多个指定商品\n到购物车\n/help [Page] - 查看帮助')
    print('————————————————————————\n')

def guesthelp2(): #帮助2
    print('\n\n\n————————————————————————\n指令帮助 <第2页 / 共2页>')
    print('/mycart - 查看购物车\n/mycart [Page] - 查看购物车的指定页数\n/check - 结账\n/cartclear - 清空购物车\n/exit - 退出顾客模式\n————————————————————————\n')

def tidlist(): #商品列表
    if count <=5:
        print('\n\n————————————————————————\n商品列表 ',end='')
        print('<第1页 / 共1页>\n————————————————————————')
        print('编号          商品名称              价格    \n————————————————————————')
        for i in range(count):
            print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————\n')
    if count >5:
        print('\n\n————————————————————————\n商品列表 ',end='')
        print('<第1页 / 共{}页>\n————————————————————————'.format(idpage))
        print('编号          商品名称              价格    \n————————————————————————')
        for i in range(5):
            print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————\n')

def idlistpage(): #切换商品列表页
    if idpage < selectidpage or selectidpage < 1:
        print('[错误] 请输入正确的页数！\n')
        return 0
    else:
        print('\n\n————————————————————————\n商品列表 ',end='')
        print('<第{}页 / 共{}页>\n————————————————————————'.format(selectidpage,idpage))
        print('编号          商品名称              价格    \n————————————————————————')
        if selectidpage == idpage:
            for i in range(5*selectidpage-5,5*selectidpage+idsolo-5):
                print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        else:
            for i in range(5*selectidpage-5,5*selectidpage):
                print('{0:<10}{1:{3}<12}{2:>8}￥'.format(getid[i][0],getid[i][1],getid[i][2],chr(12288)))
        print('————————————————————————\n')



def main(): #主进程
    ctypes.windll.kernel32.SetConsoleTitleW(" Easy-Shopping System")
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))
    idlistfile = open('idlist.txt','a',encoding='utf-8')
    idlistfile.close()
    idlistfile = open('idlist.txt','r+',encoding='utf-8')
    idlist = idlistfile.readlines()
    if idlist == []:
        print('\n————————————————————————\n[简单购物] 请在商品列表idlist.txt中添加商品！\n\n格式：商品名|商品价格\n————————————————————————\n')
        idlistfile.write('一斤西瓜|5\n泡面|4\n小泡芙|5\n酒|10\n新游戏光盘|198\n篮球|95\n电脑屏幕|1000\n扑克牌（十七张）|5\n周淑怡定制手机铃声|3000\n《哲学：深邃达克幻想》|68\n《我也是个广东人》|35\n《这个世界太乱》|28\n《帕秋莉♂ＧＯ》|98\n《幻想乡》|52\n《阿斯·维堪（ＡＷＣ）》|76\n木吉重工业区门票|220\n夹心糖|10\n毛绒手套|1998\n《带篮子名言》|-250')
        idlistfile.close()
        input('\n*按任意键退出。*\n')
    else:
        idlistfile.close()
        global getid,count,idpage,idsolo,mycart
        mycart = []
        getid = idlist
        count = len(getid)
        idpage = ceil(count/5)
        if count %5 != 0:
            idsolo = count%5
        else: idsolo = 5
        newidlist = []
        for i in range(count-1):
            getid[i] = getid[i][:-1]
        for i in getid[:]:
            newidlist.extend(i.split('|'))
        getid = []
        for i in range(count):
            getid.append([i+1,newidlist[0+2*i],eval(newidlist[1+2*i])])
        login()

def buy(): #购买操作
    if 0<=buyid<=count-1:
        print('————————————————————————\n【商品信息】\n编号：{}\n商品名：{}\n售价：{}￥'.format(getid[buyid][0],getid[buyid][1],getid[buyid][2]))
        print('\n确认购买请输入 /buy confirm\n取消购买请输入/buy cancel\n————————————————————————\n')
        while True:
            msg = input('<Guest> ').lower()
            if msg[0:1] != '/':
                print('[错误] 格式错误，请检查输入。\n')
            elif msg == '/buy confirm':
                print('生成加密订单中，请稍等……\n');time.sleep(random.randint(5,35)/10)
                xiadan(getid[buyid][2])
                time.sleep(2)
                print('使用 /help 指令来查看帮助。\n')
                return 0
            elif msg == '/buy cancel':
                print('已取消购买，即将返回菜单。\n')
                time.sleep(0.5)
                print('使用 /help 指令来查看帮助。\n')
                return 0
            else:
                print('[错误] 请先处理当前正在进行的任务！\n')
    else:
        print('[错误] 商品不存在，请检查输入！\n')
        time.sleep(0.2)

def buys(): #购买多个物品
    if 0<=buyid<=count-1:
        print('————————————————————————\n【商品信息】\n编号：{}\n商品名：{}\n单价：{}￥\n数量：{}\n应付金额：{}￥'.format(getid[buyid][0],getid[buyid][1],getid[buyid][2],buynum,getid[buyid][2]*buynum))
        print('\n确认购买请输入： /buy confirm\n取消购买请输入： /buy cancel\n————————————————————————\n')
        while True:
            msg = input('<Guest> ').lower()
            if msg[0:1] != '/':
                print('[错误] 格式错误，请检查输入。\n')
            elif msg == '/buy confirm':
                print('生成加密订单中，请稍等……\n');time.sleep(random.randint(5,35)/10)
                xiadan(getid[buyid][2]*buynum)
                time.sleep(2)
                print('使用 /help 指令来查看帮助。\n')
                return 0
            elif msg == '/buy cancel':
                print('已取消购买，即将返回菜单。\n')
                time.sleep(0.5)
                print('使用 /help 指令来查看帮助。\n')
                return 0
            else:
                print('[错误] 请先处理当前进行中的事务！\n')
    else:
        print('[错误] 商品不存在，请检查输入！\n')
        time.sleep(0.2)

def xiadan(price): #下单
    buytimes=time.time();buytime=str(buytimes).split('.');buytimes=time.localtime(buytimes)
    t0=int(buytime[0]);t1=int(buytime[1])
    if price < 10000:
        notecode = '{0:0>10}{1}{2:0>8}{3:0>8}'.format((t0+t1*600) , random.randint(0,4) , (price+t1)*3 , int(t1)*7)
        print('\n\n\n————————————————————————\n下单成功！\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n下单金额：{}￥\n————————————————————————\n\n\n'.format(notecode, buytimes.tm_year, buytimes.tm_mon, buytimes.tm_mday, buytimes.tm_hour, buytimes.tm_min, buytimes.tm_sec, price))
    elif price >= 10000:
        notecode = '{0:0>10}{1}{2:0>8}{3:0>8}'.format((t0+t1*600) , random.randint(5,9) , random.randint(0,99999999) , int(t1)*7)
        print('\n\n\n————————————————————————\n下单成功！\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n这是一笔大额订单，该订单记录仅供参考。\n请联系店主开出书面证明文件！\n————————————————————————\n\n\n'.format(notecode, buytimes.tm_year, buytimes.tm_mon, buytimes.tm_mday, buytimes.tm_hour, buytimes.tm_min, buytimes.tm_sec))
    notefile = open('orderforgoods.txt', 'a',encoding='utf-8');notefile.write('%s\n'%notecode);notefile.close()

def addtocart(tid,tnum): #加入购物车
    if tid<0 or tid >= count:
        print('[错误] 商品不存在！\n')
        return 0
    elif tnum<0:
        print('[错误] 商品数量不能是负数！\n')
        return 0
    elif tnum>100:
        print('[错误] 单次添加到购物车的商品数量不能过多！\n')
        return 0
    print('[系统] 已将：{}×{} 加入购物车！\n'.format(getid[tid][1],tnum))
    if mycart==[]:
        mycart.append([getid[tid][0],getid[tid][1],getid[tid][2],tnum])
    else:
        right=0
        for i in range(len(mycart)):
            if getid[tid][0] == mycart[i][0]:
                mycart[i][3]+=tnum
                right=1
        if right == 0:
            mycart.append([getid[tid][0],getid[tid][1],getid[tid][2],tnum])


def showmycart(pagec): #查看购物车
    if mycart==[]:
        print('当前购物车内没有商品，即将返回菜单。\n')
        time.sleep(2)
        print('使用 /help 指令来查看帮助。\n')
        return 0
    cartcount=len(mycart)
    allcartpage = ceil(len(mycart)/5)
    if cartcount%5 != 0:
        solocart=cartcount%5
    else:
        solocart=5
    mycarts = sorted(mycart,key= lambda n:n[0])
    if pagec > allcartpage or pagec < 1:
        print('[错误] 请输入正确的页数！\n')
        return 0
    elif pagec==1:
        if cartcount <=5:
            print('\n\n—————————————————————————\n      我的购物车 ',end='')
            print('<第1页 / 共1页>\n—————————————————————————')
            print('编号          商品名称                  价格  数量    \n—————————————————————————')
            for i in range(cartcount):
                print('{0:<10}{1:{3}<12}{2:>8}￥ ×{4:>3}'.format(mycarts[i][0],mycarts[i][1],mycarts[i][2],chr(12288),mycarts[i][3]))
            print('—————————————————————————\n')
        if cartcount >5:
            print('\n\n—————————————————————————\n      我的购物车 ',end='')
            print('<第1页 / 共{}页>\n—————————————————————————'.format(allcartpage))
            print('编号          商品名称                  价格  数量    \n—————————————————————————')
            for i in range(5):
                print('{0:<10}{1:{3}<12}{2:>8}￥ ×{4:>3}'.format(mycarts[i][0],mycarts[i][1],mycarts[i][2],chr(12288),mycarts[i][3]))
            print('—————————————————————————\n')
    else:
        print('\n\n—————————————————————————\n      我的购物车 ',end='')
        print('<第{}页 / 共{}页>\n—————————————————————————'.format(pagec,allcartpage))
        print('编号          商品名称                  价格  数量    \n—————————————————————————')
        if pagec == allcartpage:
            for i in range(5*pagec-5,5*pagec+solocart-5):
                print('{0:<10}{1:{3}<12}{2:>8}￥ ×{4:>3}'.format(mycarts[i][0],mycarts[i][1],mycarts[i][2],chr(12288),mycarts[i][3]))
        else:
            for i in range(5*pagec-5,5*pagec):
                print('{0:<10}{1:{3}<12}{2:>8}￥ ×{4:>3}'.format(mycarts[i][0],mycarts[i][1],mycarts[i][2],chr(12288),mycarts[i][3]))
        print('—————————————————————————\n')

def check(): #付款
    if mycart==[]:
        print('当前购物车内没有商品，即将返回菜单。\n')
        time.sleep(2)
        print('使用 /help 指令来查看帮助。\n')
        return 0
    mycarts = sorted(mycart,key= lambda n:n[0])
    print('\n\n—————————————————————————\n                    购物清单')
    print('—————————————————————————')
    print('编号          商品名称                  价格  数量    \n—————————————————————————')
    price = 0
    for i in range(len(mycarts)):
        print('{0:<10}{1:{3}<12}{2:>8}￥ ×{4:>3}'.format(mycarts[i][0],mycarts[i][1],mycarts[i][2],chr(12288),mycarts[i][3]))
        price += mycarts[i][2]*mycarts[i][3]
    print('—————————————————————————\n共需支付：          {:>22}￥(CNY)\n—————————————————————————\n'.format(price))
    print('确认购买请输入： /buy confirm\n取消购买请输入： /buy cancel\n—————————————————————————\n')
    while True:
        msg = input('<Guest> ').lower()
        if msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        elif msg == '/buy confirm':
            print('生成加密订单中，请稍等……\n');time.sleep(random.randint(5,35)/10)
            xiadan(price)
            time.sleep(2)
            mycart.clear()
            mycarts.clear()
            print('使用 /help 指令来查看帮助。\n')
            return 0
        elif msg == '/buy cancel':
            print('已取消购买，即将返回菜单。\n')
            time.sleep(0.5)
            print('使用 /help 指令来查看帮助。\n')
            return 0
        else:
            print('[错误] 请先处理当前进行中的事务！\n')

def admin(): #管理员模式
    print('\n\n\n————————————————————————\n欢迎使用简单购物管理员系统\n')
    print('/findrecord [Code] - 查找订单记录')
    print('/exit - 退出管理员模式\n————————————————————————\n')
    while True:
        msg = (input('<Administrator> ')).lower()
        if msg == '/help' or msg == '/help 1':
            print('\n\n\n————————————————————————\n管理员指令帮助\n')
            print('/findrecord [Code] - 查找订单记录')
            print('/exit - 退出管理员模式\n————————————————————————\n')
        elif msg == '/exit':
            print('正在退出......\n');time.sleep(1)
            print('使用 /help 指令来查看帮助。\n')
            return 0
        elif msg == '/findrecord' or msg == '/findrecord ' or msg == '' or msg[0:1] != '/':
            print('[错误] 格式错误，请检查输入。\n')
        elif len(msg) > 11:
            if msg[:12]=='/findrecord ':
                msgs=msg.split(' ')
                if len(msgs)==2:
                    if is_kazu(msgs[1]):
                        if len(msgs[1]) == 27:
                            print('[系统] 查找记录中，请稍等……\n');time.sleep(0.7)
                            try:
                                findrecord(str(msgs[1]))
                            except:
                                print('[错误] 不支持的订单号！')
                        else:
                            print('[错误] 订单号不正确，请检查输入！\n')
                    else:
                        print('[错误] 订单号格式错误，请检查输入。\n')
                else:
                    print('[错误] 指令格式错误，请检查输入。\n')
            else:
                print('[错误] 格式错误，请检查输入。\n')
        else:
            print('[错误] 未知的指令。\n')
        time.sleep(0.2)


def cartclear(): #清空购物车
    if mycart==[]:
        print('当前购物车内没有商品，即将返回菜单。\n')
        time.sleep(2)
        print('使用 /help 指令来查看帮助。\n')
        return 0
    else:
        print('已清空购物车。\n')
        mycart.clear()

def findrecord(codes): #查找记录
    codefile = open('orderforgoods.txt','a',encoding='utf-8');codefile.close();codefile=open('orderforgoods.txt','r',encoding='utf-8')
    needtofind=codefile.readlines();codefile.close()
    if needtofind == []:
        print('未找到订单数据，还没有任何人下过单，即将返回菜单。\n')
        time.sleep(2)
        print('使用 /help 指令来查看帮助。\n')
        return 0
    for i in needtofind:
        if str(codes) + '\n' == i:
            ms = int(codes[-8:]);ymd=int(codes[:10]);snl=int(codes[10])
            if snl <5:
                pricelock=int(codes[11:-8]);ms//=7;ymd-=ms*600;pricelock=pricelock//3-ms
                fulltime=eval(str(ymd)+'.'+str(ms));gettime=time.localtime(fulltime)
                print('\n\n\n————————————————————————\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n下单金额：{}￥\n————————————————————————\n\n\n'.format(codes, gettime.tm_year, gettime.tm_mon, gettime.tm_mday, gettime.tm_hour, gettime.tm_min, gettime.tm_sec, pricelock))
            else:
                ms//=7;ymd-=ms*600;fulltime=eval(str(ymd)+'.'+str(ms));gettime =time.localtime(fulltime)
                print('\n\n\n————————————————————————\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n该订单为大额单，订单信息以书面形式由顾客和商家共同保存。\n————————————————————————\n\n\n'.format(codes, gettime.tm_year, gettime.tm_mon, gettime.tm_mday, gettime.tm_hour, gettime.tm_min, gettime.tm_sec))
            time.sleep(2)
            print('使用 /help 指令来查看帮助。\n')
            return 0
    else:
        time.sleep(2.6)
        print('[错误] 订单未找到，请检查输入！即将返回菜单。\n')
        time.sleep(1.2)
        print('使用 /help 指令来查看帮助。\n')
        return 0




main() #启动！


# SZPT-BClockraft