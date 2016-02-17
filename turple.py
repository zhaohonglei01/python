#coding:utf-8
a = b = c = 1 #多重赋值
d= 'john'
print a,b,c,d

x,y,z=1,2,3 #多元赋值
print x,y,z

tuple = ('haha',123,'heihei',888) #元组是另一个数据类型，类似于List（列表）。元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表
tinytuple = (1,"welcome to china")
print tuple
print tuple[2]
print tuple[1:3] # 输出第二个至第三个的元素       print tuple + "welcome to china" #字符串可以这样输出，元组不可以
print tuple + tinytuple #打印组合的元组

#元组中的元素值不能修改和删除
#元组运算符&列表运算符

#Python支持四种不同的数值类型：
#int（有符号整型）
#long（长整型[也可以代表八进制和十六进制]）
#float（浮点型）
#complex（复数）

#Python有五个标准的数据类型：
#Numbers（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Dictionary（字典）
