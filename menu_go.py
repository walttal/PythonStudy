# -*- coding:utf-8 -*-

__author__ = 'Wallance Hou'

menu = {
    "Beijing": {
        "ChaoYang": {
            "Wangjing": ['baidu','sina'],
            "xuj": ['baidu','sina']
        },
        "Haidian": ['xiaomi', 'ali']
    },
    "Shanghai": {
        "Pudong": ['jd','bolang'],
        "Xuhui": ['cisco','wenfeng']
    }
}

exit_flag = False
while not exit_flag:
    for index,key in enumerate(menu.keys()):
        print index,key
    user_choice1 = raw_input("Plese select index to enter:").strip()
    if user_choice1.isdigit():
        user_choice1 = int(user_choice1)
        key1 = menu.keys()[user_choice1]
        while not exit_flag:
            for index,key in enumerate(menu[key1]):
                print '-->',index,key
            user_choice2 = raw_input("Plese select index to enter:").strip()
            if user_choice2.isdigit():
                user_choice2 = int(user_choice2)
                key2 = menu[key1].keys()[user_choice2]
                while not exit_flag:
                    for index,key in enumerate(menu[key1][key2]):
                        print '-->-->',index,key
                    user_choice3 = raw_input("Plese select index to enter:").strip()
                    if user_choice3.isdigit():
                        print "this is the last level..."
                    elif user_choice3 == 'quit':
                        exit_flag = True
                    elif user_choice3 == 'back':
                        break
    else:
        print "=====going to quit====="

