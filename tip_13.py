
# -*-coding:utf-8-*-
'''

Tip 13. Lowest and highest score and average score
'''

aStr = raw_input("Please input a string:\n")
aNumList = [int(item) for item in aStr.split()]
if len(aNumList) <= 3:
    print("Please input at least 3 integer numbers")
else:
    aNumList.sort()
#     aNumList.remove(aNumList[0])
#     aNumList.pop()
    aNumList = aNumList[1:-1]
    aNumListAvg = float(sum(aNumList)) / len(aNumList)
     
    print("The average is: %.2f" % aNumListAvg)


