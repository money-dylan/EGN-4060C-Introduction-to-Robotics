#!/usr/bin/env python3
import rospy
import math
import numpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def scan_callback(msg):
    l=len(msg.ranges)
    print(msg.ranges)
    range_ahead = msg.ranges[0]
    print("scan elements: %d" % l)
    print("first element: %f" % range_ahead) 
    print("middle element: %f" % msg.ranges[180])
    print("min element: %f" % min(msg.ranges))
    print("numpy mean: %f" % numpy.mean(msg.ranges))

    pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
    move_twist=Twist()
    move_twist.linear.x = 0.1
    pub.publish(move_twist)

    back_twist=Twist()
    back_twist.linear.x = -0.1

    rotate_twist=Twist()
    rotate_twist.angular.z = 0.1

    if(min(msg.ranges) <= 0.3):
        pub.publish(back_twist)
        
# END MEASUREMENT

rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin()