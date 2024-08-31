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
    front_min = min(msg.ranges[300:420])
    left_min = min(msg.ranges[61:180])
    right_min = min(msg.ranges[181:299])
    print("scan elements: %d" % l)
    print("first element: %f" % range_ahead) 
    print("middle element: %f" % msg.ranges[180])
    print("min element: %f" % min(msg.ranges))
    print("numpy mean: %f" % numpy.mean(msg.ranges))
    print("front mean: %f" % numpy.mean(numpy.mean(msg.ranges[0-60]) + numpy.mean(msg.ranges[300-360])))
    print("front min: %f" % front_min)
    print("left mean %f" % numpy.mean(msg.ranges[61-180]))
    print("left min: %f" % left_min)
    print("right mean %f" % numpy.mean(msg.ranges[181 - 299]))
    print("right min %f" % right_min)

    pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
    move_twist=Twist()
    move_twist.linear.x = 0.1
    pub.publish(move_twist)

    back_twist=Twist()
    back_twist.linear.x = -0.1
    back_twist.angular.z = 0.2


    rotate_twist=Twist()
    rotate_twist.linear.x = 0.1
    rotate_twist.angular.z = 0.1

    rotate2_twist=Twist()
    rotate2_twist.linear.x = 0.1
    rotate2_twist.angular.z = -0.1

    if(front_min < 0.3 and front_min < right_min and front_min < left_min):
        pub.publish(back_twist)
    elif(right_min < 0.3 and right_min < front_min and right_min < left_min):
        pub.publish(rotate_twist)
    elif(left_min < 0.3 and left_min < front_min and left_min < right_min):
        pub.publish(rotate2_twist)
    else:
        pub.publish(move_twist)
        
# END MEASUREMENT

rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin()