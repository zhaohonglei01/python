#coding:utf-8
for i in range(1,5):
    print i
for j in range(1,10,3):
    print j


# range(10),等于[0,1,2,3,4,5,6,7,8,9]
# range(1,9),等于[1,2,3,4,5,6,7,8]
# range(1,9,2),等于[1,3,5,7]


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                print i,j,k

# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

str = input("请输入：");
print "你输入的内容是: ", str