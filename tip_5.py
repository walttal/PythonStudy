
#-*-coding:utf-8-*-
'''

Tip_5.提示输入一个整数(x元),输出这笔钱等于多少张50元，10元，5元，1元纸币（优先用大额纸币）

'''

aNumStr = raw_input("Please input X Yuan:\n")
aNum = int(aNumStr)

Yuan50, Yuan10_tmp = divmod(aNum, 50)
Yuan10, Yuan5_tmp = divmod(Yuan10_tmp, 10)
Yuan5, Yuan1 = divmod(Yuan5_tmp,5)

print("%d Yuan = %d Fifty, %d Ten, %d Five, %d one" % (aNum,Yuan50,Yuan10,Yuan5,Yuan1))







