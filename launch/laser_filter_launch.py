from launch import LaunchDescription
from launch_ros.actions import Node
from numpy import number

def generate_launch_description():
    ld = LaunchDescription()
    
    scan_to_cloud = Node(
        package="pointcloud_to_laserscan",
        executable="laserscan_to_pointcloud_node",
        name="scan_to_cloud",
        remappings=[ ("scan_in", "scan")],
        parameters=[{'target_frame': "base_link"},
                    {'use_sim_time': True} ]
    )
    
    cloud_to_scan = Node(
        package="pointcloud_to_laserscan",
        executable="pointcloud_to_laserscan_node",
        name="cloud_to_scan",
        remappings=[
            ("cloud_in", "cloud"),
            ("scan", "scan_high")
        ],
        parameters=[{'min_height': -0.2},
                    {'max_height': 5.0},
                    {'angle_min': -3.14159},
                    {'angle_max': 3.14159},
                    {'angle_increment': 3.14159/180},
                    {'transform_tolerance': 0.1},
                    {'range_min': 0.3},
                    {'range_max': 25.0},
                    {'use_inf': True},
                    {'use_sim_time': True}
        ]
    )
    
    remap_number_topic = ("number", "my_number")
    
    number_publisher_node = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_num_pub",
        remappings=[
            remap_number_topic
        ],
        parameters=[
            {"num_to_pub": 4, "freq_hz": 0.5}
        ]
    )
    
    counter_node = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="num_counter",
        remappings=[
            remap_number_topic,
            ("number_count", "my_number_count")
        ]
    )
    
    ld.add_action(scan_to_cloud)
    ld.add_action(cloud_to_scan)
    
    return ld
