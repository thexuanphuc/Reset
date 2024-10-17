from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    ld = LaunchDescription([DeclareLaunchArgument(
            'trajectory',
            default_value='circle',
            description='Trajectory type: circle, square, infinity, star'
    )])

    planner_node = Node(
        package='robot_planner',
        executable='planner_sv2',
        name='path_planner',
        output='log',
        parameters=[{'trajectory': LaunchConfiguration('trajectory')}]
    )

    client_node = Node(
        package='robot_planner',
        executable='client',
        name='client_ins',
        output='log',
    )

    server_node = Node(
        package='robot_planner',
        executable='server',
        name='server_ins',
        output='screen',
    )
    simulation_turtle = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim_ins',
        output='screen',
    )

    ld.add_action(planner_node)
    # ld.add_action(client_node)
    ld.add_action(server_node)
    ld.add_action(simulation_turtle)

    return ld