#!/usr/bin/env python3

import rospy as ros
from std_msgs.msg import String, Int16



smartguys_data = ""
xs_data = 0

def smartguys(data):
    global smartguys_data
    smartguys_data = data.data

def xs(data):
    global xs_data
    xs_data = data.data
    message()

def message():
    if smartguys_data == "HIGH" and xs_data > 50:
        print("LANCAR")
    elif smartguys_data == "MEDIUM" and xs_data > 50:
        print("PATAH-PATAH")
    elif smartguys_data == "LOW" and xs_data > 50:
        print("NGE-LAG")
    else:
        print("MENDING TURU")


if  __name__ == '__main__':
    ros.init_node('budi_node', anonymous=True)
    ros.Subscriber('smartguys', String, smartguys)
    ros.Subscriber('xs', Int16, xs)
    ros.spin()