# ros2 robot rpi4 setup

## ros2 packages from apt
irobot_create_msgs joy pointcloud_to_laserscan slam_toolbox

## ldlidar_stl_ros2

## mowpi_comm2

## my_interfaces

## my_robot_bringup

## nav_sim
branch ros2
git remote set-url origin https://github.com/coderkarl/nav_sim.git

## nxp_imu
ros2 run nxp_imu nxp_imu
sudo apt install python3-smbus2
pip install smbus2
pip3 install smbus2
ros2 run nxp_imu nxp_imu
sudo adduser ubuntu i2c
ros2 run nxp_imu nxp_imu
sudo chmod a+rw /dev/i2c-1

## openni2_camera
git clone https://github.com/mikeferguson/openni2_camera.git

## rplidar_ros

## ublox ublox_gps ublox_msgs

## v4l2_camera

## zumo_serial_comm


# Network
`sudo nano /etc/netplan/50-cloud-init.yaml`  

# Misc
timedatectl set-timezone America/Chicago

# udev rules
udevadm info -n /dev/ttyACM0 -a -p
sudo nano /etc/udev/rules.d/97-usb-serial.rules
sudo udevadm control --reload-rules && udevadm trigger

97-usb-serial.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DO008OAY", SYMLINK+="sweep"
SUBSYSTEM=="tty", ATTRS{idVendor}=="239a", ATTRS{idProduct}=="800c", SYMLINK+="mowpi_feather"
SUBSYSTEM=="tty", ATTRS{idVendor}=="1546", ATTRS{idProduct}=="01a8", SYMLINK+="gps"
SUBSYSTEM=="tty", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="0001", SYMLINK+="rplidarA3"

ldlidar.rules
KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE:="0777", SYMLINK+="ldlidar"

# Past relevant bash history
colcon build --symlink-install --packages-select nav_sim --cmake-args ' -DCMAKE_BUILD_TYPE=Release'

ros2 service call /reset_pose irobot_create_msgs/srv/ResetPose	

sudo apt install build-essential
colcon build --symlink-install --packages-select openni2_camera_msgs
colcon build --symlink-install
sudo apt install boost1.71
sudo apt install boost1.67
sudo apt install libboost-dev
sudo apt install libboost-all-dev
colcon build --symlink-install
sudo apt install ros-foxy-camera-info-manager
sudo apt install ros-foxy-image-transport
sudo apt install ros-foxy-sensor-msgs
colcon build --symlink-install
sudo apt install libopenni2-dev
colcon build --symlink-install
sudo apt install ros-foxy-std-msgs
sudo apt install ros-foxy-desktop

sudo rosdep init
sudo apt install python-rosdep
sudo apt update
cd ~
sudo apt install python-rosdep
ping google.com
sudo apt install python3-rosdep
cd ros2_ws/
sudo rosdep init
rosdep update
sudo apt update
rosdep install -y --from-paths src --ignore-src

sudo dphys-swapfile swapoff
swapoff
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
top
sudo swapon /swapfile
sudo nano /etc/fstab
top
cat /proc/sys/vm/swappiness

sudo apt install ros-foxy-rosbag2-transport

# rpi camera
ros2 run raspicam2 raspicam2_node --ros-args --params-file `ros2 pkg prefix raspicam2`/share/raspica>
rpi-update
sudo curl -L --output /usr/bin/rpi-update
sudo curl -L --output /usr/bin/rpi-update https://raw.githubusercontent.com/Hexxeh/rpi-update/master>
sudo chmod +x /usr/bin/rpi-update
sudo rpi-update
ros2 run raspicam2 raspicam2_node --ros-args --params-file `ros2 pkg prefix raspicam2`/share/raspica>
wget <https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20211019_all.deb>>
wget <https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20221214_all.deb>>
wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20221214_all.deb ->
sudo apt -y install libnewt0.52 whiptail parted triggerhappy lua5.1 alsa-utils
sudo apt install -fy
dkpg -i archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20221214_all.deb
dpkg -i archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20221214_all.deb
sudo dpkg -i archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20221214_all.deb
sudo raspi-config
ros2 run raspicam2 raspicam2_node --ros-args --params-file `ros2 pkg prefix raspicam2`/share/raspica>
sudo nano /boot/config.txt
ros2 run raspicam2 raspicam2_node --ros-args --params-file `ros2 pkg prefix raspicam2`/share/raspica>
sudo apt update
