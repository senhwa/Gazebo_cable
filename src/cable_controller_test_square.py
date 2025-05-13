#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point
import math
import time

def move_end_sphere():
    '''
    Move the end sphere to the target position
    '''
    # Create a publisher to publish the target position
    pub = rospy.Publisher('cable_target_position', Point, queue_size=10)
    target_position = Point()
    offset = 0.4

    # Go to the first target position

    target_position.x = 0.0
    target_position.y = -0.5
    target_position.z = 1.0
    pub.publish(target_position)

    # Wait for the end sphere to reach the target position
    rospy.sleep(2)

    # Go to the second target position
    target_position.x = 0.0
    target_position.y = -0.5
    target_position.z = 1.0
    pub.publish(target_position)

    # Wait for the end sphere to reach the target position
    rospy.sleep(2)

    # Go to the third target position
    target_position.x = 0.0
    target_position.y = 0.5
    target_position.z = 1.0
    pub.publish(target_position)

    # Wait for the end sphere to reach the target position
    rospy.sleep(2)

    # Go to the fourth target position
    target_position.x = 0.0
    target_position.y = 0.5
    target_position.z = 1.0
    pub.publish(target_position)

    # Wait for the end sphere to reach the target position
    rospy.sleep(2)


if __name__ == "__main__":
    rospy.init_node('move_end_sphere', anonymous=True)
    try:
        rate = rospy.Rate(20)  # 20 Hz
        x = 0.0   # preset x
        z = 1.5    # preset z
        amp = 1.0  # amplitude for y
        freq = 0.05 # frequency in Hz
        start_time = time.time()
        
        pub = rospy.Publisher('cable_target_position', Point, queue_size=10)
        target_position = Point()
        while not rospy.is_shutdown():
            t = time.time() - start_time
            y = amp * math.sin(2 * math.pi * freq * t)
            target_position.x = x
            target_position.y = y
            target_position.z = z
            pub.publish(target_position)
            # move_end_sphere()   
    except rospy.ROSInterruptException:
        pass
