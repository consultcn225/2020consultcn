 #tempconvert.py
tempstr=input("请输入带有符号的温度值:")
if tempstr[-1]in['F','f']:
    C=(eval(tempstr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}c".format(C))
elif tempstr[-1]in['C','c']:
    F=1.8*eval(tempstr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
    
