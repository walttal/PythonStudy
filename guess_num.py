# -*- coding:utf-8 -*-

__author__ = 'wallance'
import random

#
# real_num = random.randint(1,10)
real_num = random.randrange(10)
count = 0
# for i in range(3):
while count < 3:
    guess_num = raw_input("Please guess the real number(<10): ").strip()
    if len(guess_num) == 0:
        continue
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print "Oops! You need input a integer number instead of a string!"
        continue
    if guess_num > real_num:
        print "Wrong: greater that real number!"
    elif guess_num < real_num:
        print "Wrong: less that real number!"
    else:
        print "Correct, you got it right!"
        break
    count += 1
else:
    print "Real number is:",real_num

