#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random


if  __name__ == '__main__':
    pub = rospy.Publisher('smartguys', String, queue_size = 10)
    rospy.init_node('smartguys_node', anonymous=True)
    rate = rospy.Rate(1)


    while not rospy.is_shutdown():
        msg = String()
        msg.data = random.choice(["LOW", "MEDIUM", "HIGH"])
        pub.publish(msg)
        rate.sleep()