# ROS2 Point Cloud Clustering and Segmentation for Autonomous Vehicles
ROS2 Point Clouds For Autonomous Self Driving Car using PCL. This repository helps you understand and learn usage of point clouds in autonomous vehicles.

It covers the basics of point clouds, including what they are, how they are created, and how they can be represented. The Point Cloud Library (PCL), a popular open-source library for processing point clouds. I learned how to create and run ROS2 nodes, use the PCL (Point Cloud Library) library, perform RTAB mapping (Real-Time Appearance-Based Mapping), and apply segmentation and clustering techniques.

The next few sections focuses on using PCL to process point clouds for autonomous vehicles. We will learn how to filter point clouds, segment point clouds, and cluster point clouds. We will also learn how to use PCL to create 3D maps and to track objects in the environment.

The final section covers the Kitti dataset, a large dataset of 3D lidar data. We will learn how to use the Kitti dataset to train and evaluate object detection algorithms.

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
  </ol>
</details>

## About this Repository
This is repository for the course **ROS2 Point Clouds For Autonomous Self Driving Car using PCL** availble at Udemy . Complete source code is open sourced.

 ![alt text](https://github.com/roniepatil/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Vehicles/blob/main/image_resources/main_cover.png)

----
## Using this Repository
* Move into your workspace/src folder
 ```
 cd path/to/ros2_ws/src/
##e.g cd ~/ros2_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/roniepatil/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Vehicles.git
```

* Perform make and build through colcon
 ```
 cd /path/to/workspace_root/
 ##e.g ~/ros2_ws/
 colcon build
 ```

* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/ros2_ws/install/setup.bash
```
- Make sure kitti data is in *~/ros2_ws/data*
- Build Kitti Data Processing and run it
```
colcon build && ros2 launch  point_cloud_processing process_kitti.launch.py
```
- Run Rviz with config file
```
ros2 launch  point_cloud_processing bring_rviz.launch.py
```


---
## Features
* **Building Point Cloud Maps with RTAB-Map**
  -  ![alt text](https://github.com/roniepatil/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Vehicles/blob/main/image_resources/rtabmap.gif)
* **Processing Kitti Dataset**
  - ![alt text](https://github.com/roniepatil/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Vehicles/blob/main/image_resources/kitti.gif)



----
## Requirments

**Software Based**
* Ubuntu 22.04 (LTS)
* ROS2 - Humble


## Extra - commands

export AMENT_PREFIX_PATH=''

sudo apt install libpcl-dev

sudo apt-get install ros-humble-pcl-ros

sudo apt-get install ros-humble-pcl-conversions

sudo apt install pcl-tools

Extras:

sudo apt install python3-colcon-clean

colcon clean workspace


colcon build

ros2 pkg create --build-type ament_cmake point_cloud_processing

colcon build --packages-select point_cloud_processing

pcl_viewer table_scene.pcd

ros2 run point_cloud_processing pcd_import

ros2 run point_cloud_processing plane_cloud

pcl_viewer -multiview 2 plane.pcd plane_.pcd

EXTRA

sudo apt remove libgazebo11

sudo apt remove libgazebo-dev

sudo apt remove 

sudo apt install ros-humble-gazebo-ros-pkgs

sudo apt install ros-humble-rtabmap-ros

sudo apt install python3-opencv

sudo apt install libopencv-dev


ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

ros2 launch point_cloud_processing rtab_mapping.launch.py

ros2 run teleop_twist_keyboard teleop_twist_keyboard

## Helpful repos

https://github.com/umtclskn/ros2_kitti_publishers

https://github.com/Deepak3994/Kitti-Dataset/blob/master/raw_data_downloader.sh

https://github.com/introlab/rtabmap_ros/tree/humble-devel/rtabmap_demos/launch

https://github.com/introlab/rtabmap/wiki/Installation#rtab-map-desktop-ubuntu-1804-2004-2204

https://github.com/introlab/rtabmap_ros#installation

