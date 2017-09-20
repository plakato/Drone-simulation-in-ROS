#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelStates

first_time = True
start_pos = None


def callback(data):
    global start_pos
    global first_time
    i = data.name.index('quadrotor')
    if first_time:
        start_pos = data.pose[i].position.x
        rospy.loginfo("START = {}".format(start_pos))
        first_time = False
    else:
        rospy.loginfo("distance from start = {} \n"
                      "START = {} \n NOW = {}"
                      .format(data.pose[i].position.x - start_pos, start_pos, data.pose[i].position.x))


def drone_distance_counter():
    rospy.init_node('drone_distance_counter', anonymous=True)
    rospy.Subscriber("gazebo/model_states", ModelStates, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        drone_distance_counter()
    except rospy.ROSInterruptException:
        pass
