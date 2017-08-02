
#-*-coding:utf-8-*-
'''
Tip_1. 要求输入一个秒数（整数），输出这些秒相当于多少分钟加多少秒，以及相当于多少分钟（带小数）。


Run:
Please input seconds number: 72
72 sec = 1.200000 min
72 sec = 1 min + 12 sec


'''

secInput = raw_input("Please input one seconds: ")
sec = int(secInput)
minFloat = float(sec)/60
minInt, secMod = divmod(sec,60)
print("%d sec = %f min" % (sec,minFloat))
print("%d sec = %d min + %d sec" % (sec, minInt, secMod))
print float(244)/60



