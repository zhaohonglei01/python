#coding:utf-8
dict1 = {'abc':456,'bbb':3,1:888}
dict2 = {'abc':123,'bbb':888}
print dict1,dict2,dict2['abc'] #输出时应该用方括号
dict2['abc']=100 #修改字典
print dict2
del dict2['bbb'] #删除字典元素
print dict2
dict1.clear()#删除字典所有条目
print dict1

#两个重要的点需要记住：1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住;
#  2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。因为列表可以update