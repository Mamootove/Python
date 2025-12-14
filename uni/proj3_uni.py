#Functions are here!!!
def girande_derakht():
    '''
    (function)
    get the tree's inputes.
    '''
    tree_list =[] 
    print("Do you want to draw your own tree??\nHere you can draw one without doing anything!!\nYour tree has 4 parts, fill the parts and get the tree you wanted!")
    tool_s = (input("Enter the tool of shakhe: "))
    ertefa_s = (input("Enter the ertefa of shakhe: "))
    tool_d = (input("Enter the tool of derakht: "))
    ertefa_d = (input("Enter the ertefa of derakht: "))
    tree_list.append(tool_s)
    tree_list.append(tool_d)
    tree_list.append(ertefa_d)
    tree_list.append(ertefa_s)

    print(f"tree list is {tree_list}")
    
    tree_dict = {}
    tree_dict["tool_d"] = tool_d
    tree_dict["tool_s"] = tool_s
    tree_dict["ertefa_d"] = ertefa_d
    tree_dict["ertefa_s"] = ertefa_s
    
    print(f"tree dict is {tree_dict}")
    
    def regirande_derakht():
        tool_s = (input("reEnter the tool of shakhe: "))
        ertefa_s = (input("reEnter the ertefa of shakhe: "))
        tool_d = (input("reEnter the tool of derakht: "))
        ertefa_d = (input("reEnter the ertefa of derakht: "))
        a= True
        b=True
        c=True
        d=True
        try:
            tool_s = int(tool_s)
        except:
            a =False
        try:
            ertefa_s = int(ertefa_s)
        except:
            b = False
        try:
            tool_d = int(tool_d)
        except:
            c= False
        try:
            ertefa_d = int(ertefa_d)
        except:
            d = False
        if a and b and c and d != True:
            regirande_derakht()
        return tool_s, ertefa_s, tool_d, ertefa_d

    a= True
    b=True
    c=True
    d=True
    try:
        tool_s = int(tool_s)
    except:
        a =False
    try:
        ertefa_s = int(ertefa_s)
    except:
        b = False
    try:
        tool_d = int(tool_d)
    except:
        c= False
    try:
        ertefa_d = int(ertefa_d)
    except:
        d = False
    if a and b and c and d != True:
        regirande_derakht()




    return tool_d, ertefa_d, tool_s, ertefa_s

def girande_goldon():
    '''
    (function)
    get the flowerpot's inputes.
    '''
    tool_g = int(input("Enter the tool of goldon: "))
    ertefa_g = int(input("Enter the ertefa of goldon: "))
    name = input("Enter your full name: ")
    return tool_g, ertefa_g, name
 
def tabdilat(tool_d, ertefa_d, tool_s, ertefa_s, tool_g, ertefa_g, name):
    '''
    (function)
    User may give the even number to function, but in that way we cant draw a nice triangle for the -shakhe- --> even nums turn to previous odd num
    Also prepaires the name and it len for next function>.
    '''
    if tool_s %2 == 1:
        ts = tool_s
    else:
        ts = tool_s -1
    
    if tool_d %2 == 1:
        td = tool_d
    else:
        td = tool_d -1

    if tool_g %2 == 1:
        tg = tool_g
    else:
        tg = tool_g -1
    
    if ertefa_g %2 == 1:
        eg = ertefa_g
    else:
        eg = ertefa_g -1

    len_name = len(name)+2
    real_name = (f"-{name}-")
    real_ertefa_shakhe = int((ts+1)/2)
    #شاید بپرسید ارتفاع واقعی نمنه!
    #پاسخش سادست، اگه دنباله اعداد فردو بنویسید و سعی کنید یه مثلث باهاش بسازید در عمل یه ارتفاع مشخص داره که با دنباله ها در میاد.
    #این ارتفاع بعدا توی درک اینکه چقدر باید هر برای هر سطر فاصله درمظر بگیریم.

    return td, ertefa_d, ertefa_s, tg, eg, real_name, len_name, real_ertefa_shakhe


def hame_kare(td, ertefa_d, ertefa_s, tg, eg, real_name, len_name, real_ertefa_shakhe):
    '''
    (function)
    main function, everything happens here!
    3 main parts, each of them uses the inputes
    '''

    #Shakhe:
    if ertefa_s >= real_ertefa_shakhe:
        for _ in range(ertefa_s - real_ertefa_shakhe):
            print(" "* (real_ertefa_shakhe) + "+")
        for i in range(real_ertefa_shakhe):
            print(" " *(real_ertefa_shakhe - i) + "*" *(i*2 + 1))
    else:
        for i in range(ertefa_s):
            print(" " *(ertefa_s - i) + "*" *((i - ertefa_s + real_ertefa_shakhe)*2 +1))

    #Derakht:
    for i in range(ertefa_d):
        print(" " *(real_ertefa_shakhe - int((td-1)/2)) + "|" *(td))
    
    #Goldon:
    for n in range(int((eg - 1)/2)):
        print(" " *(real_ertefa_shakhe - int((tg-1)/2)) + "#" *(tg))

    print(" " *(real_ertefa_shakhe - int((tg-1)/2)) + "#" *int((tg - len_name)/2), end='')
    print(real_name, end='')
    print("#" *int((tg - len_name)/2))

    for m in range(int((eg - 1)/2)):
        print(" " *(real_ertefa_shakhe - int((tg-1)/2)) + "#" *(tg))



#mokhtasar o mofid, bedon inke barnamamono kasif konim hamaro toye ye khat
hame_kare(*tabdilat(*girande_derakht(), *girande_goldon()))


