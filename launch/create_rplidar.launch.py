from launch import LaunchDescription
from launch_ros.actions import Node
from math import pi


def generate_launch_description():
    return LaunchDescription([
        Node(
            name='rplidar_composition',
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 256000,  # A3
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Stability',
            }],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_laser_tf',
            # x y z yaw pitch roll frame_id child_frame_id period_in_ms
            arguments=['-0.036', '0.052', '0', '3.14159', '0', '0', 'base_link', 'laser']
        ),
    ])
