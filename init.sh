#!/bin/bash

# build packages
source /opt/ros/humble/setup.sh
colcon build --packages-select rbpler_interfaces
source /opt/ros2_ws_1710/install/setup.sh
colcon build --packages-select robot_planner
source /opt/ros2_ws_1710/install/setup.sh

# Launch the robot planner
ros2 launch robot_planner test2.launch.py &
ros2 run robot_planner client
