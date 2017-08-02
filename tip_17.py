
'''

tip_17. shu xiang count

'''

SX_LIST = "shu niu hu tu long she ma yang hou ji gou zhu".split()

aYearNum = int(raw_input("Please input an year:"))

SXIndex = (aYearNum - 1984) % 12

print("ShengXiao: %d => %s" % (aYearNum, SX_LIST[SXIndex]))