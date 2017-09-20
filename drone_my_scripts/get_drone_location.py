#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Empty


def callback(data):
    i = data.name.index('quadrotor')
    x = data.pose[i].position.x
    y = data.pose[i].position.y
    z = data.pose[i].position.z
    rx = data.pose[i].orientation.x
    ry = data.pose[i].orientation.y
    rz = data.pose[i].orientation.z
    rw = data.pose[i].orientation.w

    rospy.loginfo("\n x = {} \n y = {} \n z = {} \n"
                  "\n rx = {}\n ry = {}\n rz = {}\n rw = {}".format(i, x, y, z, rx, ry, rz, rw))


def drone_location_listener():
    rospy.init_node('drone_location_listener', anonymous=True)
    rospy.Subscriber("gazebo/model_states", ModelStates, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        drone_location_listener()
    except rospy.ROSInterruptException:
        pass
