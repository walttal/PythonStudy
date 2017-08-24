# -*- coding:utf-8 -*-

__author__ = 'wallance'

data = {
    'name':'alex',
    'age':18,
    'job':'CEO'
}
data['salary']=15000
del data['job']
# data.clear()  #clear all key,value
# print data
#ergodic dict method 1
# for key in data:
#     print key,data[key]
# #ergodic dict method 2
# for key,val in data.items():
#     print key,val
#NOTES: method 1 is more efficient than method 2

if data.has_key("info"):
    print data["info"]

print data.get("info",[]) #no vlaue, then print [] null list

