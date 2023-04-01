from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            node_name='teleop',
            package='turtlesim',
            node_executable='turtle_teleop_key',
            #output='screen',
            remappings = [('/turtle1/cmd_vel', '/cmd_vel')],
        ),
    ])
