#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
     pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
     rospy.init_node('Lab3')
     rotate_twist=Twist()
     rotate_twist.angular.z = 0.4
     rotate_twist.linear.x = 0.1
     pub.publish(rotate_twist)
         #print(rospy.Time.now())
         #print(Duration)

if __name__ == '__main__':
    try:
        while True:
            circle()
  
    except rospy.ROSInterruptException:
        pass
