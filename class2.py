# coding: utf-8
class student:
    __name = 'lily'
    __age = 25
a = student()
print a.__name,a.__age
#属性前加2个_，说明是私有属性
#类内部定义的私有属性，不能在类外部调用
#类属性和实例属性。实例属性是不需要在类中显示定义的