
'''

tip_16. input a int number, output the number less than its power

'''
from math import ceil

aNum = int(raw_input("Please input a int num:"))
aList = [str(i ** 2) for i in range(1, int(ceil(aNum ** 0.5)))]

print("Numbers: %s" % " ".join(aList))   
    
    