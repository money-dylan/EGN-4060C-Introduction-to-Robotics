#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped

# Step 1: Initialize a node
rospy.init_node('go_to_goal')


# Step 2: Create a publisher that publishes PoseStamped messages to /movei_base_smple/goal topic

pub=rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)

rospy.sleep(3)
goal = PoseStamped()
goal.header.frame_id = "map"
goal.header.stamp = rospy.Time.now()
goal.pose.position.z = 0

try:
	while True:

        # Step 3: Take the destination corrdinates X and Y as inputs from the user
		x = float(input('Enter X coordinate'))
		y = float(input('Enter Y coordinate'))

        # Step 4: Set goal.pose.position for x, y, and w
		goal.pose.position.x = x
		goal.pose.position.y = y


		goal.pose.orientation.w = 1.0

        # Step 5: Publish the goal message using the publisher that you created in step 2
		pub.publish(goal)

		rospy.sleep(1)
        
except KeyboardInterrupt:
	pass