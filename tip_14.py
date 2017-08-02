
# -*-coding:utf-8-*-
'''

Tip 14. generate a 10000 random list and count

'''
from random import choice

aStr = raw_input("Please input a string:\n")
aNumList = [int(item) for item in aStr.split()]
if len(aNumList) <= 1:
    print("Please input at least 3 integer numbers")
else:
    aRandomList = [choice(aNumList) for i in range(10000)]
    for i in aNumList:
        print("%d => %d" % (i,aRandomList.count(i)))

'''
# for line 15 - 17, which can be replaced with below sentence:
    aRandomList = [choice(aNumList) for i in range(10000)]
    aCountList = [(i,aRandomList.count(i)) for i in aNumList]
    for x,y in aCountList:
        print("%d => %d" % (x,y))
'''
