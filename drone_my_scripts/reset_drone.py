#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


def reset():
    pub = rospy.Publisher("gazebo/set_model_state", ModelState, queue_size=10)
    rospy.init_node('reset', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    msg = ModelState()
    msg.model_name = 'quadrotor'
    msg.pose.position.x = 1
    msg.pose.position.y = 0
    msg.pose.position.z = 2
    msg.pose.orientation.x = 0
    msg.pose.orientation.y = 0
    msg.pose.orientation.z = 0
    msg.twist.linear.x = 0
    msg.twist.linear.y = 0
    msg.twist.linear.z = 0
    msg.twist.angular.x = 0
    msg.twist.angular.y = 0
    msg.twist.angular.z = 0
    msg.reference_frame = 'world'

    pub_twist = rospy.Publisher("cmd_vel", Twist, queue_size=1)
    pub_land = rospy.Publisher("ardrone/land", Empty, queue_size=1, latch=True)

    hover_msg = Twist()
    hover_msg.linear.x = 0
    hover_msg.linear.y = 0
    hover_msg.linear.z = 0
    hover_msg.angular.x = 0
    hover_msg.angular.y = 0
    hover_msg.angular.z = 0
    for i in range(0, 20):
        if not rospy.is_shutdown():
            rate.sleep()
            pub_twist.publish(hover_msg)
            pub.publish(msg)
            pub_land.publish(Empty())


if __name__ == '__main__':
    try:
        reset()
    except rospy.ROSInterruptException:
        pass
