import rclpy
from rclpy.node import Node
from rbpler_interfaces.srv import SetString

class MyServiceClient(Node):
    def __init__(self):
        super().__init__('my_service_client')
        self.client = self.create_client(SetString, 'set_mode')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = SetString.Request()

    def send_request(self, data):
        self.req.data = data
        future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    client_ins = MyServiceClient()

    while True:
        user_input = input("Enter a string to send mode to the server (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = client_ins.send_request(user_input)
        client_ins.get_logger().info(f'Response: success={response.success}, message={response.message}')
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()