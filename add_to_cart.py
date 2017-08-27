#-*-coding:utf-8-*-

#Date: 8/27/2017
__author__ = 'Wallance Hou'


products = [["apple",3000],['bike',1900],['Telsa',80000],['Coffee',35],['shoes',599],['brush',29]]
wageStr = raw_input('Please input your wage with integer number:').strip()
if wageStr.isdigit():
    wageInt = int(wageStr)
    cart_list = []
    for index,item in enumerate(products):
        print('[%d] %s: %d yuan/per' % (index,item[0],item[1]))
    print '[x] exit'
    while True:
        user_choice1 = raw_input('Please enter selection:').strip()
        if user_choice1.isdigit():
            user_choice1 = int(user_choice1)
            if user_choice1 >= len(products):
                continue
            if wageInt < products[user_choice1][1]:
                print "Sorry, you balance is not enough."
                continue
            cart_list.append(products[user_choice1])
            wageInt = wageInt - products[user_choice1][1]
            print('Add to cart successfully, your current balance is %d' % wageInt)
        elif user_choice1 == 'x':
                cart_list2 = []
                print '-' * 50 + '\n' + 'Your cart list:\n' + '-' * 50 
                for item in cart_list:
                    if not item in cart_list2:
                        cart_list2.append(item)
                        num = cart_list.count(item)
                        print('%d/%s * %d = %d' % (item[1],item[0],num,item[1] * num))
                print('\nYou balance is %d.' % wageInt)
                break
            
