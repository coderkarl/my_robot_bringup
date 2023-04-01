from launch import LaunchDescription
from launch_ros.actions import Node
from numpy import number
from math import pi

from ament_index_python.packages import get_package_share_directory
import os

from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ld = LaunchDescription()
    
    config_dir = os.path.join(
        get_package_share_directory('my_robot_bringup'),
        'config')
    gps_params = os.path.join(config_dir, 'gps.yaml')
    gps_fusion_node = Node(
        package="mowpi_comm2",
        executable="gps_fusion",
        output="screen",
        emulate_tty=True,
        parameters=[gps_params],
    )

    ld.add_action(gps_fusion_node)
    
    return ld
