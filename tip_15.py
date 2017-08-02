# -*-coding:utf-8-*-
'''

Tip 15. order by alphabetically

'''
aList = []
for i in range(5):
    Input_Str = raw_input("Please input string %d:\t" % i)
    aList.append(Input_Str.strip())

for i in aList:
    if len(i) > 3:
        print i
    