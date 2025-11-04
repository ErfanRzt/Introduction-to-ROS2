import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('rpros2_week2_assignment'),
        'config',
        'wheel2robot_service_params.yaml'
        )

    return LaunchDescription([
        Node(
            package='rpros2_week2_assignment',
            executable='wheel2robot_vel_server',
            name='wheel2robot_velocity_server',
            parameters=[
                config
            ]
        )
    ])