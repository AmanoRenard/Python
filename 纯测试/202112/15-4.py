a=input()
while a!="0":
    s=[]
    for i in a:
        if i== "(" or i == "{" or i == "[":
            s.append(i)
        elif i== ")":
            try:
                if s[-1] == "(":
                    s.pop()
            except:
                print("false")
                break
        elif i== "]":
            try:
                if s[-1] == "[":
                    s.pop()
            except:
                print("false")
                break
        elif i== "}":
            try:
                if s[-1] == "{":
                    s.pop()
            except:
                print("false")
                break
    else:
        if len(s) != 0:
            print("false")
        else:
            print("true")
    a=input()