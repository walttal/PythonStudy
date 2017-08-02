
# -*-coding:utf-8-*-
'''

Tip 9. palindrome check

'''

aStr = raw_input("Please input a string:\n")
aStr = aStr.strip()
aStr_reverse = aStr[::-1]
print len(aStr)
if aStr_reverse == aStr:
    print("%s is a palindrome string" % aStr)
else:
    print("%s is not a palindrome string" % aStr)







