import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PuberNode(Node):
    """
    create the node
    """
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("This is image-collecting node and publish images. give_node will subscribe this and give instructions based on the images" )
        # 2.create and initialize the property pub image
        self.pub_image = self.create_publisher(String,"This_should_be_an_image", 10) 

        #3. publishing logic
        # this is a timer
        self.i = 0 # i calculate the publishing freqeuncy
        timer_period = 0.1  #every 0.1s pub an image 
        self.timer = self.create_timer(timer_period, self.timer_callback)  #time_callback function


    def timer_callback(self):
        """
        callback function
        """
        msg = String()
        msg.data = 'number %d and number %d publishing image' % (self.i,self.i)
        self.pub_image.publish(msg)  #publish images
        self.get_logger().info('publishing images："%s"' % msg.data)    #print the log
        self.i += 1 # +1
    
def main(args=None):
    rclpy.init(args=args)
    pub_node=PuberNode("pub")
    rclpy.spin(pub_node)
    rclpy.shutdown()
