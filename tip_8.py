
# -*-coding:utf-8-*-
'''

Tip 8. Deal with multi-space and change first letter to upper

'''

aStr = raw_input("Please input a string:\n")

aStrTitle = aStr.title()
aStrList = aStrTitle.split()
aStrNew = " ".join(aStrList)

print aStrNew






