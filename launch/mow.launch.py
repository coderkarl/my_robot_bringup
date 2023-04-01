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
    
    rplidar_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                get_package_share_directory('my_robot_bringup') + '/launch/rplidar_a3.launch.py')
    )
    
    ublox_gps_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                get_package_share_directory('my_robot_bringup') + '/launch/ublox_gps_launch.py')
    )
    
    avoid_obs_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                get_package_share_directory('nav_sim') + '/launch/sim_avoid_obstacles2.launch.py')
    )
    
    nxp_node = Node(
        package="nxp_imu",
        executable="nxp_imu",
        output="screen",
        emulate_tty=True,
    )
    
    mowpi_node = Node(
        package="mowpi_comm2",
        executable="mowpi_comm",
        output="screen",
        emulate_tty=True,
    )
    
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
    
    # The map is only published once when activated, and scan_sim_launch misses it
    ld.add_action(rplidar_launch)
    ld.add_action(nxp_node)
    ld.add_action(ublox_gps_launch)
    ld.add_action(mowpi_node)
    ld.add_action(gps_fusion_node)

    #ld.add_action(avoid_obs_launch)
    
    return ld
