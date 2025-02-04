import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry

class OdometrySubscriber(Node):
	def __init__(self):
		super().__init__('odometry_subscriber')
		self.odometry_subscription = self.create_subscription(Odometry, '/localization/kinematic_state', self.odometry_filter, 10)

	def odometry_filter(self, odometry_msg):
		#self.get_logger().info('tf_msg: {}'.format(tf_msg))

		print('odometry_msg: ', odometry_msg.pose.pose)

		# for position - odometry_msg.pose.pose.position
		# for orientation - odometry_msg.pose.pose.orientation

def main(args=None):
	rclpy.init(args=args)
	odometry_subscriber = OdometrySubscriber()
	rclpy.spin(odometry_subscriber)
	odometry_subscriber.destroy_node()
	rclpy.shutdown()
