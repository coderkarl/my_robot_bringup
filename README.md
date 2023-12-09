# My Robot Bringup launch and config files

## Mower bringup  
### packages:  
[my\_robot\_bringup](https://github.com/coderkarl/my_robot_bringup.git) branch: main  
[mowpi\_comm2](https://github.com/coderkarl/mowpi_comm2.git) branch: mowpi\_gps  
[nav\_sim](https://github.com/coderkarl/nav_sim.git) branch ros2\_mow\_sim  

### launch Option 1:  
`ros2 launch my_robot_bringup rplidar_a3.launch.py`  
`ros2 launch my_robot_bringup mow.launch.py`  
(Remove rplidar\_launch and avoid\_obs\_launch)  
`ros2 launch nav_sim sim_avoid_obstacles2.launch.py`  

### Nodes
rplidar\_ros rplidar\_composition  
ublox\_gps ublox\_gps\_node  
nav\_sim nav\_states (mow area coordinates)  
nav\_sim avoid\_obs (potential fields)  
nav\_sim astar (optional)  
tf2\_ros static\_transform\_publiser (map to odom)  

nxp\_imu nxp\_imu  
mowpi\_comm2 mowpi\_comm  
mopi\_comm2 gps_fusion  

## Services  
https://www.howtogeek.com/devops/how-to-add-your-own-services-to-systemd-for-easier-management/  
Put the .service files in /etc/systemd/system/  
`sudo systemctl daemon-reload`  
To run the service on startup: `sudo systemctl enable myservice`  
