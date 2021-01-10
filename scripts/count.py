#!/usr/bin/env python3

"""
BSD 3-Clause License
Copyright (c) 2021, Isamu Nakajima and Ryuichi Ueda
All rights reserved.
"""

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
