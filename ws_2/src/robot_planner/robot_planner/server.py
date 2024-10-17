import rclpy
from rclpy.node import Node
from rbpler_interfaces.srv import SetString
from std_msgs.msg import String

class MyServiceServer(Node):
    def __init__(self):
        self.valid_trajectories = ["circle", "square", "infinity", "star"]
        self.pre_mode = None
        super().__init__('my_service_server')
        self.srv_ = self.create_service(SetString, 'set_mode', self.set_mode_callback)
        self.mode_publisher_ = self.create_publisher(String, "/mode_topic", 10)

    def set_mode_callback(self, request, response):
        self.get_logger().info(f'Received request: mode={request.data}\n')
        msg1 = String()
        if request.data == self.pre_mode:
            response.success = False
            response.message = "Mode already set \n"
            self.get_logger().warn("Mode already set! \n")
        else:
            if request.data in self.valid_trajectories:
                response.success = True
                response.message = f"Mode set to {request.data} \n"
                self.get_logger().info(f"Mode set to: {request.data} \n")
                msg1.data = str(request.data)
                self.mode_publisher_.publish(msg1)
                self.pre_mode = msg1.data

            else:
                response.success = False
                response.message = "Invalid mode \n"
                self.get_logger().warn("Invalid mode entered! \n") 
        
        return response 


def main(args=None):
    rclpy.init(args=args)
    server_ins = MyServiceServer()
    rclpy.spin(server_ins)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
