#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose, Twist, PoseStamped, TwistStamped
from sensor_msgs.msg import CompressedImage, LaserScan, JointState

def scan_callback(self, msg):
    print(msg)


def laser_scan():
    rospy.init_node('laser_scan',anonymous = True)
    rospy.Subscriber("/base_scan", LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    laser_scan()
    





