import time

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node


class Rotator(Node):
    def __init__(self):
        super().__init__('rotate')
        self._cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def rotate_forever(self):
        twist = Twist()
        while rclpy.ok():
            twist.angular.z = 0.1
            self._cmd_pub.publish(twist)
            self.get_logger().info('Rotating robot: {}'.format(twist))
            time.sleep(0.1)


def main(args=None):
    rclpy.init(args=args)
    rotator = Rotator()
    rotator.rotate_forever()


if __name__ == '__main__':
    main()
