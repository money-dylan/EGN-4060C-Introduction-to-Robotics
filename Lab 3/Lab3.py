#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def rotate():
     pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
     rospy.init_node('Lab3')
     rotate_twist=Twist()
     rotate_twist.angular.z = 0.3
     rate=rospy.Rate(10)
     time = 90 * (3.14/180) / rotate_twist.angular.z
     Duration = rospy.Time.now() + rospy.Duration(time)
     print(time)
     print(Duration)
     print(rospy.Time.now())
     while rospy.Time.now() < Duration:
         pub.publish(rotate_twist)
         #print(rospy.Time.now())
         #print(Duration)

     
def go_straight():
     pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
     rospy.init_node('Lab3')
     straight_twist=Twist()
     straight_twist.linear.x = 0.1
     rate=rospy.Rate(10)
     time = 0.5 / straight_twist.linear.x
     Duration = rospy.Time.now() + rospy.Duration(time)
     print(time)
     print(Duration)
     print(rospy.Time.now())
     while rospy.Time.now() < Duration:
         pub.publish(straight_twist)
         #print(rospy.Time.now())
         #print(Duration)
         

if __name__ == '__main__':
    try:
        while True:
            rotate()
            go_straight()
            rotate()
            go_straight()
    except rospy.ROSInterruptException:
        pass
