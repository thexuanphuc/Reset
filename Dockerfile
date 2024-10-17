FROM ros:humble-ros-base-jammy

### Customizations Start Here ###

# Set environment variables for non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive
ENV AMENT_CPPCHECK_ALLOW_SLOW_VERSIONS=1

RUN apt-get update && apt-get install -y --no-install-recommends \
  bash-completion \
  build-essential \
  cmake \
  # gdb \
  # openssh-client \SHELL ["/bin/bash", "-c"]
  # python3-argcomplete \
  python3-pip \
  ros-humble-ament-* \
  ros-humble-ament-cmake \
  ros-humble-turtlesim \
  # ros-humble-ament-cmake-clang-format \
  && rm -rf /var/lib/apt/lists/*

RUN export CMAKE_PREFIX_PATH=/opt/ros/humble:ament_cmake
RUN . /opt/ros/humble/setup.sh

# Copy the ROS2 workspace into the container
RUN mkdir -p /opt/ros2_ws_1710/src/
COPY ./ws_2/src /opt/ros2_ws_1710/src/

# Set the working directory to the ROS2 workspace
WORKDIR /opt/ros2_ws_1710/
RUN sudo chmod 777 -R .
COPY init.sh .
RUN chmod +x init.sh
CMD ["./init.sh"]

