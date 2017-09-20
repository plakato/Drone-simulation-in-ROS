#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from ardrone_autonomy.msg import Navdata

# create publishers
pub_cmd_vel = rospy.Publisher("cmd_vel", Twist, queue_size=1)
pub_takeoff = rospy.Publisher("ardrone/takeoff", Empty, queue_size=1, latch=True)
pub_land = rospy.Publisher("ardrone/land", Empty, queue_size=1, latch=True)
distance_flown = 0
last_timestamp = 0
first_time = True
speeding_const = .01


def fly_forward(x):
    msg = Twist()
    msg.linear.x = x
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.z = 0
    if not rospy.is_shutdown():
        pub_cmd_vel.publish(msg)  # rate.sleep()
    # rospy.loginfo("-----------------FORWARD SPEED {}--------------".format(x))


def takeoff():
    if not rospy.is_shutdown():
        pub_takeoff.publish(Empty())
        # rate.sleep()


def land():
    if not rospy.is_shutdown():
        pub_land.publish(Empty())
        # rate.sleep()


def hover():
    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    if not rospy.is_shutdown():
        pub_cmd_vel.publish(msg)
        # rate.sleep()


def reset():
    pub = rospy.Publisher("ardrone/reset", Empty, queue_size=10)
    for i in range(0, 10):
        if not rospy.is_shutdown():
            pub.publish(Empty())
            rate.sleep()


def initialize_distance_counter():
    rospy.Subscriber("/ardrone/navdata", Navdata, navdata_callback)


# calculates distance flown from velocity
def navdata_callback(data):
    global last_timestamp
    global distance_flown
    global first_time
    if first_time:
        last_timestamp = data.tm
        first_time = False
    velocity = data.vx
    acceleration = data.ax
    delta_time = (data.tm - last_timestamp) / (1000*1000)  # in seconds
    added_distance = (velocity * delta_time - .5*acceleration*(delta_time ** 2)) / 1000  # in meters
    distance_flown += added_distance
    rospy.loginfo(distance_flown)
    last_timestamp = data.tm


if __name__ == '__main__':
    try:
        distance_to_fly = 5.0
        speed = 0
        rospy.init_node('fly_x_meters', anonymous=True)
        rate = rospy.Rate(10)  # 10hz
        initialize_distance_counter()

        # speeding up and flying to midpoint
        while distance_flown < distance_to_fly/2:
            speed += speeding_const
            if speed <= 1:
                takeoff()
                fly_forward(speed)
            else:
                fly_forward(1)

        # speed in the second half is reversed first half
        while speed > 0 and distance_flown < distance_to_fly:
            if speed <= 1:
                fly_forward(speed)
            else:
                fly_forward(1)
            speed -= speeding_const
        fly_forward(0)
        land()
    except rospy.ROSInterruptException:
        pass

# try sleep before publishing + checking for state
