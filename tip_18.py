
'''

tip_18. encryption string

'''

aStr = raw_input("Please input a string:\n")

aList = [chr(ord(i) + 1) for i in aStr]
bList = [chr(ord(i) - 1) for i in aList]

print('-' * 30)
print("".join(aList))
print("".join(bList))