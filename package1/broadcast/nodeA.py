#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16


def publish():
    """Publishes a number k increasing interatively by 4 at 20hz on the topic 'schmidt'."""
    pub = rospy.Publisher('schmidt', UInt16, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20)

    k = 0

    while not rospy.is_shutdown():
        k += 4
        pub.publish(k)
        rate.sleep()


if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
