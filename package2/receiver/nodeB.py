#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16, Float32

pub = rospy.Publisher('kthfs/result', Float32, queue_size=10) # Publisher initialized as global variable. Not very pretty but faster than writing a class.


def callback(data):
    """Divides the data input by 0.15 and publishes it on the topic 'kthfs/result'.

    Args:
        data (_std_msgs/UInt16): Integer value from the subscriber of topic 'schmidt' that gets processed.
    """
    q = 0.15

    processed = data.data / q
    pub.publish(processed)


def subscriber():
    """Initialization of the node and its subscriber.
    """
    rospy.init_node('nodeB', anonymous=True)

    sub = rospy.Subscriber("schmidt", UInt16, callback)

    rospy.spin()


if __name__ == '__main__':
    subscriber()
