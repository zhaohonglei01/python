# coding:utf-8
class student:
    __name = 'lily'
    __age = 25
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def __init__(self):
        self.school = 'beijing'
p = student()
print p.getname(),p.getage(),p.school #定义一个对象时，构造函数自动调用
# 用某个对象调用该方法时，就将该对象作为第一个参数传递给self

