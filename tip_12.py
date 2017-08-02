
# -*-coding:utf-8-*-
'''

Tip 12. count string
'''

aStr = raw_input("Please input a string:\n")
aStr = aStr.strip()
aCount = aStr.lower().count('a')
aFirstIndex = aStr.lower().find('a')

print("String '%s' has %d a(or A), first a(or A) in %d" % (aStr, aCount, aFirstIndex))



