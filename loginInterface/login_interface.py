# -*- coding:utf-8 -*-
'''
Login interface, check if input password failure more than 3 times, then lock this user
'''
pass_file = open("pass.txt")
pass_file = pass_file.read().strip()
username = pass_file.split(":")[0].strip('!')
password = pass_file.split(":")[1]


count = 0
login_success = False
while True:
    userName = raw_input("Username: ").strip()
    if userName == username:
        if pass_file[0] == "!":
            print "Your password has been locked, please contact your administrator!"
            break
        while count < 3:
            userPass = raw_input("Password: ").strip()
            if userPass == password:
                print "Welcome to login!"
                login_success = True
                break
            else:
                print "Wrong password!"
                count += 1
                continue

        if count == 3:
            print "Your password has been locked, please contact your administrator!"
            with open('pass.txt', 'r+') as f:
                old = f.read()
                f.seek(0)
                f.write("!" + old)
                f.close()
            break
    else:
        print "user does not exist"
        continue
    if login_success:
        break
