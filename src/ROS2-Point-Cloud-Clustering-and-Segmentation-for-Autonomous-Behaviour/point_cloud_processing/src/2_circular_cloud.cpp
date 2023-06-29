#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>

int main(){
    // Data type(PointXYZ) used in point cloud library pcl for representing a 3D point cloud
    pcl::PointCloud<pcl::PointXYZRGB> cloud ;
    double radius = 3.0;
    int num_points = 50;
    double angular_step_size = 2.0 * M_PI /num_points;

    for(int i=0;i<num_points;i++){
    pcl::PointXYZRGB point;
    double angle = i * angular_step_size;
    point.x = radius * std::cos(angle);
    point.y = radius * std::sin(angle);
    point.z = 1.0;

    point.r = 255 * std::cos(angle);
    point.r = 255 * std::sin(angle);
    point.b = 255 * std::cos(angle + M_PI_2);
    cloud.push_back(point);
    }
    // cloud.push_back(pcl::PointXYZ(1.0,2.0,3.0));
    // cloud.push_back(pcl::PointXYZ(4.0,5.0,6.0));
    // cloud.push_back(pcl::PointXYZ(7.0,9.0,9.0));
    // cloud.push_back(pcl::PointXYZ(10.0,11.0,12.0));
    // cloud.push_back(pcl::PointXYZ(12.0,14.0,-15.0));
    std::string path = "/home/rohit/pcl_ws/src/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Behaviour/point_cloud_processing/point_clouds/circular.pcd";
    pcl::io::savePCDFileASCII(path,cloud);
    // std::cout<<cloud.size();
    return 0;
}
