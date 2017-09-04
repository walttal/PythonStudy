# -*- coding:utf-8 -*-

__author__ = 'Wallance Hou'

import pickle,json
import datetime

## dump data to test.pkl
# dict1={'name':'Alex','age':44}
# dict1={'name':'Alex','age':44,'time':datetime.datetime.now()}
# # f=file('test.pkl','w')
# f=file('test.json','w')
# # print pickle.dumps(dict1)
# json.dump(dict1,f)
# f.close()

## restore data
#json not support datetime data
# f = file('test.pkl')
f = file('test.json')
data = json.load(f)
print '-->',data
