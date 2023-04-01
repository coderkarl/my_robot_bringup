"""Launch the ublox gps node with zed-f9p configuration."""

import os

import ament_index_python.packages
import launch
import launch_ros.actions


def generate_launch_description():
    config_directory = os.path.join(
        ament_index_python.packages.get_package_share_directory('my_robot_bringup'),
        'config')
    params = os.path.join(config_directory, 'zed_f9p.yaml')
    ublox_gps_node = launch_ros.actions.Node(package='ublox_gps',
                                             executable='ublox_gps_node',
                                             output='both',
                                             respawn=True,
                                             respawn_delay = 5,
                                             parameters=[params])

    return launch.LaunchDescription([ublox_gps_node])

                                     #launch.actions.RegisterEventHandler(
                                     #    event_handler=launch.event_handlers.OnProcessExit(
                                     #        target_action=ublox_gps_node,
                                     #        on_exit=[launch.actions.EmitEvent(
                                     #            event=launch.events.Shutdown())],
                                     #    )),
                                     #])
