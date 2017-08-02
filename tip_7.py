
# -*-coding:utf-8-*-
'''

Tip 7. Check Str you input if including key

'''

aStr = raw_input("Please input a string:\n")
if 'APPLE' in aStr.upper():
    print("'Apple' in '%s'" % (aStr))
else:
    print("'Apple' not in '%s'" % (aStr))






