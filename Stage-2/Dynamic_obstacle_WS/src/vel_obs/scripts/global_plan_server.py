#!/usr/bin/env python2 

import rospy
from rbe500_project.srv import rrpIKResponse, rrpIKRequest, rrpIK
from math import sqrt, atan2

def ik_cb(req):
    l0 = 0.05
    l1 = 0.45
    l2 = 0.425
    l3 = 0.345
    l4 = 0.11
    
    x = req.x
    y = req.y
    z = req.z
    
    q3 = l0 + l1 - l4 - z
    cos_theta2 = (x**2 + y**2 - l2**2 - l3**2)/(2*l2*l3)
    cos_theta2 = round(cos_theta2, 3)
    sin_theta2 = sqrt(1-cos_theta2**2) # + or - 
    theta2 = atan2(sin_theta2, cos_theta2)
    
    # cos_theta1 = ((l2 + l3*cos_theta2)*x - l3*sin_theta2*y)/(x**2 + y**2)
    # sin_theta1 = ((l2 + l3*cos_theta2)*y - l3*sin_theta2*x)/(x**2 + y**2)
    # theta1 = atan2(sin_theta1/cos_theta1, 1)
    
    theta1 = atan2(y, x) - atan2(l3*sin_theta2, l2 + l3*cos_theta2)
    
    response = rrpIKResponse()
    response.q1 = theta1
    response.q2 = theta2
    response.q3 = q3
    return response

if __name__ == "__main__":
    rospy.init_node("ik_server")

    rospy.Service("ik_server/ik", rrpIK, ik_cb)
    rospy.spin()