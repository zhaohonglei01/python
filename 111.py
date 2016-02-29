#coding:utf-8

def add(a,b):
    c=a+b
    print c

print add(1,2) #3是调add（1，2）输出的；print add（1,2）根本不会输出值，因为函数没有返回给它值，函数中用个return就可以了。