from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                "-file", "/path/to/your/urdf/three_arm_robot.xacro",
                "-entity", "three_arm_robot"
            ],
            output="screen",
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_controller", "--controller-manager", "/controller_manager"],
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_trajectory_controller", "--controller-manager", "/controller_manager"],
        )
    ])
