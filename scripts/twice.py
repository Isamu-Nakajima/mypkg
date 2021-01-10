#!/usr/bin/env python3

"""
BSD 3-Clause License
Copyright (c) 2021, Isamu Nakajima and Ryuichi Ueda
All rights reserved.
"""

import rospy
import random
import math
from std_msgs.msg import Int32

n = 0
rou = 1
you = 0
cpu = 0
ydef = 0
cdef = 0
ran = 0
gmo = 0

def cb(message):
    global n
    n = message.data

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(10)

print("数あてゲーム")
print("１から３０までの数字がランダムに選ばれる。")
print("相手より近い数字を出せ。")

while 1:
    print(f"第{rou}回戦")
    def cb(message):
        global n
        n = message.data
    cpu = random.randint(1,30)
    while 1:
        you = input('１から３０の間で数字を決めろ。リタイアなら１３６を:')
        try:
            you = int(you)

        except ValueError:
            you = 0

        if you == 136:
            gmo = 1
            break
        elif you < 1 or you > 30:
            print("違うぞ")
        else:
            break
    if gmo == 1:
        print("GAME　OVER")
        print(f"あなたは{rou - 1}回勝った")
        break
    print(f"相手は{cpu}を選んだ。")
    rospy.sleep(2)
    ran = (n % 30) + 1
    print(f"結果は{ran}だ。")
    ydef = abs(ran - you)
    cdef = abs(ran - cpu)

    if ydef < cdef:
        print("あなたの勝ち。")
        rou = rou + 1
    elif ydef == cdef:
        print("引き分け。もう一度")
    else:
        print("GAME OVER")
        print(f"あなたは{rou - 1}回勝った")
        break

while not rospy.is_shutdown():
    rospy.signal_shutdown('finish')
    rospy.spin()

