#-*- coding:utf-8 -*-
#Date: 9/5/2017
__author__ = 'Wallance Hou'


data_list = range(0,1000000,2)

def binary_search(find_num,data):
    mid = len(data)/2
    if mid > 0:
        if find_num > data[mid]:
            # print "data should be in right", mid, data[mid:]
            print "data should be in right", mid
            binary_search(find_num,data[mid:])
        elif find_num < data[mid]:
            # print "data should be in left", mid, data[:mid]
            print "data should be in left", mid
            binary_search(find_num,data[:mid])
        else:
            print "\033[32;1mfind the num: %s\033[0m" % data[mid]
    elif data[0] == find_num:
        print "\033[32;1mfind the num:%s\033[0m" % data[mid]
    else:
        print "\033[31;1mcan't find the num\033[0m", find_num

if __name__ == '__main__':
    find_n = raw_input('Please input num you want to find:').strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_search(find_n,data_list)

