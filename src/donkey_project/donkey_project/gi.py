import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ImgRecNode(Node):
    """
    ImgRecNode
    """
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this node is to give gas/brake/steering instruction from the neural network, the rec node will receive the information.")
        self.sub_ = self.create_subscription(String,"This_should_be_an_image",self.recv_callback,10)

    def recv_callback(self,novel):
        self.get_logger().info('ImgRecNode：received：%s' % novel.data)


def main(args=None):
    """
    main functino
    """
    rclpy.init(args=args) # initialize rclpy
    node = ImgRecNode("give")  # create a new node
    rclpy.spin(node) # keep node running, if detected （Ctrl+C）, then exit
    rclpy.shutdown() # rcl closed



