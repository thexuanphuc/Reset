import rclpy
import math
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String


class PathPlanner(Node):

    def __init__(self, trajectory):
        super().__init__('path_planner')
        start_time = 0.0
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.create_subscription(String, '/mode_topic', self.mode_callback, 10)

        # Trajectory parameter
        self.trajectory = trajectory

        self.linear_speed = 1.0  # meters per second
        self.angular_speed = 1.0  # radians per second

    def pose_callback(self, msg:Pose):
        self.current_position = [msg.x, msg.y, msg.theta]  # update current position

    def mode_callback(self, msg:String):
        self.trajectory = msg.data
        # Move the robot based on the current trajectory
        if self.trajectory == "circle":
            self.move_in_circle()
        elif self.trajectory == "square":
            self.move_in_square()
        elif self.trajectory == "infinity":
            self.move_in_infinity()
        elif self.trajectory == "star":
            self.move_in_star()
        # self.get_logger().info(f'Drawed: {self.trajectory}')


    def move_in_circle(self):
        self.get_logger().info(f'moving in Circle trajectory')
        # Movement logic for circle trajectory
        self.vel_msg = Twist()
        self.vel_msg.linear.x = self.linear_speed
        self.vel_msg.angular.z = self.angular_speed

        # Calculate the time to complete one circle
        radius = self.linear_speed / self.angular_speed
        circumference = 2 * math.pi * radius
        duration = circumference / self.linear_speed

        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub_.publish(self.vel_msg)
            time.sleep(0.01)  # 100Hz

        # Stop the robot after completing the circle
        self.vel_msg.linear.x = 0.0
        self.vel_msg.angular.z = 0.0
        self.cmd_vel_pub_.publish(self.vel_msg)
        

    def move_in_square(self):
        self.get_logger().info(f'moving in Square trajectory')
        # Movement logic for square trajectory
        for _ in range(4):
            self.move_forward(4.0)
            self.rotate(math.pi / 2)
        

    def move_in_infinity(self):
        self.get_logger().info(f'moving in Infinity trajectory')
        # Movement logic for infinity trajectory (two circles)
        for _ in range(2):
            self.move_in_circle()
            self.rotate(math.pi)

    def move_in_star(self):
        self.get_logger().info(f'moving in Star trajectory')
        # Movement logic for star trajectory with 5 wings
        for _ in range(5):
            self.move_forward(3.0)
            self.rotate(0.8 * math.pi)  # (180-36) degrees)
            
    
    # handle moving by position 
    def move_forward(self, distance):
        duration = distance / self.linear_speed
        velocity_msg = Twist()
        velocity_msg.linear.x = self.linear_speed
        velocity_msg.angular.z = 0.0
        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub_.publish(velocity_msg)
            time.sleep(0.01) # 100Hz
        velocity_msg.linear.x = 0.0
        self.cmd_vel_pub_.publish(velocity_msg)


    def rotate(self, angle):
        duration = abs(angle) / self.angular_speed
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.0
        velocity_msg.angular.z = self.angular_speed if angle > 0 else -self.angular_speed
        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub_.publish(velocity_msg)
            time.sleep(0.01)  # 100Hz
        velocity_msg.angular.z = 0.0
        self.cmd_vel_pub_.publish(velocity_msg)


def main(args=None):
    rclpy.init(args=args)
    trajectory = "circle"  # Default value
    path_planner = PathPlanner(trajectory)
    rclpy.spin(path_planner)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
