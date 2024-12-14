from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                "-file", "/home/ubuntuarm64/ros2_ws/src/three_arm_robot_description/urdf/three_arm_robot.xacro",
                "-entity", "three_arm_robot"
            ],
            output="screen",
        )
    ])
