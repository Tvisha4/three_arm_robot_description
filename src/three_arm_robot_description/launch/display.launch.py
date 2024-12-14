from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('three_arm_robot_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'three_arm_robot.urdf')
    rviz_config_file = os.path.join(pkg_share, 'rviz', 'three_arm_robot.rviz')

    return LaunchDescription([
      
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_file).read()}],
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])