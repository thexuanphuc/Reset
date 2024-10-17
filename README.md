# Demo ROS2 with Docker

This repository provides a setup for controlling turtlebot with Docker 

## Table of Contents
- [Video demo](#video)
- [Features](#features)
- [Prerequisites](#prerequisites)

## Video
[[DEMO]](https://youtu.be/qM8QbNK3gqI)



## Features

- Docker: Customized image from humble-ros-base(https://hub.docker.com/layers/library/ros/humble-ros-base-jammy/images/sha256-5b530b78b01b3429d086b49a776dc4f5e6240677122d723b8211e6b46d73c471) image for controlling turtlebot.
- Volume Mounting: Copy source from local workspace into the Docker container.
- **GUI turtlesim**: I was tired of fixing compatibility issues with monitor and Docker, so I decided to use simulation turtlebot on my local machine instead.

## Prerequisites
- [Docker 24.0.5](https://www.docker.com/get-started) + [Docker Compose v2.20.3](https://docs.docker.com/compose/install/)
- [ROS2 Humble] (https://docs.ros.org/en/humble/Installation.html).
