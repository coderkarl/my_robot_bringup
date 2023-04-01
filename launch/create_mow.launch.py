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
                get_package_share_directory('my_robot_bringup') + '/launch/create_rplidar.launch.py')
    )
    
    nav_states_node = Node(
        package="nav_sim",
        executable="nav_states",
        output='screen',
        emulate_tty='True',
        parameters=[{'plan_rate_hz': 10.0},
                    {'use_PotFields': False},
                    {'close_cone_to_bot_dist': 11.0},
                    {'valid_cone_to_wp_dist': 11.0},
                    {'near_path_dist': 0.1},
                    {'valid_end_of_path_dist': 0.1},
                    {'desired_speed': 0.4},
                    {'slow_speed': 0.3},
                    {'max_omega': 1.0},
                    {'max_fwd_heading_error_deg': 180.0},
                    {'search_time': 2.0},
                    {'search_omega': 0.8},
                    {'reverse_time': 1.0},
                    {'cmd_control_ver': 0},
                    {'scan_collision_db_limit': 4},
                    {'scan_collision_range': 0.3},
                    {'cone_detect_db_limit': 1},
                    {'cmd_speed_filter_factor': 0.5},
                    {'report_bumped_obstacles': True},
                    {'max_camera_search_time': 30.0},
                    {'slow_approach_distance': 0.5},
                    {'reverse_speed': 0.8},
                    {'bump_db_limit': 2},
                    {'path_step_size': 3},
                    {'waypoints_are_in_map_frame': True},
                    
                    {'x_coords':          [0.0, 2.0, 2.0, 0.0]}, # west ***LATEST
                    {'y_coords':          [ 0.0, 0.0, 0.5, 0.5]},
                    
                    {'waypoint_types':     [0,   0,    0]},
                    {'hill_waypoint_list': [0,   0,    0]},
                    {'is_mow_boundary': True},
                    {'mow_ccw': True},
                    {'mow_width': 0.1}, #0.2
                    {'mow_wp_spacing': 0.3},
        ],
        remappings=[('cmd_vel', 'ignore_cmd_vel')]
    )
    
    avoid_obs_node = Node(
        package="nav_sim",
        executable="avoid_obs",
        output='screen',
        emulate_tty='True',
        arguments=['--ros-args', '--log-level', 'info'],
        parameters=[{'plan_rate_hz': 10.0},
                    {'map_res_m': 0.1},
                    {'map_size': 301},
                    {'min_range': 0.1},
                    {'max_range': 4.0},
                    {'min_hill_range': 1.0},
                    {'plan_range': 3.0},
                    {'clear_decrement': -5},
                    {'adjacent_cost_offset': 2.0},
                    {'adjacent_cost_slope': 2.0},
                    {'inflation_factor': 2},
                    {'reinflate_cost_thresh': 30},
                    {'reinflate_radius': 0.4},
                    {'use_PotFields': True},
                    {'cone_search_radius': 0.3},
                    {'cone_obs_thresh': 0},
                    {'max_num_known_obstacles': 30},
                    {'known_obstacle_time_limit': 30.0},
                    {'useLinear': True},
                    {'useTan': True},
                    {'R1': 0.3},
                    {'R2': 0.4},
                    {'Kt': 10.0},
                    {'offset_gamma': pi/2},
                    {'max_heading_error': pi/3},
                    {'Kw': 1.3},
                    {'des_speed': 0.5},
                    {'min_omega': 0.3},
                    {'d_retreat': 0.1},
                    {'goal_thresh': 0.2},
        ]
    )
    
    astar_node = Node(
        package="nav_sim",
        executable="astar",
        output="screen",
        emulate_tty=True,
        parameters=[{'plan_rate_hz': 5.0},
                    {'obs_thresh': 30},
                    {'obs_weight': 0.1},
                    {'max_plan_time_sec': 3.0}
        ]
    )
    
    static_map_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_map_tf',
        arguments=['0.0', '0', '0', '0', '0', '0', 'map', 'odom']
    )
    
    ld.add_action(rplidar_launch)
    ld.add_action(avoid_obs_node)
    ld.add_action(nav_states_node)
    #ld.add_action(astar_node)
    ld.add_action(static_map_tf_node)
    
    return ld
