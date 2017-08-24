# -*- coding:utf-8 -*-

__author__ = 'wallance'

passwd = 'test'
exit_flag = False
for i in range(3):
    user_input = raw_input("Please input your passwd:").strip()
    if len(user_input) == 0:continue
    if user_input == passwd:
        while True:
            print "welcom login!"
            user_choice = raw_input( '''
                1. run a cmd
                2. send a file
                3. exit this level
                4. exit this whole system 
                ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print "going to run cmd"
            elif user_choice == 2:
                print "going to send a file"
            elif user_choice == 3:
                print "going to exit this level"
                break
            else:
                exit_flag = True
                print "going to exit this whole system"
                break
    else:continue
    if exit_flag:
        break
    print "going to do something else..."

