#!/usr/bin/env python3

import rospy
import os
from geometry_msgs.msg import Twist

def mover():
     pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
     rospy.init_node('moveturtlefwd')
     straight_twist=Twist()
     straight_twist.linear.x=1
     #straight_twist.angular.z=2
     turn_twist=Twist()
     #straight_twist.linear.x = 1
     turn_twist.linear.x=1
     turn_twist.angular.z= 2
     rip_twist=Twist()
     rip_twist.linear.x=1
     rip_twist.angular.z=-0.8
     rate=rospy.Rate(10)
     change_time=rospy.Time.now()
     turning=0
     while not rospy.is_shutdown():
       if turning == 1:
       	os.system('rosservice call /turtle1/set_pen 255 0 255 3 0')
       	pub.publish(turn_twist)
       if turning == 2:
       	os.system('rosservice call /turtle1/set_pen 69 86 255 3 0')
       	pub.publish(straight_twist)
       if turning == 3:
       	os.system('rosservice call /turtle1/set_pen 255 0 255 3 0')
       	pub.publish(rip_twist)
       if turning == 4:
       	os.system('rosservice call /turtle1/set_pen 69 86 255 3 0')
       	pub.publish(straight_twist)
       if turning == 5:
       	os.system('rosservice call /turtle1/set_pen 255 0 255 3 0')
       	pub.publish(turn_twist)

       if rospy.Time.now() > change_time:
          turning += 1
          change_time=rospy.Time.now() + rospy.Duration(3)
       rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
